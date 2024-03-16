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


def get_output_data(filename):
    with open(filename, "r") as file:
        data = file.read()

    return data


def get_default_font():
    with open("data/default_font.json", "r") as file:
        data = json.load(file)

    return data


def write_default_font(new_font_name):
    with open("data/default_font.json", "w") as file:
        json.dump({"default_name": new_font_name}, file, indent=4)


def change_default_font():
    font_window = ctk.CTk()
    font_window.geometry("300x500")
    frame = ctk.CTkScrollableFrame(font_window)
    frame.pack(expand=True, fill="both")

    for font_name in font.families():
        button = ctk.CTkButton(frame, text=font_name, command=lambda name=font_name: write_default_font(name),
                               font=(font_name, 15))
        button.pack(pady=2)

    font_window.mainloop()


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


def change_font_selected(textbox, fontsize, font_label):
    default_font = get_default_font()["default_name"]  # Get the selected text
    # Get the start index of the selection
    start_index = textbox.index("sel.first")
    # Get the end index of the selection
    end_index = textbox.index("sel.last")

    # Configure tag for selected text
    textbox.tag_config("selected", font=(default_font, fontsize))
    textbox.tag_add("selected", start_index, end_index)

    font_label.configure(text=f"Current Font: {load_data()[
                         "name"]} || Default Ctrl + f Font: {get_default_font()["default_name"]}")
