import customtkinter as ctk

# Hovedvindu
root = ctk.CTk()
root.geometry("400x300")
root.title("Hovedvindu")

# Liste over instruksjoner
steps = [
    "1. Refresh list and choose your window.",
    "2. Click 'select area' button and a window will open with a screen shot of you chosen window",
    "3. drag you mouse to select the chat that wil be translated and monitored. when your done click 'enter' to confirm or 'c' which will not confirm and close the window.",
    "4. when you have selected your area the chat wil say something like: ✅ Area selected: (999, 999, 999, 999)",
    "5. then all you need to do is click start and the app will read up every chat and translate them to Norwegian.",
    "The language that the ai can read are the following: Russain, Norwagian, Chinese traditional, Chinese simple, Dutch, French, Spanish, Japanese, English. our team is working on adding more in the future!"
]

# Funksjon for å åpne et nytt tutorial-vindu
def open_tutorial():
    tutorial_window = ctk.CTkToplevel(root)
    tutorial_window.geometry("500x400")
    tutorial_window.title("Tutorial")

    # Hovedramme for innhold
    main_frame = ctk.CTkFrame(tutorial_window)
    main_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Loop gjennom stegene og legg til tekst
    for step in steps:
        step_label = ctk.CTkLabel(main_frame, text=step, font=("Arial", 14), wraplength=480)
        step_label.pack(pady=5, padx=10, anchor="w")

    # Lukk-knapp
    close_button = ctk.CTkButton(main_frame, text="Lukk", command=tutorial_window.destroy)
    close_button.pack(pady=20)

# Knapp for å åpne tutorial-vindu
tutorial_button = ctk.CTkButton(root, text="📖 Åpne Tutorial", command=open_tutorial)
tutorial_button.pack(pady=20)

# Kjør programmet
root.mainloop()
