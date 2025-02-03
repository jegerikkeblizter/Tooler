import os
import subprocess
import threading
from CTkMessagebox import CTkMessagebox
import customtkinter as Ctk

ffmpeg_path = os.path.join(os.path.dirname(__file__), 'ffmpeg.exe')

def select_file():
    file_path = Ctk.filedialog.askopenfilename(filetypes=[("Media Files", "*.mp4;*.avi;*.mkv;*.mov;*.mp3;*.wav")])
    if file_path:
        CTkMessagebox(title="File Selected", message=f"Selected: {os.path.basename(file_path)}")
    return file_path

def convert_media_threaded(file_path, output_format):
    """Starter en ny tråd for konverteringen."""
    thread = threading.Thread(target=convert_media, args=(file_path, output_format))
    thread.start()

def convert_media(file_path, output_format):
    if not file_path:
        CTkMessagebox(title="Error", message="Please select a file first")
        return
    
    output_file = os.path.splitext(file_path)[0] + f".{output_format}"
    
    try:
        if output_format in ["mp3", "wav"]:
            subprocess.run([ffmpeg_path, "-y", "-i", file_path, "-q:a", "0", "-map", "a", output_file], check=True)
        else:
            subprocess.run([ffmpeg_path, "-y", "-i", file_path, output_file], check=True)
        CTkMessagebox(title="Success", message=f"File converted successfully to {output_file}")
    except subprocess.CalledProcessError:
        CTkMessagebox(title="Error", message="Conversion failed")

def delete_original(file_path):
    if not file_path:
        CTkMessagebox(title="Error", message="No file selected to delete")
        return
    
    confirm = CTkMessagebox(title="Confirm", message="Are you sure you want to delete the original file?", option_1="Yes", option_2="No")
    if confirm.get() == "Yes":
        try:
            os.remove(file_path)
            CTkMessagebox(title="Deleted", message="Original file deleted successfully")
        except Exception as e:
            CTkMessagebox(title="Error", message=f"Failed to delete file: {str(e)}")
