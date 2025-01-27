import tkinter as tk

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    position_top = int(screen_height / 2 - height / 2)
    position_right = int(screen_width / 2 - width / 2)
    window.geometry(f'{width}x{height}+{position_right}+{position_top}')

root = tk.Tk()
root.title("Dem som vet")
root.geometry("570x500")

center_window(root, 570, 500)

root.config(bg='#2e2e2e')

homepage_frame = tk.Frame(root, bg='#2e2e2e')
homepage_frame.pack()

root.mainloop()