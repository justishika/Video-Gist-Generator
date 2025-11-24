import json
from youtube_transcript_api import YouTubeTranscriptApi

vid = 'Y5wajKa4iz8'

print('Checking video id:', vid)

# instantiate API (methods are instance methods)
api = YouTubeTranscriptApi()

# Try fetch if available
if hasattr(api, 'fetch'):
    try:
        r = api.fetch(vid)
        print('fetch: OK, type=', type(r))
        # FetchedTranscript might be iterable or have .entries
        if hasattr(r, 'entries'):
            entries = r.entries
            print('fetch entries:', len(entries))
            print('sample:', json.dumps([{'text': e.get('text', '')} for e in entries[:2]], ensure_ascii=False))
        elif isinstance(r, list):
            print('fetch items:', len(r))
            print('sample:', json.dumps(r[:2], ensure_ascii=False))
        else:
            print('fetch result:', r)
    except Exception as e:
        print('fetch: ERROR ->', repr(e))
else:
    print('fetch: not available')

# Try get_transcript if available
if hasattr(api, 'get_transcript'):
    try:
        r = api.get_transcript(vid)
        print('get_transcript: OK, items=', len(r))
        print('sample:', json.dumps(r[:2], ensure_ascii=False))
    except Exception as e:
        print('get_transcript: ERROR ->', repr(e))
else:
    print('get_transcript: not available')

# Try list if available
if hasattr(api, 'list'):
    try:
        r = api.list(vid)
        print('list: OK, type=', type(r))
        if hasattr(r, 'fetch'):
            try:
                fetched = r.fetch()
                print('list.fetch: OK, type=', type(fetched))
                if hasattr(fetched, 'entries'):
                    entries = fetched.entries
                    print('list.fetch entries:', len(entries))
                    print('sample:', json.dumps([{'text': e.get('text', '')} for e in entries[:2]], ensure_ascii=False))
                elif isinstance(fetched, list):
                    print('list.fetch items:', len(fetched))
                    print('sample:', json.dumps(fetched[:2], ensure_ascii=False))
                else:
                    print('list.fetch result:', fetched)
            except Exception as e:
                print('list.fetch: ERROR ->', repr(e))
    except Exception as e:
        print('list: ERROR ->', repr(e))
else:
    print('list: not available')
