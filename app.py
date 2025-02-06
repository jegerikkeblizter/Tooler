import customtkinter as Ctk
from CTkMessagebox import CTkMessagebox
import youtubedown
import imgConverter
import videoConverter
import speedtest
from PIL import Image
import time
import threading
import os
import ffmpeg
import cv2
import numpy as np
import mss
import pytesseract
import pygetwindow as gw
from deep_translator import GoogleTranslator
import keyboard
import mouse
import ctypes
from time import sleep
import random
import sys
import os

# Fix potential sys.stdout issues in PyInstaller EXE
if sys.stdout is None:
    sys.stdout = open(os.devnull, "w")
if sys.stderr is None:
    sys.stderr = open(os.devnull, "w")


class App(Ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Tooler")
        self.geometry("800x500")

        self.current_frame = None
        self.menu_frame = None
        self.show_homepage()

        #dette er for oversettelse toolen
        #----------------------------------
        self.running = False
        self.bbox = None
        self.custom_bbox = None  
        self.last_messages = []
        #----------------------------------


    def show_homepage(self):
        if self.current_frame or self.menu_frame:
            self.current_frame.destroy()
            self.menu_frame.destroy()
            
        self.destroy_main_interface()

        self.current_frame = Ctk.CTkFrame(self, corner_radius=0, border_color="black", border_width=0.7)
        self.current_frame.pack(side="right", fill="both", expand=True)

        self.menu_frame = Ctk.CTkFrame(self, fg_color="#21266B", corner_radius=0, border_color="black", border_width=0.7)
        self.menu_frame.pack(side="left", fill="both")

        label = Ctk.CTkLabel(self.current_frame, text="Welcome To Tooler!", font=("Arial", 25, "bold"))
        label.pack(pady=20)

        whats_new = Ctk.CTkLabel(self.current_frame, text="Whats new? ", font=("Arial", 20))
        whats_new.pack(side="top", padx=(0,400), pady=(30,0))

        whats_new_text = Ctk.CTkLabel(self.current_frame, text="• Changed from Tkinter to CustomTkinter\n\n""• Updated UI\n\n""• Added ICO picture\n\n""• Cleaned up code\n\n""• MORE NEW TOOLS!\n\n""• New logo\n\n""• New brand name", justify="left" ,font=("Arial", 15))
        whats_new_text.pack(side="left", padx=(60,0), pady=(0,130))

        def get_resource_path(relative_path):
            if getattr(sys, 'frozen', False):  # Sjekker om programmet kjører som en .exe
                base_path = sys._MEIPASS  # Midlertidig mappe for PyInstaller
            else:
                base_path = os.path.abspath(".")

            return os.path.join(base_path, relative_path)

        # Hent riktig filbane
        image_path = get_resource_path("wave.png")

        # Opprett CustomTkinter Image med riktig bane
        water = Ctk.CTkImage(
            light_image=Image.open(image_path),
            dark_image=Image.open(image_path),
            size=(300, 200)
        )

        # Bruk bildet i en CTkLabel
        water_wave = Ctk.CTkLabel(self.current_frame, text="", image=water)
        water_wave.pack(side="right", pady=(0, 150))


        button = Ctk.CTkButton(self.menu_frame, text="Youtube Downloader", command=self.show_youtube)
        button.pack(pady=20, padx=10)

        button2 = Ctk.CTkButton(self.menu_frame, text="Image Converter", command=self.show_imgconverter)
        button2.pack()

        button3 = Ctk.CTkButton(self.menu_frame, text="Speed Test", command=self.show_speedtest)
        button3.pack(pady=20)

        button4 = Ctk.CTkButton(self.menu_frame, text="Video Converter", command=self.show_video_converter)
        button4.pack()

        button5 = Ctk.CTkButton(self.menu_frame, text="MP4 To GIF", command=self.show_mp4togif)
        button5.pack(pady=20)

        button6 = Ctk.CTkButton(self.menu_frame, text="Chat Translator", command=self.show_translate_page)
        button6.pack()

        button7 = Ctk.CTkButton(self.menu_frame, text="Auto Clicker", command=self.show_autoclicker)
        button7.pack(pady=20)

        back_button_youtube = Ctk.CTkButton(self.menu_frame, text="Back to Homepage", command=self.show_homepage, font=("Arial", 12))
        back_button_youtube.pack(side="bottom", pady=(0,20))

    def show_youtube(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.destroy_main_interface()

        self.current_frame = Ctk.CTkFrame(self)
        self.current_frame.pack(fill="both", expand=True)
        
        def handle_youtube_download():
            youtube_url = url_entry.get()
            selected_file_type = file_type.get()
            youtubedown.start_download(youtube_url, selected_file_type)

        youtube_page_label = Ctk.CTkLabel(self.current_frame, text="YouTube Video Downloader", font=("Arial",20, "bold"))
        youtube_page_label.pack(pady=20)

        url_label = Ctk.CTkLabel(self.current_frame, text="Enter YouTube URL:", font=("Arial", 12))
        url_label.pack(pady=5)

        url_entry = Ctk.CTkEntry(self.current_frame, width=500, font=("Arial", 10))
        url_entry.pack(pady=2, ipady=6)

        file_type_label = Ctk.CTkLabel(self.current_frame, text="Select File Type:", font=("Arial", 12))
        file_type_label.pack(pady=(20, 0))

        file_type = Ctk.StringVar(value="mp4")
        mp4_radio = Ctk.CTkRadioButton(self.current_frame, text="MP4", variable=file_type, value="mp4", font=("Arial", 10))
        mp4_radio.pack(pady=(0, 10))

        mp3_radio = Ctk.CTkRadioButton(self.current_frame, text="MP3", variable=file_type, value="mp3", font=("Arial", 10))
        mp3_radio.pack()

        download_button = Ctk.CTkButton(self.current_frame, text="Download", font=("Arial", 12), command=handle_youtube_download)
        download_button.pack(pady=20)
    
    def show_imgconverter(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.destroy_main_interface()

        self.current_frame = Ctk.CTkFrame(self)
        self.current_frame.pack(fill="both", expand=True)

        picchanger_label = Ctk.CTkLabel(self.current_frame, text="Picture File Type Changer", font=("Arial", 20, "bold"))
        picchanger_label.pack(pady=20)

        self.img_selected_file = Ctk.StringVar()
        self.original_file = Ctk.StringVar()
        self.selected_format = Ctk.StringVar(value="jpeg")

        file_label = Ctk.CTkLabel(self.current_frame, text="Select Image File:", font=("Arial", 12))
        file_label.pack(pady=5)

        file_button = Ctk.CTkButton(self.current_frame, text="Browse", command=self.select_file, font=("Arial", 10))
        file_button.pack(pady=5)

        file_path_label = Ctk.CTkLabel(self.current_frame, textvariable=self.img_selected_file, wraplength=300, font=("Arial", 10))
        file_path_label.pack(pady=5)

        output_format_label = Ctk.CTkLabel(self.current_frame, text="Select Output Format:", font=("Arial", 12))
        output_format_label.pack(pady=10)

        output_formats = ["jpeg", "png", "webp"]
        format_menu = Ctk.CTkOptionMenu(self.current_frame, variable=self.selected_format, values=output_formats)
        format_menu.pack(pady=5)

        convert_button = Ctk.CTkButton(self.current_frame, text="Convert", command=self.start_conversion, font=("Arial", 12, "bold"))
        convert_button.pack(pady=20)

        self.delete_button = Ctk.CTkButton(self.current_frame, text="Delete Original Image", command=self.delete_original_image, font=("Arial", 12),
                                           state="disabled")
        self.delete_button.pack(pady=10)

        copyright_label = Ctk.CTkLabel(self.current_frame, text="© 2024 Dem Som Vet", font=("Arial", 10))
        copyright_label.pack(side="bottom", pady=10)

    def select_file(self):
        file_path = Ctk.filedialog.askopenfilename(
            title="Select an Image File",
            filetypes=[("Image Files", "*.jpeg *.png *.webp"), ("All Files", "*.*")]
        )
        if file_path:
            self.img_selected_file.set(file_path)
            self.delete_button.configure(state="disabled")

    def start_conversion(self):
        input_file = self.img_selected_file.get()
        output_format = self.selected_format.get()

        if not input_file:
            CTkMessagebox(title="Error", message="Please select an image file.", icon="warning")
            return

        if not output_format:
            CTkMessagebox(title="Error", message="Please select an output format.", icon="warning")
            return

        converted_file, error = imgConverter.convert_image(input_file, output_format)

        if converted_file:
            CTkMessagebox(title="Conversion Result", message=f"Image converted and saved as: {converted_file}", icon="info")
            self.delete_button.configure(state="normal")
            self.original_file.set(input_file)
        else:
            CTkMessagebox(title="Error", message=f"An error occurred: {error}", icon="error")

    def delete_original_image(self):
        original_file_path = self.original_file.get()

        if not original_file_path:
            CTkMessagebox(title="Warning", message="No original image to delete.", icon="warning")
            return

        success, message = imgConverter.delete_original_image(original_file_path)

        if success:
            CTkMessagebox(title="Success", message=message, icon="info")
            self.original_file.set("")
            self.delete_button.configure(state="disabled")
        else:
            CTkMessagebox(title="Error", message=message, icon="error")

    def show_speedtest(self):
        if self.current_frame:
            self.current_frame.destroy()
            
        self.destroy_main_interface()

        self.current_frame = Ctk.CTkFrame(self)
        self.current_frame.pack(fill="both", expand=True)

        overskrift = Ctk.CTkLabel(self.current_frame, text="Internett Speed Test", font=("Arial", 20, "bold"))
        overskrift.pack(pady=(20))

        download_progressbar = Ctk.CTkProgressBar(self.current_frame)
        download_progressbar.pack(pady=(10,10))
        download_progressbar.set(0)

        def start():
            def speedtest_function():
                st = speedtest.Speedtest()
                info_label.configure(text="Finding best server...")
                st.get_best_server()

                res_dict = st.results.dict()
                server_label.configure(text=f"HOST:{res_dict['server']['country']} | SUPPLIER:{res_dict['server']['sponsor']} | LATENCY: {res_dict['server']['latency']:.2f}")
                time.sleep(2)


                info_label.configure(text="Testing download speed.....")
                download_speed = st.download(loading_bar) / 1000000  # Convert to Mbps

                download_progressbar.set(0) 
                info_label.configure(text="Testing upload speed.....")
                upload_speed = st.upload(loading_bar) / 1000000  # Convert to Mbps

                if download_speed and upload_speed:
                    results.configure(text=f"Download Speed: {download_speed:.3f} Mbps\n"f"Upload Speed: {upload_speed:.3f} Mbps")

            thread = threading.Thread(target=speedtest_function)
            thread.start()

        start_test = Ctk.CTkButton(self.current_frame, text="start the test", command=start)
        start_test.pack(pady=10)

        info_label = Ctk.CTkLabel(self.current_frame, text="")
        info_label.pack(pady=5)

        server_label = Ctk.CTkLabel(self.current_frame, text="")
        server_label.pack(pady=(10,2))

        results = Ctk.CTkLabel(self.current_frame, text="")
        results.pack()

        def loading_bar(i, request_count, end=False, start=False):
            if end == True:
                progress = (i + 1)/request_count
                download_progressbar.set(progress)
    
    def show_video_converter(self):
        if self.current_frame:
                self.current_frame.destroy()

        self.destroy_main_interface()
            
        self.current_frame = Ctk.CTkFrame(self)
        self.current_frame.pack(fill="both", expand=True)
            
        file_var = Ctk.StringVar()
        format_var = Ctk.StringVar(value="mp4")
            
        video_label = Ctk.CTkLabel(self.current_frame, text="Video Converter", font=("Arial", 20 ,"bold"))
        video_label.pack(pady=(20))
            
        select_file_button = Ctk.CTkButton(self.current_frame, text="Select Media File", command=lambda: file_var.set(videoConverter.select_file()))
        select_file_button.pack(pady=20)
            
        format_menu = Ctk.CTkComboBox(self.current_frame, values=["mp4", "avi", "mkv", "mov", "mp3", "wav"], variable=format_var)
        format_menu.pack(pady=10)
            
        convert_button = Ctk.CTkButton(self.current_frame, text="Convert", command=lambda: videoConverter.convert_media(file_var.get(), format_var.get()))
        convert_button.pack(pady=10)
            
        delete_button = Ctk.CTkButton(self.current_frame, text="Delete Original File", command=lambda: videoConverter.delete_original(file_var.get()))
        delete_button.pack(pady=10)
            
        video_warning_label = Ctk.CTkLabel(self.current_frame, text="Warning: Big video files with high quality and frame rate can cause high pc usage!", font=("Arial",12), text_color="Red")
        video_warning_label.pack(pady=10)

    
    def show_mp4togif(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.destroy_main_interface()

        self.current_frame = Ctk.CTkFrame(self)
        self.current_frame.pack(fill="both", expand=True)

        ffmpeg_path = os.path.join(os.path.dirname(__file__), 'ffmpeg.exe')
        self.selected_file = None

        def check_ffmpeg():
            if not os.path.exists(ffmpeg_path):
                CTkMessagebox (title="Error", text="FFmpeg not found at {ffmpeg_path}. Please ensure 'ffmpeg.exe' is in the script directory.", icon="warning")
                return False
            return True

        def select_file():
            root = Ctk.CTk()
            root.withdraw()
            root.update()
            file_path = Ctk.filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
            root.destroy()
            if file_path:
                self.selected_file = file_path
                selected_label.configure(text=f"Selected file: {self.selected_file}")
            else:
                selected_label.configure(text=f"No Selected file.")

        def mp4_to_gif(fps: int = 10, scale: int = -1):
            def gif_start():

                if not check_ffmpeg():
                    return

                if not self.selected_file:
                    CTkMessagebox(message="An error occurred, No file is choosen!", title="ERROR 903", icon="warning")

                if not os.path.exists(self.selected_file):
                    raise FileNotFoundError (CTkMessagebox(text=f"Input file {self.selected_file} does not exist."))
                
                self.selected_file = self.selected_file
                
                output_file = os.path.splitext(self.selected_file)[0] + ".gif"
                
                try:
                    (
                        ffmpeg
                        .input(self.selected_file)
                        .filter('fps', fps=fps)
                        .filter('scale', scale, -1)
                        .output(output_file, format='gif')
                        .run(cmd=ffmpeg_path, overwrite_output=True)
                    )
                    CTkMessagebox(title="Success", message=f"Successfully converted {self.selected_file} to {output_file}")
                except ffmpeg.Error as e:
                    CTkMessagebox(title="Error", message=f"Error converting file: {e}", icon="warning")
        
            thread_gif = threading.Thread(target=gif_start)
            thread_gif.start()


        def start_conv_gif():
            mp4_to_gif(fps=15, scale=500)

        def delete_original_mp4():
            if self.selected_file:
                try:
                    os.remove(self.selected_file)
                    return True, CTkMessagebox (message=f"The original image file {self.selected_file} has been deleted.", title="Success")
                except Exception as e:
                    return False, CTkMessagebox(message=f"An error occurred while deleting the file: {e}", title="ERROR 554", icon="warning")
            elif not self.selected_file:
                CTkMessagebox(message="An error occurred, No file is choosen!", title="ERROR 903", icon="warning")


        mp4_to_gif_label = Ctk.CTkLabel(self.current_frame, text="MP4 To GIF", font=("Arial", 20, "bold"))
        mp4_to_gif_label.pack(pady=20)

        select_button = Ctk.CTkButton(self.current_frame, text="Select file", command=select_file, font=("Arial", 12))
        select_button.pack(pady=10)

        selected_label = Ctk.CTkLabel(self.current_frame, text="")
        selected_label.pack(pady=5)

        conver_gif_button = Ctk.CTkButton(self.current_frame, text="Convert", command=start_conv_gif, font=("Arial", 12))
        conver_gif_button.pack(pady=15)

        delete_original_button = Ctk.CTkButton(self.current_frame, text="Delete original file", command=delete_original_mp4)
        delete_original_button.pack(pady=15)

    def show_translate_page(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.destroy_main_interface()

        pytesseract.pytesseract.tesseract_cmd = r"Tesseract-OCR\tesseract.exe"

        self.current_frame = Ctk.CTkFrame(self)
        self.current_frame.pack(fill="both", expand=True)

        translate_page_label = Ctk.CTkLabel(self.current_frame, text="Chat Translator", font=("Arial", 20, "bold"))
        translate_page_label.pack(pady=(20))

        self.window_var = Ctk.StringVar()
        self.window_dropdown = Ctk.CTkComboBox(self.current_frame, variable=self.window_var, values=self.get_window_list())
        self.window_dropdown.pack(pady=5)

        self.refresh_button = Ctk.CTkButton(self.current_frame, text="Refresh list", command=self.update_window_list)
        self.refresh_button.pack(pady=5)

        self.select_area_button = Ctk.CTkButton(self.current_frame, text="Select area", command=self.select_capture_area)
        self.select_area_button.pack(pady=5)

        self.output_text = Ctk.CTkTextbox(self.current_frame, width=500, height=200)
        self.output_text.pack(pady=5)

        self.start_button = Ctk.CTkButton(self.current_frame, text="Start", command=self.start_translation, state="disabled")
        self.start_button.pack(pady=5)

        self.stop_button = Ctk.CTkButton(self.current_frame, text="Stop", command=self.stop_translation, state="disabled")
        self.stop_button.pack(pady=5)

        steps = [
            "1. Refresh list and choose your window.",
            "2. Click 'select area' button and a window will open with a screenshot of your chosen window",
            "3. drag you mouse to select the chat that will be translated and monitored. when your done click 'enter' to confirm. if you dont want to confirm press 'c' which will not confirm and close the window.",
            "4. when you have selected your area the chat will say something like: ✅ Area selected: (999, 999, 999, 999)",
            "5. then all you need to do is click start and the app will read up every chat and translate them to Norwegian.",
            "The language that the AI can read are the following: Russain, Norwagian, Chinese traditional, Chinese simple, Dutch, French, Spanish, Japanese and English. our team is working on adding more in the future!"
        ]


        def open_tutorial():
            tutorial_window = Ctk.CTkToplevel(self.current_frame)
            tutorial_window.geometry("500x400")
            tutorial_window.title("Tutorial")
            tutorial_window.attributes("-topmost", True)

            main_frame = Ctk.CTkFrame(tutorial_window)
            main_frame.pack(fill="both", expand=True, padx=10, pady=10)

            for step in steps:
                step_label = Ctk.CTkLabel(main_frame, text=step, font=("Arial", 14), wraplength=480)
                step_label.pack(pady=5, padx=10, anchor="w")

            close_button = Ctk.CTkButton(main_frame, text="Lukk", command=tutorial_window.destroy)
            close_button.pack(pady=20)
            
        tutorial_button = Ctk.CTkButton(self.current_frame, text="Tutorial", command=open_tutorial, corner_radius=100, width=30)
        tutorial_button.pack(side="right", pady=(0,5), padx=(0,5))

    def get_window_list(self):
        return [win.title for win in gw.getAllWindows() if win.title]

    def update_window_list(self):
        self.window_dropdown.configure(values=self.get_window_list())

    def get_window_bbox(self, window_title):
        try:
            win = gw.getWindowsWithTitle(window_title)[0]
            return (win.left, win.top, win.right, win.bottom)
        except IndexError:
            self.output_text.insert("end", "❌ Window not found! Try again.\n")
            return None

    def select_capture_area(self):
        window_title = self.window_var.get()
        bbox = self.get_window_bbox(window_title)

        if not bbox:
            return

        x1, y1, x2, y2 = bbox

        with mss.mss() as sct:
            screenshot = np.array(sct.grab(bbox))
            screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)

        # Sett maksimal bredde og høyde for OpenCV-vinduet
        MAX_WIDTH = 800   # Juster denne for å endre max bredde
        MAX_HEIGHT = 600  # Juster denne for å endre max høyde

        # Finn skalering basert på maks verdier
        height, width, _ = screenshot.shape
        scale_factor = min(MAX_WIDTH / width, MAX_HEIGHT / height, 1.0)  # Maks 1.0 (ingen oppskalering)

        # Skaler bildet om nødvendig
        if scale_factor < 1.0:
            resized_screenshot = cv2.resize(screenshot, (0, 0), fx=scale_factor, fy=scale_factor)
        else:
            resized_screenshot = screenshot

        # Velg område med cv2.selectROI()
        roi = cv2.selectROI("Select area (Press ENTER to confirm)", resized_screenshot, fromCenter=False, showCrosshair=True)
        cv2.destroyAllWindows()

        if roi != (0, 0, 0, 0):
            x, y, w, h = roi

            # Konverter ROI-koordiner tilbake til original størrelse hvis bildet var skalert
            x = int(x / scale_factor)
            y = int(y / scale_factor)
            w = int(w / scale_factor)
            h = int(h / scale_factor)

            self.custom_bbox = (x1 + x, y1 + y, x1 + x + w, y1 + y + h)
            self.output_text.insert("end", f"✅ Area selected: {self.custom_bbox}\n")
            self.start_button.configure(state="normal")


    def capture_text_from_window(self):
        with mss.mss() as sct:
            while self.running:
                if self.custom_bbox:
                    screenshot = sct.grab(self.custom_bbox)
                    img = np.array(screenshot)
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                    # OCR - use multiple languages
                    extracted_text = pytesseract.image_to_string(gray, lang="rus+eng+deu+fra+spa+ita+chi_sim+jpn").strip()

                    # Split text into separate messages
                    messages = extracted_text.split("\n")

                    for message in messages:
                        message = message.strip()
                        if message and message not in self.last_messages:
                            self.last_messages.append(message)  # Store message to prevent repetition

                            # Ensure list doesn't grow too large
                            if len(self.last_messages) > 10:
                                self.last_messages.pop(0)

                            try:
                                translated_text = GoogleTranslator(source="auto", target="no").translate(message)
                                self.output_text.insert("end", f"{translated_text}\n")
                                self.output_text.yview_moveto(1)
                            except Exception as e:
                                self.output_text.insert("end", "⚠ Translation error, check your connection!\n")

                time.sleep(1)

    def start_translation(self):
        if not self.custom_bbox:
            self.output_text.insert("end", "⚠ Select an area first!\n")
            return

        self.running = True
        self.start_button.configure(state="disabled")
        self.stop_button.configure(state="normal")

        threading.Thread(target=self.capture_text_from_window, daemon=True).start()

    def stop_translation(self):
        self.running = False
        self.start_button.configure(state="normal")
        self.stop_button.configure(state="disabled")
        self.output_text.insert("end", "🛑 Translation stopped.\n")

    def destroy_main_interface(self):
            if hasattr(self, 'main_frame') and self.main_frame:
                self.main_frame.destroy()
                self.main_frame = None  # Fjern referanse

            if hasattr(self, 'info_frame') and self.info_frame:
                self.info_frame.destroy()
                self.info_frame = None  # Fjern referanse
                
            if hasattr(self, 'buttons_frame') and self.buttons_frame:
                self.buttons_frame.destroy()
                self.buttons_frame = None  # Set to None after destruction

    def show_autoclicker(self):
        if self.current_frame:
            self.current_frame.destroy()
            
        self.destroy_main_interface()

        self.stop_main_thread = False

        self.interval_ms = Ctk.StringVar(value='100')
        self.interval_s = Ctk.StringVar(value='0')
        self.interval_min = Ctk.StringVar(value='0')
        self.interval_hr = Ctk.StringVar(value='0')

        self.interval_ms.trace('w', lambda x, y, z: self.validate(self.interval_ms))
        self.interval_s.trace('w', lambda x, y, z: self.validate(self.interval_s))
        self.interval_min.trace('w', lambda x, y, z: self.validate(self.interval_min))
        self.interval_hr.trace('w', lambda x, y, z: self.validate(self.interval_hr))

        self.mouse_button = Ctk.StringVar(value='Left')
        self.hotkey = Ctk.StringVar(value='f8')

        self.super_mode = Ctk.BooleanVar(value=False)

            # Advanced options
        self.random_time_offset_enabled = Ctk.BooleanVar(value=False)
        self.random_time_offset = Ctk.StringVar(value='0')

        self.random_mouse_offset_enabled = Ctk.BooleanVar(value=False)
        self.random_mouse_offset_x = Ctk.StringVar(value='0')
        self.random_mouse_offset_y = Ctk.StringVar(value='0')

        self.click_type = Ctk.StringVar(value='Single')
        self.hold_duration = Ctk.StringVar(value='0')

        self.repeat_option = Ctk.StringVar(value='Toggle')
        self.repeat_value = Ctk.StringVar(value='0')

        self.killswitch_hotkey = Ctk.StringVar(value='Ctrl+Shift+K')


        self.random_time_offset.trace('w', lambda x, y, z: self.validate(self.random_time_offset))
        self.random_mouse_offset_x.trace('w', lambda x, y, z: self.validate(self.random_mouse_offset_x))
        self.random_mouse_offset_y.trace('w', lambda x, y, z: self.validate(self.random_mouse_offset_y))
        self.hold_duration.trace('w', lambda x, y, z: self.validate(self.hold_duration))
        self.repeat_value.trace('w', lambda x, y, z: self.validate(self.repeat_value))

        self.main_frame = MainFrame(self)
        self.buttons_frame = ButtonsFrame(self)
        self.info_frame = InfoFrame(self)

        keyboard.add_hotkey('Ctrl+Shift+K', self.destroy)

    def get_interval_sum(self) -> float | int:
        return (self.normalize(self.interval_ms) * 0.001
                + self.normalize(self.interval_s)
                + self.normalize(self.interval_min) * 60
                + self.normalize(self.interval_hr) * 3600)

    def start_clicking(self) -> None:
        self.stop_main_thread = False

        keyboard.remove_hotkey(self.hotkey.get())
        self.buttons_frame.start_button.configure(state='disabled')
        self.buttons_frame.stop_button.configure(state='normal')

        keyboard.add_hotkey(self.hotkey.get(), self.stop_clicking)

        threading.Thread(
            target=self.clicking_thread,
            daemon=True
        ).start()

    def stop_clicking(self) -> None:
        self.stop_main_thread = True

        keyboard.remove_hotkey(self.hotkey.get())

        self.buttons_frame.start_button.configure(state='normal')
        self.buttons_frame.stop_button.configure(state='disabled')

        keyboard.add_hotkey(self.hotkey.get(), self.start_clicking)

    def clicking_thread(self) -> None:

        if self.super_mode.get():
            user32 = ctypes.WinDLL('user32', use_last_error=True)
                # Directly calling system to click even faster (really unstable)
                # Ignores all preferences for speed performance
                # 0x201 - LEFTBUTTONDOWN
                # 0x202 - LEFTBUTTONUP
            while not self.stop_main_thread:
                user32.mouse_event(0x201, 0, 0, 0, 0)
                user32.mouse_event(0x202, 0, 0, 0, 0)
            exit()

        mouse_button = self.mouse_button.get().lower()
        click_interval = self.get_interval_sum()

        if self.repeat_option.get() == 'Repeat':
            self.repeat_clicking(mouse_button, click_interval)
        else:
            self.toggle_clicking(mouse_button, click_interval)

        exit()

    def repeat_clicking(self, mouse_button, click_interval) -> None:
        repeat_amount = int(self.repeat_value.get())
        while not self.stop_main_thread and repeat_amount > 0:

            if self.random_mouse_offset_enabled:
                x = random.randint(
                    -int(self.random_mouse_offset_x.get()), int(self.random_mouse_offset_x.get())
                )
                y = random.randint(
                    -int(self.random_mouse_offset_y.get()), int(self.random_mouse_offset_y.get())
                )
                mouse.move(x, y, absolute=False)

            mouse.press(mouse_button)
            sleep(int(self.hold_duration.get()) / 1000)
            mouse.release(mouse_button)

            if self.click_type.get() == 'Double':
                mouse.press(mouse_button)
                sleep(int(self.hold_duration.get()) / 1000)
                mouse.release(mouse_button)

            sleep(
                click_interval + random.uniform(0, int(self.random_time_offset.get()) / 1000)
                if self.random_time_offset_enabled else click_interval
            )

            if self.random_mouse_offset_enabled:
                mouse.move(-x, -y, absolute=False)

            repeat_amount -= 1

        self.stop_clicking()

    def toggle_clicking(self, mouse_button, click_interval) -> None:
        while not self.stop_main_thread:

            if self.random_mouse_offset_enabled.get():
                x = random.randint(
                        -int(self.random_mouse_offset_x.get()), int(self.random_mouse_offset_x.get())
                )
                y = random.randint(
                    -int(self.random_mouse_offset_y.get()), int(self.random_mouse_offset_y.get())
                )
                mouse.move(x, y, absolute=False)

            mouse.press(mouse_button)
            sleep(int(self.hold_duration.get()) / 1000)
            mouse.release(mouse_button)

            if self.click_type.get() == 'Double':
                mouse.press(mouse_button)
                sleep(int(self.hold_duration.get()) / 1000)
                mouse.release(mouse_button)

            sleep(click_interval + random.uniform(0, int(self.random_time_offset.get()) / 1000)
                if self.random_time_offset_enabled else click_interval)

            if self.random_mouse_offset_enabled.get():
                mouse.move(-x, -y, absolute=False)

    def change_hotkey(self) -> None:
        keyboard.remove_hotkey(self.hotkey.get())
        hotkey_created = False
        new_hotkey = []
        used_modifiers = []
        self.buttons_frame.change_hotkey_button.configure(text='Press any key...')

        def callback(key) -> None:
            nonlocal hotkey_created
            if key.name not in keyboard.all_modifiers:
                new_hotkey.append(key.name)
                hotkey_created = True
                return
            if key.name not in used_modifiers:
                    new_hotkey.append(key.name)
                    used_modifiers.append(key.name)

        keyboard.hook(callback)

        def wait_for_callback() -> None:
            while not hotkey_created:
                sleep(0.01)
            keyboard.unhook(callback)
            hotkey = '+'.join(new_hotkey)

            self.hotkey.set(hotkey)
            keyboard.add_hotkey(self.hotkey.get(), self.start_clicking)

            self.buttons_frame.change_hotkey_button.configure(text='Change Hotkey')

            self.buttons_frame.start_button.configure(text=f"Start: {self.hotkey.get().replace('+', '-').title()}")
            self.buttons_frame.stop_button.configure(text=f"Stop: {self.hotkey.get().replace('+', '-').title()}")

            exit()

        threading.Thread(target=wait_for_callback, daemon=True).start()

    @staticmethod
    def normalize(variable: Ctk.StringVar) -> int:
        if variable.get() == '':
            return 0
        return int(variable.get())

    @staticmethod
    def validate(variable: Ctk.StringVar) -> None:
        # Should be used in entry traces
        variable_text = variable.get()
        for letter in variable_text:
            if not letter.isdigit():
                variable_text = variable_text.replace(letter, '')
            variable.set(variable_text)


class MainFrame(Ctk.CTkFrame):
    def __init__(self, master: App):
        super().__init__(master)
        self.pack(expand=True, fill='both', padx=5, pady=5)

        self.info_frame = MainFrameInfoFrame(self, master)
        self.interval_frame = IntervalFrame(self, master)


class MainFrameInfoFrame(Ctk.CTkFrame):
    def __init__(self, master, root: App):
        super().__init__(master, fg_color='transparent')
        self.pack(expand=True, fill='x')

        self.description = Ctk.CTkLabel(self, text='Click Interval:')
        self.description.pack(side='left', padx=10)

        self.advanced_options = Ctk.CTkButton(
            self,
            text='>>',
            width=40,
            command=lambda: AdvancedOptions(root),
        )
        self.advanced_options.pack(side='right', padx=5, pady=10)

        self.dropdown = Ctk.CTkOptionMenu(
            self,
            values=['Left', 'Right', 'Middle'],
            variable=root.mouse_button,
            )
            
        self.dropdown.pack(side='right', padx=5, pady=10)

        self.dropdown_label = Ctk.CTkLabel(self, text='Mouse Button:')
        self.dropdown_label.pack(side='right', padx=5, pady=10)


class IntervalFrame(Ctk.CTkFrame):
    def __init__(self, master, root: App):
        super().__init__(master, fg_color='transparent')
        self.pack(expand=True, fill='x', padx=5)

        self.label_ms = IntervalFrameLabel(self, text='Ms:')
        self.entry_ms = IntervalFrameEntry(self, root.interval_ms, width=60)

        self.label_sec = IntervalFrameLabel(self, text='Sec:')
        self.entry_sec = IntervalFrameEntry(self, root.interval_s, width=60)

        self.label_min = IntervalFrameLabel(self, text='Min:')
        self.entry_min = IntervalFrameEntry(self, root.interval_min, width=60)

        self.label_hr = IntervalFrameLabel(self, text='Hr:')
        self.entry_hr = IntervalFrameEntry(self, root.interval_hr, width=60)


class IntervalFrameEntry(Ctk.CTkEntry):
    def __init__(self, master, interval_variable, *, width):
        super().__init__(master, textvariable=interval_variable, width=width)
        self.pack(side='left', expand=True, fill='x', padx=5, pady=5)


class IntervalFrameLabel(Ctk.CTkLabel):
    def __init__(self, master, *, text):
        super().__init__(master, text=text, )
        self.pack(side='left', expand=True, fill='x', padx=5, pady=5)


class ButtonsFrame(Ctk.CTkFrame):
    def __init__(self, master: App):
        super().__init__(master, fg_color='transparent')
        self.pack(expand=True, fill='y', padx=5, pady=5)

        self.start_button = Ctk.CTkButton(
            self,
            text=f"Start: {master.hotkey.get().replace('+', '-').title()}",
            command=lambda: master.start_clicking(),
        )

        self.start_button.pack(side='left', expand=True, padx=5)

        self.stop_button = Ctk.CTkButton(
            self,
            text=f"Stop: {master.hotkey.get().replace('+', '-').title()}",
            state='disabled',
            command=lambda: master.stop_clicking(),
        )
        self.stop_button.pack(side='left', expand=True, padx=5)

        self.change_hotkey_button = Ctk.CTkButton(
            self,
            text='Change Hotkey',
            command=lambda: master.change_hotkey(),
        )
        self.change_hotkey_button.pack(side='left', expand=True, padx=5)

        keyboard.add_hotkey((master.hotkey.get()), master.start_clicking)


class InfoFrame(Ctk.CTkFrame):
    def __init__(self, master: App):
        super().__init__(master, fg_color='transparent')
        self.pack(fill='x', padx=10, pady=5)
        self.killswitch_label = Ctk.CTkLabel(self, text=f'Killswitch: {master.killswitch_hotkey.get().replace("+", "-").title()}')
        self.killswitch_label.pack(side='left')

        self.super_mode_switch = Ctk.CTkSwitch(self, text='Super Mode', variable=master.super_mode)
        self.super_mode_switch.pack(side='right', padx=5)


class AdvancedOptions(Ctk.CTkToplevel):
    def __init__(self, root: App):
        super().__init__()
        self.title("Advanced Options")
        self.grab_set()
        self.geometry(
            f"500x300"
            f"+{int(self.winfo_screenwidth() / 2 - 500 / 2)}"
            f"+{int(self.winfo_screenheight() / 2 - 300 / 2)}"
        )
        self.resizable(False, False)

        self.rowconfigure((0, 1, 2), weight=3, uniform='a')
        self.columnconfigure((0, 1), weight=1, uniform='a')

        self.root = root

        self.time_offset = TimeOffset(self)
        self.mouse_offset = MouseOffset(self)
        self.click_type = ClickType(self)
        self.repeat_options = RepeatOptions(self)
        self.killswitch = KillSwitch(self)

    def change_killswitch_hotkey(self, buttons_frame):
        keyboard.remove_hotkey(self.root.killswitch_hotkey.get())
        hotkey_created = False
        new_hotkey = []
        used_modifiers = []
        buttons_frame.change_killswitch_hotkey.configure(text='Press any key...')

        def callback(key):
            nonlocal hotkey_created
            if key.name not in keyboard.all_modifiers:
                new_hotkey.append(key.name)
                hotkey_created = True
                return
            if key.name not in used_modifiers:
                new_hotkey.append(key.name)
                used_modifiers.append(key.name)

        keyboard.hook(callback)

        def wait_for_callback():
            while not hotkey_created:
                sleep(0.01)
            keyboard.unhook(callback)
            hotkey = '+'.join(new_hotkey)

            self.root.killswitch_hotkey.set(hotkey)
            keyboard.add_hotkey(self.root.killswitch_hotkey.get(), self.root.destroy)

            buttons_frame.change_killswitch_hotkey.configure(text='Change KillSwitch Hotkey')
            buttons_frame.killswitch_hotkey.configure(
                text=f"{self.root.killswitch_hotkey.get().replace('+', '-').title()}"
            )
            self.root.info_frame.killswitch_label.configure(text=f'Killswitch: {hotkey.replace("+", "-").title()}')
            exit()

        threading.Thread(target=wait_for_callback, daemon=True).start()

class TimeOffset(Ctk.CTkFrame):
    def __init__(self, master: AdvancedOptions):
        super().__init__(master)
        self.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        self.switch = Ctk.CTkSwitch(
            self,
            text='Random Time Offset',
            variable=master.root.random_time_offset_enabled,
        )
        self.switch.place(relx=0.05, rely=0.1)

        self.label = Ctk.CTkLabel(self, text='Milliseconds')
        self.label.place(relx=0.05, rely=0.55)

        self.entry = Ctk.CTkEntry(self, width=60, textvariable=master.root.random_time_offset)
        self.entry.place(relx=0.4, rely=0.55)


class MouseOffset(Ctk.CTkFrame):
    def __init__(self, master: AdvancedOptions):
        super().__init__(master)
        self.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

        self.switch = Ctk.CTkSwitch(
            self,
            text='Random Mouse Offset',
            variable=master.root.random_mouse_offset_enabled,
        )
        self.switch.place(relx=0.05, rely=0.1)

        self.x = Ctk.CTkLabel(self, text='X:')
        self.x.place(relx=0.05, rely=0.55)

        self.x_entry = Ctk.CTkEntry(self, width=60, textvariable=master.root.random_mouse_offset_x)
        self.x_entry.place(relx=0.15, rely=0.55)

        self.y = Ctk.CTkLabel(self, text='Y:')
        self.y.place(relx=0.45, rely=0.55)

        self.y_entry = Ctk.CTkEntry(self, width=60, textvariable=master.root.random_mouse_offset_y)
        self.y_entry.place(relx=0.55, rely=0.55)


class ClickType(Ctk.CTkFrame):
    def __init__(self, master: AdvancedOptions):
        super().__init__(master)
        self.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        self.description = Ctk.CTkLabel(self, text='Click Type:')
        self.description.place(relx=0.05, rely=0.1)

        self.option_menu = Ctk.CTkOptionMenu(
            self,
            values=['Single', 'Double'],
            width=135,
            variable=master.root.click_type,
        )

        self.option_menu.place(relx=0.37, rely=0.1)

        self.hold_label = Ctk.CTkLabel(
            self, text='Hold duration (ms):'
        )
        self.hold_label.place(relx=0.05, rely=0.55)

        self.hold_entry = Ctk.CTkEntry(
            self,
            width=60,
            textvariable=master.root.hold_duration
        )
        self.hold_entry.place(relx=0.6, rely=0.55)


class RepeatOptions(Ctk.CTkFrame):
    def __init__(self, master: AdvancedOptions):
        super().__init__(master)
        self.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

        self.description = Ctk.CTkLabel(self, text='Repeat Options:')
        self.description.place(relx=0.05, rely=0.1)

        self.toggle = Ctk.CTkRadioButton(
            self,
            text='Toggle',
            variable=master.root.repeat_option,
            value='Toggle',
        )
        self.toggle.place(relx=0.05, rely=0.55)

        self.repeat = Ctk.CTkRadioButton(
            self,
            text='Repeat',
            variable=master.root.repeat_option,
            value='Repeat',
        )
        self.repeat.place(relx=0.4, rely=0.55)

        self.entry = Ctk.CTkEntry(self, width=50, textvariable=master.root.repeat_value)
        self.entry.place(relx=0.75, rely=0.53)


class KillSwitch(Ctk.CTkFrame):
    def __init__(self, master: AdvancedOptions):
        super().__init__(master)
        self.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

        self.change_killswitch_hotkey = Ctk.CTkButton(
            self,
            text='Change KillSwitch Hotkey',
            command=lambda: master.change_killswitch_hotkey(self),
        )
        self.change_killswitch_hotkey.place(relx=0.5, rely=0.15, anchor='n')

        self.killswitch_hotkey = Ctk.CTkLabel(
            self,
            text=f"{master.root.killswitch_hotkey.get().replace('+', '-').title()}"
        )
        self.killswitch_hotkey.place(relx=0.5, rely=0.6, anchor='n')


if __name__ == "__main__":
    app = App()
    app.mainloop()
