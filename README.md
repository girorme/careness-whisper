Careness Whisper
---
Whisper speech model poc.

<p align="center">
 <img align="center" src="https://github.com/user-attachments/assets/6f478ecd-cb7e-43b6-a063-d49b645da5cf"/>
</p>

ref: https://github.com/openai/whisper


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
  -m MODEL, --model MODEL (default: base)
                        Model to use: tiny, base, small, medium, large, turbo
```

### Via docker

2.1. build image
> docker build -t cwhisper .

2.2 run cwhisper
> docker run -v $(pwd):/app/cwhisper cwhisper -f /app/cwhisper/record1.m4a --model base 


### Via python in your host machine
```
$ python main.py -f record1.m4a
or
$ python main.py -f record1.m4a --model MODEL
```
