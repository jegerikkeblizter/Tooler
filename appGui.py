import tkinter as tk
import app
import gui

welcome_label = tk.Label(app.homepage_frame, text=f"Welcome", font=("Arial", 14), fg="white", bg='#2e2e2e')
welcome_label.pack(pady=10, anchor="center")

# Buttons
youtube_button = tk.Button(app.homepage_frame, text="Gå til YouTube Video Downloader", command=gui.show_youtube_page, font=("Arial", 12), bg="#4caf50", fg="white")
youtube_button.pack(pady=10, anchor="center")

picchanger_button = tk.Button(app.homepage_frame, text="Gå til Picture File Type Changer", command=gui.show_picchanger_page, font=("Arial", 12), bg="#4caf50", fg="white")
picchanger_button.pack(pady=10, anchor="center")