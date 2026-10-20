*/automation/browser.py/

import webbrowser
import os


def open_youtube():
    try:
        webbrowser.open("https://www.youtube.com")
        return "Opening Youtube"
    except Exception as e:
        return f"Error opening youtube: {e}"
def open_google():
    try:
        webbrowser.open("https://www.google.com")
        return "Opening Google"
    except Exception as e:
        return f"Error opening google: {e}"

def open_github():
    try:
        webbrowser.open("https://github.com")
        return "Opening Github"
    except Exception as e:
        return f"Error opening github: {e}"
