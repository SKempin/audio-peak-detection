# Detect audio peaks with Librosa (https://librosa.github.io/librosa/)

# imports
from __future__ import print_function
import librosa
import numpy as np
import datetime

# Load local audio file
y, sr = librosa.load('path-to-file.mp3')

# Get file duration in seconds
duration = librosa.get_duration(y)

# Print duration to console
print("File duration(s): ", str(datetime.timedelta(seconds=duration)))

# Find peaks
onset_env = librosa.onset.onset_strength(y=y, sr=sr,
                                         hop_length=512,
                                         aggregate=np.median)
peaks = librosa.util.peak_pick(onset_env, 3, 3, 3, 5, 0.5, 10)

# Print peaks list to console
print('Peaks detected at: ', librosa.frames_to_time(peaks, sr=sr))

# Create CSV output
peak_times = librosa.frames_to_time(peaks, sr=sr)
librosa.output.times_csv('./output/peak_times.csv', peak_times)

# Complete message
print("Peak times output to ./output/peak_times.csv. \n Process complete.")