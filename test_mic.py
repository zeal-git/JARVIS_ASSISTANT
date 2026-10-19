import sounddevice as sd 
from scipy.io.wavfile import write 
fs = 44100
duration = 5
print ("Recording...")

audio = sd.rec(
    int(duration * fs),
    samplerate = fs,
    channels =1,
    dtype='int16'
)

sd.wait()

write("recording.wav", fs, audio)

print("Saved as recording.wav")