import customtkinter as Ctk
from CTkMessagebox import CTkMessagebox
import youtubedown
import imgConverter
import videoConverter
import speedtest
from PIL import Image
import time
import threading
import subprocess

class App(Ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Tooler")
        self.geometry("800x500")
        self.wm_iconbitmap("tooler.ico")

        self.current_frame = None
        self.menu_frame = None
        self.show_homepage()


    def show_homepage(self):
        if self.current_frame or self.menu_frame:
            self.current_frame.destroy()
            self.menu_frame.destroy()

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

        water = Ctk.CTkImage(light_image=Image.open('wave.png'), dark_image=Image.open('wave.png'), size=(300,200))
        water_wave = Ctk.CTkLabel(self.current_frame, text="", image=water)
        water_wave.pack(side="right", pady=(0,150))


        button = Ctk.CTkButton(self.menu_frame, text="Youtube Downloader", command=self.show_youtube)
        button.pack(pady=20, padx=10)

        button2 = Ctk.CTkButton(self.menu_frame, text="Image Converter", command=self.show_imgconverter)
        button2.pack()

        button3 = Ctk.CTkButton(self.menu_frame, text="Speed Test", command=self.show_speedtest)
        button3.pack(pady=20)

        button4 = Ctk.CTkButton(self.menu_frame, text="Video Converter", command=self.show_video_converter)
        button4.pack()

        button5 = Ctk.CTkButton(self.menu_frame, text="Mp4 to Gif", command=self.show_gif_converter)
        button5.pack(pady=20)

    def show_youtube(self):
        if self.current_frame:
            self.current_frame.destroy()

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

        back_button_youtube = Ctk.CTkButton(self.current_frame, text="Back to Homepage", command=self.show_homepage, font=("Arial", 12))
        back_button_youtube.pack(pady=10)
    
    def show_imgconverter(self):
        if self.current_frame:
            self.current_frame.destroy()

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

        back_button_picchanger = Ctk.CTkButton(self.current_frame, text="Back to Homepage", command=self.show_homepage, font=("Arial", 12))
        back_button_picchanger.pack(pady=10)

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
            
        self.current_frame = Ctk.CTkFrame(self)
        self.current_frame.pack(fill="both", expand=True)
            
        file_var = Ctk.StringVar()
        format_var = Ctk.StringVar(value="mp4")
            
        video_label = Ctk.CTkLabel(self.current_frame, text="Video Converter", font=("Arial",20,"bold"))
        video_label.pack(pady=(10,0))
            
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

    def show_gif_converter(self):
        if self.current_frame:
            self.current_frame.destroy()

        


if __name__ == "__main__":
    app = App()
    app.mainloop()
