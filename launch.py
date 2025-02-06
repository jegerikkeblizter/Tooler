import sys
import os
import tkinter as tk
import threading
import subprocess
import time
from PIL import Image, ImageDraw, ImageTk
import psutil  # For å sjekke prosesser
import pygetwindow as gw  # For å sjekke aktive vinduer

class SplashScreen(tk.Tk):
    def __init__(self):
        super().__init__()

        # Gjør vinduet usynlig (ingen ramme)
        self.overrideredirect(True)
        self.wm_attributes("-transparentcolor", "black")
        self.attributes("-topmost", True)  # Splash skal være øverst inntil tooler.exe åpner GUI

        # Finn skjermstørrelse
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Hent riktig filbane for tooler.png
        image_path = self.get_resource_path("tooler.png")
        self.logo_tk = self.create_circular_image(image_path, (300, 300))
        
        # Opprett og plasser bildet
        self.label = tk.Label(self, image=self.logo_tk, bg="black", borderwidth=0, highlightthickness=0)
        self.label.pack()

        # Sentrer vinduet på skjermen
        window_width, window_height = 300, 300
        x_pos = (screen_width - window_width) // 2
        y_pos = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

        # Fade-in animasjon
        self.fade_in()

        # Start tooler.exe
        self.start_app()

    def get_resource_path(self, relative_path):
        """Returnerer riktig filbane uansett om programmet kjører som .py eller .exe"""
        if getattr(sys, 'frozen', False):  # Hvis vi kjører som en PyInstaller .exe
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def create_circular_image(self, image_path, size):
        """Laster et bilde, gjør det rundt, og returnerer en Tkinter-kompatibel versjon"""
        img = Image.open(image_path).convert("RGBA")
        img = img.resize(size, Image.LANCZOS)

        # Lag en sirkulær maske
        mask = Image.new("L", size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + size, fill=255)

        # Påfør masken
        img.putalpha(mask)

        return ImageTk.PhotoImage(img)

    def fade_in(self):
        """Glatt fade-in animasjon"""
        for i in range(1, 11):
            self.attributes("-alpha", i / 10)
            self.update()
            time.sleep(0.05)

    def fade_out(self):
        """Glatt fade-out animasjon før lukking"""
        for i in range(10, -1, -1):
            self.attributes("-alpha", i / 10)
            self.update()
            time.sleep(0.05)
        self.destroy()

    def start_app(self):
        """Starter tooler.exe og venter til GUI-et er oppe før splash-vinduet lukkes"""
        def run_app():
            try:
                # Finn riktig filbane for tooler.exe
                if getattr(sys, 'frozen', False):
                    app_path = os.path.join(sys._MEIPASS, "tooler.exe")  # tooler.exe må være inne i pakken
                else:
                    app_path = os.path.abspath("tooler.exe")  # Hvis den kjører i en mappe

                # Start tooler.exe uten terminalvindu
                process = subprocess.Popen([app_path], creationflags=subprocess.CREATE_NO_WINDOW)

                # Vent til GUI faktisk er synlig
                self.wait_for_app_gui()

                # Fade ut splash-skjermen når GUI er oppe
                self.fade_out()

            except Exception as e:
                print(f"Kunne ikke starte tooler.exe: {e}")
                self.fade_out()  # Lukker splash-vinduet hvis det feiler

        threading.Thread(target=run_app, daemon=True).start()

    def wait_for_app_gui(self):
        """Sjekker når tooler.exe sitt GUI er oppe"""
        print("Venter på at tooler.exe GUI skal åpne seg...")
        time.sleep(3)  # Gi app tid til å starte

        while True:
            # Sjekk om tooler.exe kjører
            running = any("tooler.exe" in proc.name().lower() for proc in psutil.process_iter(attrs=['name']))

            if not running:
                print("Tooler.exe feilet eller lukket seg. Lukker splash...")
                self.fade_out()
                return

            # Sjekk om tooler.exe har et synlig vindu
            windows = gw.getWindowsWithTitle("Tooler")  # ⚠️ Endre "Tooler" til riktig vindustittel fra tooler.py
            for win in windows:
                if win.isActive and not win.isMinimized and win.width > 100 and win.height > 100:
                    print("Tooler GUI er synlig, lukker splash...")
                    return

            time.sleep(1)  # Sjekker hvert sekund

# Kjør splash-skjermen
if __name__ == "__main__":
    splash = SplashScreen()
    splash.mainloop()
