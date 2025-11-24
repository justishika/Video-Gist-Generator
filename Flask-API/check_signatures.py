import inspect
from youtube_transcript_api import YouTubeTranscriptApi

print('repr:', repr(YouTubeTranscriptApi))
for name in ['fetch','list','get_transcript']:
    if hasattr(YouTubeTranscriptApi, name):
        func = getattr(YouTubeTranscriptApi, name)
        try:
            print(name, 'callable:', callable(func))
            print(name, 'signature:', inspect.signature(func))
        except Exception as e:
            print(name, 'signature error:', repr(e))
    else:
        print(name, 'not present')
