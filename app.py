import customtkinter as Ctk
from CTkMessagebox import CTkMessagebox
import youtubedown
import imgConverter
from PIL import Image

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

        whats_new_text = Ctk.CTkLabel(self.current_frame, text="• Changed from Tkinter to CustomTkinter\n\n""• Updated UI\n\n""• Added ICO picture\n\n""• Cleaned up code\n\n""• Added new tools", justify="left" ,font=("Arial", 15))
        whats_new_text.pack(side="left", padx=(60,0), pady=(0,150))

        water = Ctk.CTkImage(light_image=Image.open('wave.png'), dark_image=Image.open('wave.png'), size=(300,200))
        water_wave = Ctk.CTkLabel(self.current_frame, text="", image=water)
        water_wave.pack(side="right", pady=(0,150))


        button = Ctk.CTkButton(self.menu_frame, text="Youtube Downloader", command=self.show_youtube)
        button.pack(pady=20, padx=10)

        button2 = Ctk.CTkButton(self.menu_frame, text="Image Converter", command=self.show_imgconverter)
        button2.pack()

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

        download_button = Ctk.CTkButton(self.current_frame, text="Download", font=("Arial", 12), command=handle_youtube_download )
        download_button.pack(pady=20)

        back_button_youtube = Ctk.CTkButton(self.current_frame, text="Back to Homepage", command=self.show_homepage, font=("Arial", 12))
        back_button_youtube.pack(pady=10)
    
    def show_imgconverter(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = Ctk.CTkFrame(self)
        self.current_frame.pack(fill="both", expand=True)

        picchanger_label = Ctk.CTkLabel(self.current_frame, text="Picture File Type Changer", font=("Arial", 16))
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


if __name__ == "__main__":
    app = App()
    app.mainloop()
