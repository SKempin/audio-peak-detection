# Convert WAV file(s) to MP3 using Pydub (http://pydub.com/)

# Imports
import os
import pydub
import glob

# Load local WAV files(s)
wav_files = glob.glob('../test/*.wav')

# Iterate and convert
for wav_file in wav_files:
    mp3_file = os.path.splitext(wav_file)[0] + '.mp3'
    sound = pydub.AudioSegment.from_wav(wav_file)
    sound.export(mp3_file, format="mp3")
    os.remove(wav_file)

# Print complete message to console
print("WAV to MP3 conversion complete")

