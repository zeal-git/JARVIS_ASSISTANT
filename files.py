import os 

def open_downloads():
    try:
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        os.startfile(downloads_path)
        return "Opening Downloads folder."
    except Exception as e:
        return f"Error opening Downloads folder: {e}"
    
def create_folder(folder_name):
    try:
        downloads_path = os.path.join(
            os.path.expanduser("~"),
            "Downloads",
            folder_name
        )
        
        os.makedirs(downloads_path, exist_ok=True)
        
        return f"Folder '{folder_name}' created in Downloads."
    
    except Exception as e:
        return f"Error creating folder: {e}"
        