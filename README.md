Careness Whisper
---
Whisper speech model poc.

### Usage
1. Install deps:

- ffmpeg
- libs

```
$ pip install -r requirements.txt
```

2. Script usage
```
usage: main.py [-h] -f FILE [-m MODEL]

Audio Transcription Script

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Path to the audio file
  -m MODEL, --model MODEL
                        Model to use: tiny, base, small, medium, large, turbo
```

```
$ python main.py -f record1.m4a
or
$ python main.py -f record1.m4a --model MODEL
```