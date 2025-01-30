import tkinter as tk
import youtubedown
import gui


def youtube_frame(frame):

    def handle_youtube_download():
        youtube_url = url_entry.get()
        selected_file_type = file_type.get()
        youtubedown.start_download(youtube_url, selected_file_type)

    global youtube_tk_frame
    youtube_tk_frame = tk.Frame(frame)

    global handle_youtube
    handle_youtube = handle_youtube_download

    youtube_page_label = tk.Label(frame, text="YouTube Video Downloader", font=("Arial", 16), fg="white", bg='#2e2e2e')
    youtube_page_label.pack(pady=20)

    # YouTube video downloader UI elements
    url_label = tk.Label(frame, text="Enter YouTube URL:", font=("Arial", 12), fg="white", bg='#2e2e2e')
    url_label.pack(pady=5)

    url_entry = tk.Entry(frame, width=50, font=("Arial", 10))
    url_entry.pack(pady=5, ipady=5)

    file_type_label = tk.Label(frame, text="Select File Type:", font=("Arial", 12), fg="white", bg='#2e2e2e')
    file_type_label.pack(pady=10)

    file_type = tk.StringVar(value="mp4")
    mp4_radio = tk.Radiobutton(frame, text="MP4", variable=file_type, value="mp4", font=("Arial", 10), fg="white", bg='#2e2e2e', selectcolor="#4caf50")
    mp4_radio.pack()

    mp3_radio = tk.Radiobutton(frame, text="MP3", variable=file_type, value="mp3", font=("Arial", 10), fg="white", bg='#2e2e2e', selectcolor="#4caf50")
    mp3_radio.pack()

    # Download button now calls handle_youtube_download
    download_button = tk.Button(frame, text="Download", font=("Arial", 12), bg="#4caf50", fg="white", command= handle_youtube )
    download_button.pack(pady=20)

    back_button_youtube = tk.Button(frame, text="Back to Homepage", command=gui.go_home, font=("Arial", 12), bg="#f44336", fg="white")
    back_button_youtube.pack(pady=10)

