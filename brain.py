*/brain/brain.py/*

import datetime
from automation.apps import open_vscode, open_notepad,open_task_manager, open_calculator
from automation.browser import open_youtube, open_google, open_github
from automation.files import open_downloads, create_folder

def process(command):

    command = command.lower()
    #browser commands
    if "open youtube" in command:
        return open_youtube()
    
    elif "open google" in command:
        return open_google()
    
    elif "open github" in command:
        return open_github()
    
    #commands
    if "open vscode" in command or "open visual studio code" in command:
        return open_vscode()
    
    elif "open notepad" in command:
        return open_notepad()
    
    elif "open task manager" in command:
        return open_task_manager()
    
    elif "open calculator" in command:
        return open_calculator()
    
    
    #files 
    elif "open downloads" in command:
        return open_downloads()
    
    elif "Create '{folder_name}' folder" in command:
        return create_folder()
    
    #conversations
    if "hello" in command or "hey" in command:
        return "Hello Zeal"

    elif "how are you" in command:
        return "I am functioning normally."

    elif "what are you doing" in command:
        return "I am helping you build Jarvis."

    elif "time" in command:
        current = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current}"
    

    else:
        return "I don't understand."
