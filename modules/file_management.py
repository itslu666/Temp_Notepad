import json
import customtkinter as ctk
from tkinter import font, filedialog
import os
from . import make_UI


def load_data():
    with open(os.path.join("data", "font.json"), "r") as file:
        data = json.load(file)

    return data


def write_tab_name(tab_name):
    if tab_name not in get_tab_names():
        with open(os.path.join("data", "tab_names.txt"), "a") as file:
            file.write(tab_name + "\n")


def get_tab_names():
    with open(os.path.join("data", "tab_names.txt"), "r") as file:
        tab_names = file.readlines()

    return tab_names


def delete_tab_name(tab_name):
    tab_names = get_tab_names()
    if f"{tab_name}\n" in tab_names:
        # Entfernen des gewünschten Namens aus der Liste
        tab_names.remove(f"{tab_name}\n")

        # Schreiben der aktualisierten Liste zurück in die Datei
        with open(os.path.join("data", "tab_names.txt"), "w") as file:
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
    with open(os.path.join("data", "font.json"), "w") as file:
        json.dump({"name": font_name}, file, indent=4)


def on_close(root):
    for filename in os.listdir(os.path.join("data", "temp_img")):
        os.remove(os.path.join("data", "temp_img", filename))

    root.destroy()


def save_textbox(textbox):
    data = {"text": textbox.get("1.0", "end")}
    all_tags = textbox.tag_names()
    for tag in all_tags:
        ranges = textbox.tag_ranges(tag)
        tag_info = []
        for i in range(0, len(ranges), 2):
            start_index = textbox.index(ranges[i])
            end_index = textbox.index(ranges[i + 1])
            font = textbox.tag_cget(tag, "font")
            if "underline" in tag:
                tag_info.append(
                    {"start_index": start_index, "end_index": end_index, "underline": True, "font": font})
            elif "overstrike" in tag:
                tag_info.append(
                    {"start_index": start_index, "end_index": end_index, "overstrike": True, "font": font})
            else:
                tag_info.append({"start_index": start_index,
                                "end_index": end_index, "font": font})
        data[tag] = tag_info

    return data


def save_file(textbox, tabview, root):
    data = save_textbox(textbox)

    with open(os.path.join("output", f"{tabview.get()}.notepad"), "w") as file:
        json.dump(data, file, indent=4)

    root.title("Temp Notepad")


def save_file_as(textbox, root, tabview):
    data = save_textbox(textbox)

    filepath = filedialog.asksaveasfilename(initialfile=tabview.get(), defaultextension=".notepad", filetypes=[
                                            ("Notepad Files", "*.notepad*"), ("Json Files", "*.json")])

    if filepath:
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)

        root.title("Temp Notepad")


def choose_file(tabview, root):
    filepath = filedialog.askopenfilename(
        filetypes=[("Notepad Files", "*.notepad"), ("Json Files", "*.json")])
    print(filepath)
    # get filename
    filename = filepath.split("/")[-1].split(".")[0]

    open_file(tabview, root, filename, filepath)


def open_file(tabview, root, filename, filepath):
    # only god knows but I'll try to explain
    # get filepath

    print(filename)

    # get all existing tabs
    tabs = get_tab_names()

    # if tab doesnt exist yet
    if f"{filename}\n" not in tabs:
        # add new tab with filename
        tabview.add(filename)
        # set tab
        tabview.set(filename)
        # update tab file
        write_tab_name(filename)
        # make ui for new tab
        make_UI.make_ui(tabview, filename, root)
    else:
        # if tab exists, show tab
        tabview.set(filename)

    # get the textbox from current tab (for every widget, check if its the textbox)
    for key, widget in tabview.tab(filename).children.items():
        if isinstance(widget, ctk.CTkTextbox):
            textbox = widget
            break

    # delete everything from textbox
    textbox.delete("1.0", "end")
    # open selected file
    with open(f"{filepath}", "r") as file:
        # load data
        data = json.load(file)
        # get text
        text = data["text"]
        # insert text
        textbox.insert("1.0", text)

        # add saved formatting to the text
        for tag, tag_info in data.items():
            if tag != "text":
                for info in tag_info:
                    start_index = info["start_index"]
                    end_index = info["end_index"]
                    font = info.get("font", None)  # Get font info if available
                    textbox.tag_add(tag, start_index, end_index)
                    if "underline" in tag:
                        textbox.tag_config(tag, underline=True)
                    elif "overstrike" in tag:
                        textbox.tag_config(tag, overstrike=True)
                    if font:
                        textbox.tag_config(tag, font=font)
