import json
import customtkinter as ctk
from tkinter import font


def load_data():
    with open("data/font.json", "r") as file:
        data = json.load(file)

    return data


def write_tab_name(tab_name):
    if tab_name not in get_tab_names():
        with open("data/tab_names.txt", "a") as file:
            file.write(tab_name + "\n")


def get_tab_names():
    with open("data/tab_names.txt", "r") as file:
        tab_names = file.readlines()

    return tab_names


def delete_tab_name(tab_name):
    tab_names = get_tab_names()
    if f"{tab_name}\n" in tab_names:
        # Entfernen des gewünschten Namens aus der Liste
        tab_names.remove(f"{tab_name}\n")

        # Schreiben der aktualisierten Liste zurück in die Datei
        with open("data/tab_names.txt", "w") as file:
            for name in tab_names:
                file.write(name)


def change_font():
    font_window = ctk.CTk()
    font_window.geometry("300x500")
    frame = ctk.CTkScrollableFrame(font_window)
    frame.pack(expand=True, fill="both")

    ctk.CTkButton(frame, text="Default (Consolas)", command=lambda: switch_font("Consolas"),
                  font=("Consolas", 15)).pack(pady=2)

    for font_name in font.families():
        button = ctk.CTkButton(frame, text=font_name, command=lambda name=font_name: switch_font(name),
                               font=(font_name, 15))
        button.pack(pady=2)

    font_window.mainloop()


def switch_font(font_name):
    with open("data/font.json", "w") as file:
        json.dump({"name": font_name}, file, indent=4)
