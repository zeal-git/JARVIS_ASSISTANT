import sounddevice as sd
from scipy.io.wavfile import write 

def record(duration=5, filename="recording.wav" ):
    fs = 16000
    
    print("Listening....")
    
    audio = sd.rec(
        int(duration * fs),
        samplerate = fs,
        channels = 1,
        dtype = 'int16'
    )
    
    sd.wait()
    
    write(filename, fs, audio)
    
    print("Recording complete")