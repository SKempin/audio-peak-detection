# Audio signal peaks to list / CSV

A Python script utilising [Librosa](https://librosa.github.io/) to log the timing (in milliseconds) of audio peaks in an MP3 file.

This was originally intended to detect peaks in an audio signal that is not is constant time, and therefore doesn't have a consistant BPM.

Peak timings are output to both the console and a CSV file.

## Getting started

Ensure you have input the path to your audio file in `peaks-detection.py` line `10`.

```
$ pip install -r requirements.txt
$ python peaks-detection.py
```

## Utils

Utils contains useful additional scripts that utilise [Pydub](http://pydub.com/), [Scipy](https://www.scipy.org/) and [Matplotlib](https://matplotlib.org/) for WAV to MP3 conversion and graph plotting.
