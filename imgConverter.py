import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image
import os
import imgGui

def convert_image(input_file, output_format):
    try:
        with Image.open(input_file) as img:
            # Ensure RGB mode for formats like JPG
            if output_format.lower() in ["jpg", "jpeg"] and img.mode != "RGB":
                img = img.convert("RGB")

            # Save the converted file in the same directory as the original
            output_dir = os.path.dirname(input_file)
            base_name = os.path.splitext(os.path.basename(input_file))[0]
            output_file = os.path.join(output_dir, f"{base_name}.{output_format}")

            # Use the correct format name for JPEG
            img.save(output_file, format="JPEG" if output_format.lower() in ["jpg", "jpeg"] else output_format.upper())

            return output_file, input_file  # Return both converted and original file paths
    except Exception as e:
        return None, str(e)


# Function to select the file
def select_file():
    file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image Files", "*.jpeg *.png *.webp"), ("All Files", "*.*")]
    )
    if file_path:
        imgGui.selected_file.set(file_path)
        imgGui.delete_button.config(state="disabled")  # Disable delete button initially


# Function to start the image conversion process
def start_conversion():
    input_file = imgGui.selected_file.get()
    output_format = imgGui.selected_format.get()

    if not input_file:
        messagebox.showerror("Error", "Please select an image file.")
        return

    if not output_format:
        messagebox.showerror("Error", "Please select an output format.")
        return

    # Perform the conversion
    converted_file, error = convert_image(input_file, output_format)

    if converted_file:
        messagebox.showinfo("Conversion Result", f"Image converted and saved as: {converted_file}")
        # Enable the delete button after successful conversion
        imgGui.delete_button.config(state="normal")
        imgGui.original_file.set(input_file)  # Store original file path
    else:
        messagebox.showerror("Error", f"An error occurred: {error}")


# Function to delete the original image file
def delete_original_image():
    original_file_path = imgGui.original_file.get()
    
    if not original_file_path:
        messagebox.showwarning("Warning", "No original image to delete.")
        return

    try:
        os.remove(original_file_path)
        messagebox.showinfo("Success", f"The original image file {original_file_path} has been deleted.")
        imgGui.original_file.set("")  # Clear the original file path after deletion
        imgGui.delete_button.config(state="disabled")  # Disable the delete button
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while deleting the file: {e}")