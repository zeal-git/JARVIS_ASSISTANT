from wakeword.wakeword import load_wakeword_model
import sounddevice as sd
import numpy as np


print("Loading wake word model.....")

model = load_wakeword_model()

print("Model loaded!")
print("Listening for 5 seconds...")

audio = sd.rec(
    80000,
    samplerate=16000,
    channels=1,
    dtype="int16"
)

sd.wait()

audio = audio.flatten()

print("Audio captured!")
print("Audio shape:", audio.shape)
print("Audio maximum:", np.max(np.abs(audio)))
print("Audio minimum:", np.min(audio))

print("Running wake word detection...")

chunk_size = 1280
highest_score = 0.0

for i in range(0, len(audio), chunk_size):

    chunk = audio[i:i + chunk_size]

    if len(chunk) < chunk_size:
        continue

    prediction = model.predict(chunk)

    score = float(prediction["hey_jarvis"])

    if score > highest_score:
        highest_score = score

print()
print("Highest wake-word score:", highest_score)

if highest_score > 0.5:
    print("HEY JARVIS DETECTED!")
else:
    print("Wake word not detected.")