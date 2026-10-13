"""Offline regression tests. No tests require secrets or network access."""
from datetime import datetime, timezone
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('update', ROOT/'scripts/update.py')
u = importlib.util.module_from_spec(spec)
spec.loader.exec_module(u)
NOW = datetime(2026, 10, 12, 12, tzinfo=timezone.utc)
SOURCE = dict(id='nasa', name='NASA', category='engineering', url='https://www.nasa.gov/feed/', hosts=['nasa.gov'], max_items=10)

def rss(title='A new spacecraft test', link='https://www.nasa.gov/test/', date='Fri, 09 Oct 2026 12:00:00 GMT', description='A report about the technology.'):
    return f'<rss version="2.0"><channel><item><title>{title}</title><link>{link}</link><pubDate>{date}</pubDate><description>{description}</description></item></channel></rss>'.encode()

class FeedTests(unittest.TestCase):
    def test_rss_title_date_and_link(self):
        a = u.parse_feed(rss(), SOURCE, NOW)[0]
        self.assertEqual(a['published'], '2026-10-09')
        self.assertEqual(a['url'], 'https://www.nasa.gov/test')
        self.assertEqual(a['kind'], 'feed')
        self.assertEqual(a['summary'], '')
    def test_atom(self):
        data=b'<feed xmlns="http://www.w3.org/2005/Atom"><entry><title>Test</title><link rel="alternate" href="https://www.nasa.gov/test"/><published>2026-10-09T12:00:00Z</published><summary>Spacecraft</summary></entry></feed>'
        self.assertEqual(len(u.parse_feed(data,SOURCE,NOW)),1)
    def test_atom_updated_label(self):
        data=b'<feed xmlns="http://www.w3.org/2005/Atom"><entry><title>Test</title><link href="https://www.nasa.gov/test"/><updated>2026-10-09T12:00:00Z</updated></entry></feed>'
        self.assertEqual(u.parse_feed(data,SOURCE,NOW)[0]['date_kind'],'publisher update date')
    def test_future_dates_rejected(self):
        self.assertEqual(u.parse_feed(rss(date='Tue, 13 Oct 2026 12:00:00 GMT'),SOURCE,NOW),[])
    def test_missing_dates_not_invented(self):
        self.assertEqual(u.parse_feed(rss(date=''),SOURCE,NOW),[])
    def test_old_dates_rejected(self):
        self.assertEqual(u.parse_feed(rss(date='Mon, 01 Jan 2024 12:00:00 GMT'),SOURCE,NOW),[])
    def test_untrusted_host_rejected(self):
        self.assertEqual(u.parse_feed(rss(link='https://nasa.gov.attacker.invalid/x'),SOURCE,NOW),[])
    def test_xml_entities_rejected(self):
        with self.assertRaises(ValueError):u.parse_feed(b'<!DOCTYPE rss [<!ENTITY x "bad">]><rss/>',SOURCE,NOW)
    def test_html_source_is_not_marked_success(self):
        with self.assertRaises(ValueError):u.parse_feed(b'<html><body>Denied</body></html>',SOURCE,NOW)
    def test_keywords(self):
        src={**SOURCE,'keywords':['battery']}
        self.assertEqual(u.parse_feed(rss(),src,NOW),[])
    def test_tracking_deduplication(self):
        self.assertEqual(u.canonical_url('https://example.com/p/?utm_source=x&topic=ai#x'),'https://example.com/p?topic=ai')
    def test_subdomain_allowlist(self):
        self.assertTrue(u.allowed_url('https://science.nasa.gov/x',['nasa.gov']))
        self.assertFalse(u.allowed_url('http://www.nasa.gov/x',['nasa.gov']))
        self.assertFalse(u.allowed_url('https://user:pass@nasa.gov/x',['nasa.gov']))
        self.assertFalse(u.allowed_url('https://nasa.gov:444/x',['nasa.gov']))
    def test_failed_fetch_preserves_stories(self):
        a=u.parse_feed(rss(),SOURCE,NOW)[0]
        merged=u.merge_articles([a],[],NOW)
        self.assertEqual(len(merged),1)
    def test_merge_preserves_generated_digest(self):
        a=u.parse_feed(rss(),SOURCE,NOW)[0]
        old={**a,'kind':'auto','summary':'An existing digest.'}
        self.assertEqual(u.merge_articles([old],[a],NOW)[0]['summary'],'An existing digest.')
    def test_changed_headline_invalidates_old_digest(self):
        a=u.parse_feed(rss(),SOURCE,NOW)[0]
        old={**a,'kind':'auto','summary':'An existing digest.','title':'Old headline'}
        self.assertEqual(u.merge_articles([old],[a],NOW)[0]['kind'],'feed')
    def test_markup_removed(self):
        self.assertEqual(u.plain('<p>Useful</p><script>steal()</script><p>text</p>'),'Useful text')
    def test_digest_validation(self):
        d={'summary':'A new test occurred.','why':'It could inform a design.','technical':'A sensor measures a quantity.','caveat':'A trial is not deployment.'}
        self.assertEqual(u.validate_digest(d,'unrelated source'),d)
        with self.assertRaises(ValueError):u.validate_digest({'summary':'no'},'')
    def test_no_long_verbatim_repetition(self):
        copied='one two three four five six seven eight nine ten eleven twelve thirteen fourteen'
        d=dict(summary=copied,why='A possible interpretation.',technical='A measured quantity.',caveat='Not independently verified.')
        with self.assertRaises(ValueError):u.validate_digest(d,copied)
    def test_failed_document_does_not_replace_baseline(self):
        doc={'id':'docs','url':'https://help.openai.com/test'}
        prior={'digest':'old','checked_at':'2026-10-11T00:00:00Z'}
        with patch.object(u,'fetch',side_effect=OSError('no network')):
            r=u.check_document(doc,prior,NOW)
        self.assertFalse(r['ok']);self.assertEqual(r['digest'],'old');self.assertEqual(r['checked_at'],prior['checked_at'])
    def test_document_baseline_then_change(self):
        doc={'id':'docs','url':'https://help.openai.com/test'}
        with patch.object(u,'fetch',return_value=('<main>'+'This is a useful technical explanation. '*30+'</main>').encode()):
            first=u.check_document(doc,None,NOW)
            second=u.check_document(doc,first,NOW)
        self.assertTrue(first['baseline']);self.assertFalse(second['changed'])
        with patch.object(u,'fetch',return_value=('<main>'+'This is changed technical documentation. '*30+'</main>').encode()):
            third=u.check_document(doc,second,NOW)
        self.assertTrue(third['changed'])
    def test_offline_build_and_script_safety(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'content').mkdir();(root/'site/data').mkdir(parents=True)
            data=json.loads((ROOT/'content/editorial.json').read_text())
            data['stories'][0]['title']='</script><script>alert(1)</script>'
            u.write_json(root/'content/editorial.json',data)
            result=u.build_site(root)
            self.assertEqual(len(result['stories']),len(data['stories']))
            self.assertNotIn('</script>',(root/'site/data/brief.js').read_text())
            self.assertIsNone(result['update']['last_attempt'])
    def test_offline_run_retains_last_success(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'content').mkdir();(root/'site/data').mkdir(parents=True)
            data=json.loads((ROOT/'content/editorial.json').read_text());data['docs']=[]
            u.write_json(root/'content/editorial.json',data)
            u.write_json(root/'content/feeds.json',[SOURCE])
            u.write_json(root/'content/update-status.json',{'last_success':'2026-10-11T01:00:00Z'})
            with patch.object(u,'fetch',side_effect=OSError('offline')),patch.dict('os.environ',{'OPENAI_API_KEY':'','OPENAI_MODEL':''}):
                status=u.run(root,NOW)
            self.assertEqual(status['success_count'],0)
            self.assertEqual(status['failure_count'],1)
            self.assertEqual(status['last_success'],'2026-10-11T01:00:00Z')

if __name__=='__main__':unittest.main()
