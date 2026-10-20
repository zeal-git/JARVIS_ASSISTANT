*/automation/apps.py/*

import os
import subprocess

def open_vscode():
    try:
        subprocess.Popen(["code"])
        return "Opening Visual Studio Code"
    except Exception as e:
        return f"Erorr open Visual Studio Code: {e}"
def open_notepad():
    try:
        subprocess.Popen(["notepad"])
        return "Open Notepad"
    except Exception as e:
        return f"Error opening Notepad: {e}"
def open_task_manager():
    try:
        subprocess.Popen("taskmgr", shell=True)
        return "Open Task Manager"
    except Exception as e:
        return f"Error opening Task Manager: {e}"
def open_calculator():
    try:
        subprocess.Popen(["calc"])
        return "Open Calculator"
    except Exception as e:
        return f"Error opening Calculator: {e}"
