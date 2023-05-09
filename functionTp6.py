import numpy as np
from IPython.display import Audio,display
import time
import matplotlib.pyplot as plt

def note(frequence,amplitude,duree):
    '''
    Cette fonction crée une note. Vous pouvez choisir la fréquence (Hz), l'amplitude et la durée (s) du signal.
    ex : la = note(440,1,1)
    '''
    t1 = np.arange(0,duree,1/44100) 
    divAmpli = 3
    decPhase = 0.1112*2*np.pi
    y1 = amplitude*np.sin(2 * np.pi* frequence * t1)
    '''
    for i in range (1,1):
        amplitude_i = amplitude/(divAmpli*i)
        decPhase_i = decPhase*i
        frequence_i = (i+1)*frequence
        y1 = y1 + amplitude_i*np.sin(2 * np.pi* frequence_i * t1+decPhase_i)
    
    sizSig = t1.shape[0] 
    y1 =y1*np.linspace(1,0.3,sizSig) 
    '''
    return y1

def superposeSon(son1,son2):
    l1 = np.size(son1)
    l2 = np.size(son2)
    z = np.zeros(np.abs(l2-l1))
    if l1>l2:
        son2 = np.concatenate((son2,z))
    else:
        son1 = np.concatenate((son1,z))
    son = son1 + son2
    return son

        
def assemblerLesNotes(signal):
    '''
    Cette fonction permet d'assembler les notes les unes derrières les autres.
    Exemple: 
    note1 = note(440,1,1)
    note2 = note(493,1,0.5)
    note3 = note(520,10,1)
    signalDe3Notes = assemblerLesNotes((note1,note2,note3))
    '''
    nbNotes = len(signal)
    signal2 = signal[0]
    trou = np.zeros(10)
    for i in range(1,nbNotes):
        signal2 = np.concatenate( (signal2,trou,signal[i]) )
        
    return signal2

def voirLeSignal(signal):
    '''
    Cette fonction permet de tracer le graphe du signal
    Exemple: 
    note1 = note(440,1,0.01)
    voirLeSignal(note1)
    '''
    plt.close('all')
    fe = 44100
    te = 1/fe
    lengthSignal = signal.shape[0]
    t = np.arange(0,lengthSignal)*te
    plt.plot(t,signal)
    plt.xlabel('time (s)')
    plt.ylabel('Son')
    plt.show()
    return 1

def entendreLeSon(y):
    '''
    Cette fonction permet d'entendre le son
    Exemple: 
    note1 = note(440,1,1)
    entendreLeSon(note1)
    '''
    te = 1/44100
    fe = 1/te
    duration_s = te*(y.shape[0]-1)
    # Play the waveform out the speakers
    if np.max(y)>1:
        display(Audio(y, rate=fe,autoplay=True))
    else:
        display(Audio(y, rate=fe,autoplay=True,normalize=False))
    
    
    return 1
 

