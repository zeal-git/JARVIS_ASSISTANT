*/speech/listen.py/*

from faster_whisper import WhisperModel

# model = WhisperModel("base")
model = WhisperModel("small")

def transcribe(audio_file):
    segments, info = model.transcribe(audio_file)

    text = ""

    for segment in segments:
        text += segment.text + " "

    return text.strip()


if __name__ == "__main__":
    result = transcribe("../recording.wav")
    print("Recognized Text:")
    print(result)
