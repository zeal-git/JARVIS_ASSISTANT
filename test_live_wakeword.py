*/wakeword/test_live_wakeword.py/*

from wakeword.wakeword import wait_for_wake_word

print("Starting JARVIS...")

result = wait_for_wake_word()

print("Wake word function returned:", result)

if result is True:
   print("SUCCESS: JARVIS is awake!")
# wait_for_wake_word()
