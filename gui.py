import tkinter as tk
from PIL import Image
import imgConverter
import youtubeGui
import app

def show_youtube_page():
    app.homepage_frame.pack_forget()
    imgConverter.picchanger_page_frame.pack_forget()
    youtubeGui.youtube_page_frame.pack()


# Function to show the Picture Converter page
def show_picchanger_page():
    app.homepage_frame.pack_forget()
    youtubeGui.youtube_page_frame.pack_forget()
    imgConverter.picchanger_page_frame.pack()


# Function to go back to the homepage
def go_home():
    youtubeGui.youtube_page_frame.pack_forget()
    imgConverter.picchanger_page_frame.pack_forget()
    app.homepage_frame.pack()
