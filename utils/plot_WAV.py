# Plot WAV to graph 
# Utilises Scipy (https://www.scipy.org/) and Matplotlib (https://matplotlib.org/)

# Imports
from scipy.io.wavfile import read
import matplotlib.pyplot as plt

# Load local WAV files
input_data = read("../sounds/sample.wav")
audio = input_data[1]

# Plot to graph
plt.plot(audio)
plt.show()

# Print compelte message to console
print("WAV plotting complete")
