import os
from PIL import Image

def convert_image(input_file, output_format):
    try:
        with Image.open(input_file) as img:
            if output_format.lower() in ["jpg", "jpeg"] and img.mode != "RGB":
                img = img.convert("RGB")

            output_dir = os.path.dirname(input_file)
            base_name = os.path.splitext(os.path.basename(input_file))[0]
            output_file = os.path.join(output_dir, f"{base_name}.{output_format}")

            img.save(output_file, format="JPEG" if output_format.lower() in ["jpg", "jpeg"] else output_format.upper())

            return output_file, None  # Successfully converted, no error
    except Exception as e:
        return None, str(e)  # Return error message if conversion fails

def delete_original_image(file_path):
    try:
        os.remove(file_path)
        return True, f"The original image file {file_path} has been deleted."
    except Exception as e:
        return False, f"An error occurred while deleting the file: {e}"
