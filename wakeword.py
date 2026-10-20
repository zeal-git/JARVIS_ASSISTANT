*/wakeword/wakeword.py/*

import sounddevice as sd
import numpy as np
from openwakeword.model import Model
import threading

   
WAKE_THRESHOLD = 0.5


def load_wakeword_model():
    model = Model(
        wakeword_models=["hey_jarvis"],
        inference_framework="onnx"  
    )

    return model


def wait_for_wake_word():

    model = load_wakeword_model()
    
    detected = threading.Event()
    
    print("Jarvis is Online.")
    print("Searching for 'Hey Jarvis'...")

    # print("JARVIS is listening for 'Hey Jarvis'...")

    def audio_callback(indata, frames, time, status):

        if status:
            # print(status)
            print("Audio status:", status)

        audio = indata[:, 0]

        prediction = model.predict(audio)

        score = float(prediction["hey_jarvis"])

        # print("Wake word score:", score)

        if score > WAKE_THRESHOLD:
            detected.set()
            # print("HEY JARVIS DETECTED!")
            
    with sd.InputStream(
        samplerate=16000,
        channels=1,
        dtype="int16", 
        blocksize=1280,
        callback=audio_callback
    ):
        
        detected.wait()
        
    print("SUCCESS: JARVIS WAKE WORD DETECTED!")

    return True
        
        # while True:
        #     sd.sleep(1000)
