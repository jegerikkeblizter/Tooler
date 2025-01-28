import tkinter as tk
from tkinter import messagebox, filedialog, StringVar, OptionMenu
import imgConverter
import app
import gui


picchanger_page_frame = tk.Frame(app.root, bg='#2e2e2e')

picchanger_label = tk.Label(picchanger_page_frame, text="Picture File Type Changer", font=("Arial", 16), fg="white", bg='#2e2e2e')
picchanger_label.pack(pady=20)

selected_file = StringVar()
original_file = StringVar()  # Store the original file path

file_label = tk.Label(picchanger_page_frame, text="Select Image File:", font=("Arial", 12), fg="white", bg='#2e2e2e')
file_label.pack(pady=5)

file_button = tk.Button(picchanger_page_frame, text="Browse", command=imgConverter.select_file, font=("Arial", 10), bg="#4caf50", fg="white")
file_button.pack(pady=5)

file_path_label = tk.Label(picchanger_page_frame, textvariable=selected_file, wraplength=300, font=("Arial", 10), fg="white", bg='#2e2e2e')
file_path_label.pack(pady=5)

output_format_label = tk.Label(picchanger_page_frame, text="Select Output Format:", font=("Arial", 12), fg="white", bg='#2e2e2e')
output_format_label.pack(pady=10)

output_formats = ["jpeg", "png", "webp"]
selected_format = StringVar(value=output_formats[0])
format_menu = OptionMenu(picchanger_page_frame, selected_format, *output_formats)
format_menu.pack(pady=5)

convert_button = tk.Button(picchanger_page_frame, text="Convert", command=imgConverter.start_conversion, font=("Arial", 12, "bold"), bg="#4caf50", fg="white")
convert_button.pack(pady=20)

# Delete Original File Button (only enabled after conversion)
delete_button = tk.Button(picchanger_page_frame, text="Delete Original Image", command=imgConverter.delete_original_image, font=("Arial", 12), bg="#f44336", fg="white", state="disabled")
delete_button.pack(pady=10)

back_button_picchanger = tk.Button(picchanger_page_frame, text="Back to Homepage", command=gui.go_home, font=("Arial", 12), bg="#f44336", fg="white")
back_button_picchanger.pack(pady=10)

# Add a copyright label at the bottom
copyright_label = tk.Label(app.root, text="© 2024 Dem Som Vet", font=("Arial", 10), fg="white", bg='#2e2e2e')
copyright_label.pack(side="bottom", pady=10)