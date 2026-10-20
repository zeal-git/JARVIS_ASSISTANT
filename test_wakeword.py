from wakeword.wakeword import load_wakeword_model
import sounddevice as sd
import numpy as np
# from wakeword.wakeword import test_microphone

# test_microphone()

print("Loading wake word model.....")

model = load_wakeword_model()

print("Model loaded!")
print("Listening for 5 seconds...")

audio = sd.rec(
    # 16000,    #16000 samples/sec x 1 = 160000
    80000, #16000  samples/sec x 5 sec = 80,000
    samplerate=16000,
    channels=1,
    dtype="int16"
)

sd.wait()

print("Audio captured!")

audio = audio.flatten() #added new

#added new
print("Audio shape:", audio.shape)
print("Audio maximum:", np.max(np.abs(audio)))
print("Audio minimum:", np.min(audio))

# prediction = model.predict(audio.flatten()) # temp commented for new code 
prediction = model.predict(audio) #til here added new 

print("Prediction:")
print(prediction)

# print("Wake word model loaded succesfully!")