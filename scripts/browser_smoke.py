#!/usr/bin/env python3
"""Optional UI smoke test. Requires Playwright and an installed Chromium.

Default: render the standalone HTML without network access.
Pass --url to test an actual local/hosted site. No API calls are made.
"""
from pathlib import Path
import argparse
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]

def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--url',help='Existing site to test, for example http://localhost:8000/')
    parser.add_argument('--chromium',help='Optional path to an installed Chromium executable')
    parser.add_argument('--output',type=Path,default=ROOT/'test-output')
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    errors=[]
    def observe(page):
        page.on('pageerror',lambda e:errors.append(str(e)))
        page.on('console',lambda m:errors.append(m.text) if m.type=='error' else None)
    def load(page):
        if args.url:
            page.goto(args.url,wait_until='networkidle')
        else:
            preview=ROOT/'kirish-brief-preview.html'
            if not preview.exists():
                raise FileNotFoundError('Run python scripts/build_preview.py first')
            page.set_content(preview.read_text(encoding='utf-8'),wait_until='load')
    def route(page,name):
        page.evaluate('(r)=>location.hash=r',name)
        page.wait_for_timeout(120)
    def nav(page,name):
        page.locator(f'a[data-nav="{name}"]').click()
        page.wait_for_timeout(120)
    with sync_playwright() as p:
        launch={'headless':True}
        if args.chromium:
            launch['executable_path']=args.chromium
        browser=p.chromium.launch(**launch)
        page=browser.new_page(viewport={'width':1440,'height':1050},device_scale_factor=1)
        observe(page);load(page)
        assert page.locator('#results .story-card').count()==8
        page.screenshot(path=str(args.output/'desktop.png'))
        page.get_by_role('button',name='A two-minute foundation').click()
        page.locator('#reader').wait_for(state='visible')
        assert 'ChatGPT is the product' in page.locator('#reader-title').inner_text()
        page.get_by_role('button',name='Mark as read',exact=False).click()
        page.get_by_role('button',name='Save for later',exact=True).click()
        page.get_by_role('button',name='Close article').click()
        page.wait_for_timeout(120)
        nav(page,'saved')
        assert page.locator('main .story-card').count()==1
        nav(page,'home')
        page.locator('#search').fill('wing')
        assert page.locator('#results .story-card').count()==1
        nav(page,'docs')
        assert page.locator('.doc-card').count()==12
        page.get_by_role('button',name='Developer',exact=True).click()
        assert page.locator('.doc-card').count()==5
        page.locator('#doc-search').fill('retrieval')
        assert page.locator('.doc-card').count()==1
        page.locator('#doc-search').fill('')
        page.get_by_role('button',name='All',exact=True).click()
        page.wait_for_timeout(2900)
        page.screenshot(path=str(args.output/'docs.png'))
        for name in ['ai','engineering','finance','models','learn','sources','about']:
            route(page,name)
            assert page.locator('main h1').count()==1,name
            assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth'),name
        route(page,'learn')
        page.locator('#learn-search').fill('agent')
        assert page.locator('#learn-results .story-card').count()==1
        route(page,'home')
        page.get_by_role('button',name='Switch colour theme').click()
        assert page.locator('html').get_attribute('data-theme')=='dark'
        page.screenshot(path=str(args.output/'dark.png'))
        page.get_by_role('button',name='Switch colour theme').click()
        mobile=browser.new_page(viewport={'width':390,'height':844},device_scale_factor=1,is_mobile=True,has_touch=True)
        observe(mobile);load(mobile)
        mobile.screenshot(path=str(args.output/'mobile.png'),full_page=True)
        assert mobile.evaluate('document.documentElement.scrollWidth <= window.innerWidth')
        mobile.get_by_role('button',name='Open navigation',exact=True).click()
        nav(mobile,'docs')
        assert not mobile.locator('#sidebar').evaluate('(e)=>e.classList.contains("open")')
        assert mobile.locator('.doc-card').count()==12
        for name in ['models','learn','sources','about']:
            route(mobile,name)
            assert mobile.evaluate('document.documentElement.scrollWidth <= window.innerWidth'),name
        assert not errors,errors
        browser.close()
    print('PASS: desktop/mobile navigation, dialogs, session bookmarks, filters, search, dark mode and overflow. No browser console errors.')
    print('Mode:', 'real URL' if args.url else 'offline embedded HTML; persistent storage is not available on this opaque origin')

if __name__=='__main__':main()
