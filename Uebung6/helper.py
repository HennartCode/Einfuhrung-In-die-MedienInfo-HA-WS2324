def wkm2sound(morse_text, filename="morse.wav", fs=44100, freq=800, t_short=0.1, t_long=0.2, t_wait=0.1, t_pause=0.3):
    import numpy as np
    from scipy.io import wavfile
    
    if (not all(c in '._|' for c in morse_text)):
        raise ValueError("Morsetext must only contain . _ | chracters")
        
    if (t_short == t_long):
        raise UserWarning("Time for short long and short period must not be the same.")
    elif (t_short > t_long):
        raise ValueError("Time for short period must be smaller than the long period")
    if (freq * 2 >= fs):
        raise ValueError("Beep frequency must be under half the samplerate")
    
    w = np.zeros(int(fs * t_wait))
    N = {
        '.': np.sin((np.arange(0, int(fs * t_short)) / fs) * 2 * np.pi * freq),
        '_': np.sin((np.arange(0, int(fs * t_long)) / fs) * 2 * np.pi * freq),
        '|': np.zeros(int(fs * t_pause))
    }
    # N_short = np.sin((np.arange(0, int(samplerate * t_short)) / fs) * 2 * np.pi * freq)
    # N_long =  np.sin((np.arange(0, int(samplerate * t_long)) / fs) * 2 * np.pi * freq)
    # N_pause = np.zeros(int(fs * t_pause))
    
    signal = np.concatenate([np.concatenate((N[k],w)) for k in morse_text])
    wavfile.write(filename, fs, signal)
    # return signal