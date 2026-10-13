"""Build the initial, source-linked edition. No network requests."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CHECKED='2026-10-12'
stories=[]
def story(id,category,title,date,source,url,summary,why,technical,caveat,tags,event_date=None,featured=False):
    stories.append(dict(id=id,category=category,title=title,published=date,event_date=event_date,source=source,url=url,summary=summary,why=why,technical=technical,caveat=caveat,tags=tags,kind='explained',editorial_status='AI-assisted · source-linked',checked=CHECKED,featured=featured))
story('gpt-intelligent-ui','ai','ChatGPT is moving beyond the text box.','2026-10-07','OpenAI','https://openai.com/index/gpt-6-for-everyone/',
'OpenAI introduced GPT-6 with Intelligent UI: answers can combine text with useful interactive elements, including calculators and comparisons.',
'A useful question is no longer just “Can it answer?” but “Can it give me a tool to explore the answer?” Try asking for an interactive explanation of an engineering concept.',
'The model helps choose a response format. An interactive interface is an application capability, not proof that every calculation or underlying claim is correct.',
'The announcement distinguishes Chat from Work and Codex. Availability and reasoning-mode support vary; check the official release rather than assuming every model has the same features.',
['ChatGPT','Models','Applications'],featured=True)
story('codex-predictions','ai','Codex can suggest what you might ask next.','2026-10-09','OpenAI','https://help.openai.com/en/articles/6825453-chatgpt-release-notes',
'OpenAI’s 9 October release notes describe a beta that proposes the next message in a Codex conversation.',
'This is a small example of software becoming more proactive. You still choose whether the suggested instruction is useful.',
'Accepting a prediction fills the composer; it does not automatically send the message. Prediction and permission to act are different things.',
'The beta has plan, age, app and model restrictions. Check the dated release notes before expecting it in your account.',
['Codex','Agents','Developer tools'])
story('embedding-gemma','ai','A search model that connects words, images and sound.','2026-10-06','Google DeepMind','https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/',
'Google announced EmbeddingGemma 2, a model that maps different kinds of content into a shared numerical representation for retrieval.',
'Imagine searching a collection of engineering videos with a spoken description. Related content can be found by meaning, not only by matching filenames.',
'An embedding is a vector: a list of numbers. A trained model places related inputs near one another under a chosen similarity measure. This is not the same task as generating a conversational answer.',
'Google’s benchmark and device-performance claims come from the model’s developer. Real performance depends on the data, hardware and search task.',
['Models','Open models','Retrieval'])
story('heat-shield','engineering','Testing tomorrow’s heat shields on a spacecraft’s final journey.','2026-10-09','NASA','https://www.nasa.gov/centers-and-facilities/ames/nasa-demonstrates-next-generation-heat-shield-technologies/',
'NASA describes KREPE-3: 12 small experimental capsules carried inside a departing cargo spacecraft to test thermal-protection materials during re-entry.',
'It is a practical engineering lesson: use an existing mission to collect difficult, expensive-to-reproduce flight data.',
'The capsules carry sensors for quantities including temperature, pressure and motion. Those measurements help assess how candidate heat-shield materials behave under real re-entry conditions.',
'A demonstration gathers evidence. It does not by itself qualify a material for every future crewed mission. The source describes planned measurement steps as well as the hardware.',
['Aerospace','Materials','Testing'])
story('sspicy','engineering','Autonomous spacecraft inspection—without touching the target.','2026-10-08','NASA','https://www.nasa.gov/centers-and-facilities/ames/nasas-sspicy-mission-to-demonstrate-in-space-inspection-technologies/',
'NASA’s SSPICY technology demonstration launched on 1 October. Its Otter spacecraft is intended to inspect up to four inactive objects in low Earth orbit.',
'This connects computer vision, guidance, controls and propulsion: software must make decisions that move real hardware safely.',
'Sensors and vision support navigation, while electric propulsion enables manoeuvres. Inspections are intended to measure properties such as rotation, orientation and surface condition.',
'Inspections are planned to begin in early 2027. The mission will not dock with or repair the objects; those are potential future applications, not completed achievements.',
['Aerospace','Autonomy','Controls'],event_date='2026-10-01')
story('wing-paint','engineering','How glowing paint helps engineers understand a wing.','2026-10-02','NASA','https://www.nasa.gov/centers-and-facilities/langley/nasa-model-wing-lights-up-during-first-pressure-sensitive-paint-tests/',
'NASA used unsteady pressure-sensitive paint on a benchmark wing in its Transonic Dynamics Tunnel. Cameras record changes in the coating’s brightness.',
'For an aircraft project, this shows how experiments can check a simulation rather than simply trusting its colourful plots.',
'After calibration, the optical response can be related to surface pressure. Time-resolved measurements help researchers study changing aerodynamic loads and improve models.',
'Brightness is not a direct measurement of lift. Lift requires combining the pressure distribution with surface geometry and considering other forces. NASA describes a particular testing milestone, not the invention of pressure-sensitive paint.',
['Aerodynamics','Testing','Simulation'])
story('esa-vast','engineering','ESA and Vast plan cooperation beyond the ISS.','2026-10-05','ESA','https://www.esa.int/Newsroom/Press_Releases/The_European_Space_Agency_and_Vast_Build_on_Existing_Mission_Collaborations_and_Strengthen_Cooperation_on_Post-ISS',
'ESA and Vast signed a memorandum of understanding to continue their collaboration and explore future cooperation in low Earth orbit.',
'Space engineering is shaped by business models as well as hardware. Future stations require operators, customers, funding and technical compatibility.',
'A memorandum of understanding sets out an intention to work together. It is not the same thing as an operational station or a completed mission.',
'The announcement concerns preparatory cooperation as the ISS approaches the end of its service. Do not read it as a guarantee of a specific future mission.',
['Aerospace','Industry','Business'])
story('ai-financing','finance','Who is paying for the AI build-out?','2026-10-06','European Central Bank','https://www.ecb.europa.eu/press/blog/date/2026/html/ecb.blog20261006~35bf3c24cb.en.html',
'An ECB analysis examines how investment in AI-intensive euro-area sectors is financed, and why the funding mix matters for monetary policy.',
'Following AI means following both capability and capital. A promising technology still needs someone to fund chips, infrastructure and development.',
'Debt is borrowed money with repayment obligations; equity is an ownership claim. Different financing structures can change how investment reacts to interest rates.',
'This is an analysis of sectors and financing, not a prediction that AI stocks will rise. Keep the source’s scope separate from a global claim.',
['AI × Finance','Investment','Economics'])
story('circular-ai','finance','When AI companies are also each other’s investors and customers.','2026-10-01','Bank for International Settlements','https://www.bis.org/publications/bulletin-137-circular-relationships-among-ai-firms',
'A BIS bulletin examines circular investment relationships among AI firms.',
'Funding announcements are easier to understand when you ask who supplies the money, who receives it and what commercial relationships sit alongside the investment.',
'Investment flows and customer revenue are different quantities. Connected transactions need to be analysed together, rather than treating every headline number as independent demand.',
'A circular relationship does not automatically mean misconduct or artificial revenue. The details and evidence matter; read the bulletin before drawing conclusions about an individual firm.',
['AI × Finance','Investment','Risk'])
story('ecb-account','finance','A new release can describe an older interest-rate decision.','2026-10-08','European Central Bank','https://www.ecb.europa.eu/press/accounts/2026/html/ecb.mg261008~a10153d090.en.html',
'The ECB published its account of the 9–10 September monetary-policy meeting on 8 October. The meeting included a 25-basis-point rate increase.',
'The release helps readers understand the reasoning behind the decision. It is not a fresh rate increase on the publication date.',
'One basis point is 0.01 percentage points. A 25-basis-point rise means adding 0.25 percentage points—for example, 3.00% to 3.25%, not a 25% increase.',
'The example is illustrative, not a statement of the ECB’s actual policy-rate level. Publication date and event date are shown separately here.',
['Economics','Rates','Markets'],event_date='2026-09-10')

learn=[]
def lesson(id,title,category,summary,sections,source,url,tags,minutes=2):
 learn.append(dict(id=id,title=title,category=category,summary=summary,sections=[{'title':a,'text':b} for a,b in sections],source=source,url=url,tags=tags,minutes=minutes,checked=CHECKED))
lesson('model-vs-product','ChatGPT is the product. GPT is a model family.','ai','Start with this distinction and a lot of AI news becomes less confusing.',[
('The simple version','A model is the trained system that processes inputs and generates outputs. ChatGPT is an application that combines models with an interface, instructions, tools and product features.'),
('An engineering analogy','Think engine versus vehicle. The same engine can appear in different vehicles, and a vehicle’s usefulness also depends on its controls and equipment. This is an analogy, not an exact technical equivalence.'),
('The technical bit','The API lets software send structured requests to a model. Using ChatGPT’s interface and building an application with an API are different workflows. A model name alone does not tell you which tools a particular application exposes.'),
('When you read the news','Ask: is this a model release, a product feature, an API change, or a new way to access an existing capability?')], 'OpenAI developer documentation','https://developers.openai.com/api/docs',['ChatGPT','Models'])
lesson('agents','What makes an AI system “agentic”?','ai','A goal, tools and a loop—not a magical employee.',[
('The simple version','An agent can use a model to choose steps towards a goal, call tools, inspect results and decide what to do next. A single chatbot response does not necessarily involve this loop.'),
('A concrete example','A research assistant might search for papers, read selected results, compare findings and assemble a source-linked brief. A failed search can lead to a revised search rather than an immediate final answer.'),
('The technical bit','A common loop is: observe → decide → call a tool → inspect the result → continue or stop. The application controls available tools, budgets, state and permissions.'),
('What it does not mean','Autonomy is limited by the environment and permissions. Reliability must be measured; consequential actions need appropriate approval. A fixed scheduled script, like this site’s feed updater, is automation but not itself an AI agent.')], 'OpenAI agents guide','https://developers.openai.com/api/docs/guides/agents',['Agents','Automation'])
lesson('retrieval','RAG: giving a model the right pages before it answers.','ai','Retrieval-augmented generation, without the acronym fog.',[
('The simple version','First retrieve relevant information. Then provide it to a model as context for its answer. RAG does not normally retrain the model each time you add a document.'),
('An example','For a question about a wing test, retrieve the relevant test report instead of asking the model to rely only on learned information.'),
('The technical bit','A retrieval system may split documents into chunks, represent them with embeddings and rank matches. Keyword search or a combination can also be used. The selected passages enter the model’s context.'),
('The catch','The system can retrieve the wrong passage, miss a key section or misinterpret correct evidence. A citation is useful only when it genuinely supports the claim.')], 'OpenAI retrieval guide','https://developers.openai.com/api/docs/guides/retrieval',['Retrieval','Models'])
lesson('evaluations','How to read an AI benchmark without being fooled.','ai','“Better” needs a task, a test and a comparison.',[
('Start with the task','A coding score does not directly establish reliability in finance, engineering design or an unfamiliar document workflow.'),
('Look behind the headline','Check the test set, baseline, tools allowed, number of attempts, cost and time. A system using several attempts should not silently be compared with a single-attempt result.'),
('For your own project','Write representative test questions and define success before changing the prompt or model. Keep some examples unseen until evaluation.'),
('The technical bit','An evaluation measures a system under specified conditions. It is evidence about those conditions, not a universal intelligence or safety certificate.')], 'OpenAI evaluation guidance','https://developers.openai.com/api/docs/guides/evals',['Evaluation','Models'])
lesson('simulation','A simulation is a prediction, not a wind tunnel.','engineering','Why validation matters even when the plot looks convincing.',[
('The simple version','A simulation solves a mathematical approximation of a physical system. Real experiments help test whether that approximation is good enough for the decision you need to make.'),
('For an aircraft','Geometry, operating conditions, mesh, boundary conditions and modelling assumptions all affect the result. Compare predicted loads or flow features with measurements where possible.'),
('Two different checks','Verification asks whether you solved the chosen equations correctly. Validation asks whether the model represents reality adequately for its intended use.'),
('What to ask in a news story','What was tested? At what scale and operating conditions? What was measured? A laboratory result should not silently become a claim of production readiness.')], 'NASA modelling and simulation standard','https://standards.nasa.gov/standard/NASA/NASA-STD-7009',['Simulation','Testing'])
lesson('feedback','Feedback control: measure, compare, correct.','engineering','The basic loop behind stabilising an aircraft.',[
('The simple version','Measure what a system is doing, compare that with the desired behaviour, and use an actuator to change it.'),
('A wing-level example','An aircraft attitude controller can compare measured pitch with desired pitch and command an elevator. The aircraft’s response changes the next measurement.'),
('The technical bit','The error can be written e(t) = r(t) − y(t). Here t is time, r is the reference, y is the measured output and e is their difference. Their units must match.'),
('Why it is not automatic success','Sensor noise, delays, actuator limits and incorrect models can degrade performance or destabilise a loop. More aggressive correction is not always better.')], 'University of Michigan: Control Tutorials','https://ctms.engin.umich.edu/CTMS/index.php?example=Introduction&section=ControlPID',['Controls','Autonomy'])
lesson('rates','Why interest rates matter beyond your savings account.','finance','Follow the borrowing, spending and investment channels.',[
('The simple version','An interest rate is a price associated with borrowing money over time. A central bank influences financial conditions through its policy decisions.'),
('The connection','Higher borrowing costs can make some purchases and business projects less attractive. Changes also affect saving incentives and can influence exchange rates and asset valuations.'),
('The technical bit','The transmission mechanism is the set of channels linking monetary policy to economic activity and prices. The effects take time and depend on other conditions.'),
('Avoid the shortcut','A rate move does not guarantee an immediate stock-market move in one direction. Expectations and the reasons for the decision matter too. This is education, not a trading instruction.')], 'Bank of England: interest rates','https://www.bankofengland.co.uk/explainers/how-do-increases-in-interest-rates-affect-the-economy',['Rates','Economics'])
lesson('risk','Risk versus uncertainty—and why backtests can mislead.','finance','A strong-looking historical result is not a promise.',[
('The simple version','A backtest applies a strategy to past data. It can reveal weaknesses, but it cannot guarantee future performance.'),
('The trap','Repeatedly tuning a strategy on the same history can fit accidents in the data. That is overfitting: learning the noise instead of a durable relationship.'),
('The engineering connection','A model that fits one wind-tunnel condition may fail elsewhere. Financial models also need testing outside the conditions used to build them.'),
('A better reading habit','Look for unseen test periods, realistic costs, a sensible baseline and how large the losses could be. Treat claimed returns without those details cautiously.')], 'Investor.gov: investment risk','https://www.investor.gov/introduction-investing/investing-basics/what-risk',['Risk','Markets'])
lesson('reading-docs','How to read documentation without reading everything.','ai','Start with one question, not the whole manual.',[
('Choose a question','For example: “Can this tool search my files, and what access does it need?” This gives you a reason to read.'),
('Read in layers','Read the overview, then one relevant example, then the limitations. Only open the detailed reference when you need an exact parameter or rule.'),
('Translate the result','Write one sentence explaining what the feature does, one practical use and one limitation. Follow the source link whenever wording or availability matters.'),
('Keep the surfaces separate','ChatGPT Help explains the product. API documentation explains how software calls models and tools. The Model Spec describes intended behaviour, not a guarantee that every response will follow it.')], 'OpenAI documentation','https://developers.openai.com/api/docs',['Documentation','ChatGPT'])

# The hub links to originals rather than mirroring copyrighted documentation.
docs=[
 ('chat-release','Release notes','What changed in ChatGPT?','Start here when someone mentions a new feature. Read the date and the rollout restrictions.','https://help.openai.com/en/articles/6825453-chatgpt-release-notes','Product',True),
 ('capabilities','ChatGPT capabilities','What can the application actually do?','A product-level map of tools for text, files, audio, data and more.','https://help.openai.com/en/articles/9260256-chatgpt-capabilities-overview','Product',False),
 ('files-audio','Files and audio','Work with lecture material','Check supported uploads and limitations before planning a workflow around your notes.','https://help.openai.com/en/articles/8555545-uploading-files-and-audio-to-chatgpt','Product',False),
 ('plugins','Plugins and connected apps','Understand tools and permissions','Learn what gets connected, which actions are available and how access is controlled.','https://help.openai.com/en/articles/20001256-plugins-in-chatgpt','Product',True),
 ('privacy','Data controls','Know what happens to your data','Check training controls and privacy settings before uploading sensitive material.','https://help.openai.com/en/articles/7730893-data-controls-faq','Product',False),
 ('model-guide','Current GPT model guide','Read model differences at the source','Use the current guide rather than an old comparison chart. Capability, latency and access are separate questions.','https://developers.openai.com/api/docs/guides/latest-model','Developer',True),
 ('api-start','API overview','How an application talks to a model','Start here for requests, responses and building software with models.','https://developers.openai.com/api/docs','Developer',False),
 ('agents-doc','Building agents','Tools, state and orchestration','Compare the available agent-building approaches before choosing a framework.','https://developers.openai.com/api/docs/guides/agents','Developer',True),
 ('retrieval-doc','Retrieval','Ground answers in your documents','Learn how searching documents differs from training a model.','https://developers.openai.com/api/docs/guides/retrieval','Developer',False),
 ('evals-doc','Evaluations','Test whether a workflow works','Define success, use representative examples and check regressions.','https://developers.openai.com/api/docs/guides/evals','Developer',False),
 ('model-spec','Model Spec','Intended assistant behaviour','Read this for intended behavioural rules—not as a guarantee of perfect output.','https://model-spec.openai.com/','Behaviour',True),
 ('all-releases','All OpenAI release notes','ChatGPT, Codex and API updates','Keep product changes separate from changes intended for developers.','https://openai.com/products/release-notes/','Releases',True),
]
docdata=[dict(id=i,title=t,question=q,summary=s,url=u,track=tr,monitor=m,checked=CHECKED) for i,t,q,s,u,tr,m in docs]
models=[
 dict(name='GPT',provider='OpenAI',type='General-purpose models',description='Distinguish the GPT model family from ChatGPT, Codex and API features. Compare capabilities on your own tasks.',url='https://developers.openai.com/api/docs/guides/latest-model',tags=['Reasoning','Multimodal','Tools']),
 dict(name='Claude',provider='Anthropic',type='General-purpose models',description='Use the official model overview for current versions, supported inputs, context and API details.',url='https://docs.anthropic.com/en/docs/about-claude/models/overview',tags=['Language','Coding','Tools']),
 dict(name='Gemini',provider='Google',type='General-purpose models',description='Read the developer model documentation separately from announcements about the Gemini app.',url='https://ai.google.dev/gemini-api/docs/models',tags=['Multimodal','Developer tools']),
 dict(name='Open-weight ecosystem',provider='Multiple developers',type='Downloadable model weights',description='Inspect each model card and licence. Downloadable weights do not automatically mean unrestricted use or fully open training data.',url='https://huggingface.co/models',tags=['Model cards','Local inference']),
 dict(name='Embedding models',provider='Multiple developers',type='Retrieval and similarity',description='Turn content into numerical vectors for search and matching. An embedding model is not interchangeable with a conversational model.',url='https://developers.openai.com/api/docs/guides/embeddings',tags=['Retrieval','Search']),
]
glossary=[
('Token','A unit a model processes, often a word fragment; not a fixed number of characters.'),
('Context window','The amount of tokenised information a model can process in one request, subject to the model and API limits.'),
('Inference','Running a trained model on an input to produce an output.'),
('Training','Adjusting model parameters using data and an optimisation process.'),
('Embedding','A numerical representation of content, often used for similarity and retrieval.'),
('Agent','A system that uses a model to select actions and tools in a multi-step workflow.'),
('Hallucination','Plausible-looking model output that is unsupported or incorrect.'),
('Multimodal','Able to work with more than one kind of input or output, such as text and images.'),
('API','An interface through which software makes requests to another system.'),
('Latency','The delay before a system responds; specify whether measuring first output or total completion.'),
('Basis point','0.01 percentage points. A change of 25 basis points is 0.25 percentage points.'),
('Equity','An ownership interest in a business, rather than a loan to it.'),
('Debt','Borrowed money with contractual repayment obligations.'),
('Validation','Checking whether a model represents reality adequately for its intended use.'),
('Feedback','Using measurements of a system to influence its subsequent behaviour.'),
]
feeds=[
 dict(id='openai',name='OpenAI News',category='ai',url='https://openai.com/news/rss.xml',homepage='https://openai.com/news/',region='Global',hosts=['openai.com'],max_items=12),
 dict(id='google',name='Google AI',category='ai',url='https://blog.google/technology/ai/rss/',homepage='https://blog.google/innovation-and-ai/',region='Global',hosts=['blog.google','deepmind.google','research.google'],max_items=12),
 dict(id='hf',name='Hugging Face',category='ai',url='https://huggingface.co/blog/feed.xml',homepage='https://huggingface.co/blog',region='Global',hosts=['huggingface.co'],max_items=8),
 dict(id='nasa',name='NASA',category='engineering',url='https://www.nasa.gov/feed/',homepage='https://www.nasa.gov/news/recently-published/',region='US / global missions',hosts=['nasa.gov'],max_items=12,keywords=['engineer','technology','propulsion','robot','autonom','wing','aircraft','material','manufactur','heat shield','inspection','sensor','spacecraft','mission']),
 dict(id='esa',name='European Space Agency',category='engineering',url='https://www.esa.int/rssfeed/Our_Activities/Space_Engineering_Technology',homepage='https://www.esa.int/Enabling_Support/Space_Engineering_Technology',region='Europe / global missions',hosts=['esa.int'],max_items=10),
 dict(id='mit',name='MIT News',category='engineering',url='https://news.mit.edu/rss/feed',homepage='https://news.mit.edu/',region='US / global research',hosts=['mit.edu'],max_items=10,keywords=['robot','engineer','battery','material','energy','manufactur','semiconductor','sensor','machine learning','artificial intelligence']),
 dict(id='ecb',name='European Central Bank',category='finance',url='https://www.ecb.europa.eu/rss/press.html',homepage='https://www.ecb.europa.eu/home/html/index.en.html',region='Europe',hosts=['ecb.europa.eu'],max_items=12),
 dict(id='bis',name='Bank for International Settlements',category='finance',url='https://www.bis.org/doclist/all_pressrels.rss',homepage='https://www.bis.org/',region='Global',hosts=['bis.org'],max_items=10),
]
stories.append(dict(
 id='ultrasound-kenya-ai', category='ai', title='AI ultrasound research reaches clinics in Kenya and the US.',
 published='2026-10-06', event_date=None, source='Google Research',
 url='https://blog.google/innovation-and-ai/models-and-research/google-research/blind-sweep-ultrasounds-ai/',
 summary='Google describes a study in Nairobi and Chicago combining simpler ultrasound probe movements with AI analysis of the resulting videos.',
 why='It is a useful example of designing AI around a practical barrier: access to specialist skills, not just the accuracy of a model in isolation.',
 technical='Operators follow a set sweep pattern. A model processes the videos to estimate pregnancy stage and fetal position; Google reports that processing happens on the device.',
 caveat='The October article discusses research, not proof of universal clinical availability or a replacement for all sonographer tasks. This is technology reporting, not medical guidance.',
 tags=['Applications','Kenya','Healthcare','On-device AI'], kind='explained',
 editorial_status='AI-assisted · source-linked', checked=CHECKED, featured=False))
data=dict(site={'name':'Kirish’s Brief','tagline':'A little clearer. A little further.','edition_date':CHECKED,'editorial_checked':CHECKED},stories=stories,lessons=learn,docs=docdata,models=models,glossary=[dict(term=a,meaning=b) for a,b in glossary],sources=feeds)
(ROOT/'content/editorial.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
(ROOT/'content/feeds.json').write_text(json.dumps(feeds,ensure_ascii=False,indent=2)+'\n')
print(f'Seeded {len(stories)} stories, {len(learn)} lessons, {len(docs)} documentation guides.')
