import numpy as np
from functionTp6 import assemblerLesNotes, superposeSon
from IPython.display import Audio,display
import time
from scipy.io import wavfile
samplerate, data = wavfile.read('accompaniment.wav')
dataMono = data[:,0]
fe=44100
dataMono = superposeSon(dataMono,np.zeros(33))
display(Audio(dataMono, rate=fe,autoplay=True))