from speech.listen import transcribe
from speech.speak import speak
from brain.brain import process
from speech.record import record
from wakeword.wakeword import wait_for_wake_word

print ("Jarvis in online....")

while True:
    
    wait_for_wake_word()
    
    record()
    text = transcribe("recording.wav")
    
    if not text:
        continue
    
    text = text.lower().strip()
     
    print("You:", text)
    
    if "stop" in text:
        speak("Goodbye Zeal.")
        break
    
    response = process(text) 

    print("Jarvis:", response)

    speak(response)