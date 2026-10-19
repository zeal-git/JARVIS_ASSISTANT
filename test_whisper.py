from faster_whisper import WhisperModel

model = WhisperModel("base")

segments, info = model.transcribe("recording.wav")

print("Recognized Text:")

for segment in segments:
    print(segment.text)