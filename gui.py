import tkinter as tk
import imgGui
import youtubeGui
import app

def show_youtube_page():
    homepage_frame.pack_forget()
    imgGui.image_tk_frame.pack_forget()
    youtubeGui.youtube_tk_frame.pack()


# Function to show the Picture Converter page
def show_picchanger_page():
    homepage_frame.pack_forget()
    youtubeGui.youtube_tk_frame.pack_forget()
    imgGui.image_tk_frame.pack()

def go_home():
    youtubeGui.youtube_tk_frame.pack_forget()
    imgGui.image_tk_frame.pack_forget()
    app.homepage_frame.pack()
