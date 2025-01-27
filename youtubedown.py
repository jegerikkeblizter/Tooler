import os
import subprocess
from tkinter import messagebox, filedialog

ffmpeg_path = os.path.join(os.path.dirname(__file__), 'ffmpeg.exe')
yt_dlp_path = os.path.join(os.path.dirname(__file__), 'yt-dlp.exe')

def check_dependencies():
    if not os.path.exists(yt_dlp_path):
        return "yt-dlp executable is missing. Please include yt-dlp.exe in the same directory as this script."
    if not os.path.exists(ffmpeg_path):
        return "ffmpeg executable is missing. Please include ffmpeg.exe in the same directory as this script."
    return None

def download_youtube_video(youtube_url, output_path, file_type):
    try:
        if file_type == "mp4":
            format_option = "bestvideo+bestaudio/best"
            extra_options = ["--merge-output-format", "mp4", "--postprocessor-args", "-c:a aac"]
        elif file_type == "mp3":
            format_option = "bestaudio"
            extra_options = ["--extract-audio", "--audio-format", "mp3"]
        else:
            return "Unsupported file type."

        video_path = os.path.join(output_path, "%(title)s.%(ext)s")
        command = [
            yt_dlp_path,  # Explicit path to yt-dlp
            "-f", format_option,
            "-o", video_path,
            "--ffmpeg-location", ffmpeg_path
        ] + extra_options + [youtube_url]

        subprocess.run(command, check=True)
        return "Download completed successfully!"
    except subprocess.CalledProcessError as e:
        return f"An error occurred during download: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def start_download(youtube_url, file_type):
    if not youtube_url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return

    error = check_dependencies()
    if error:
        messagebox.showerror("Dependency Error", error)
        return

    output_directory = filedialog.askdirectory(title="Select Download Directory")
    if not output_directory:
        messagebox.showerror("Error", "Please select a download directory")
        return

    status_message = download_youtube_video(youtube_url, output_directory, file_type)
    messagebox.showinfo("Download Status", status_message)
