import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
from . import file_management, make_UI
from PIL import Image, ImageGrab
import time
import os


def do_backspace(event):
    textbox = event.widget
    cursor_index = textbox.index(tk.INSERT)
    start_index = textbox.search(
        r'\s', f'{cursor_index} wordstart', backwards=True, regexp=True)
    if start_index:
        start_index = textbox.index(f"{start_index}+1c")
        textbox.delete(start_index, tk.INSERT)


def do_delete(event):
    textbox = event.widget
    cursor_index = textbox.index(tk.INSERT)
    end_index = textbox.search(r'\s', f'{cursor_index} wordend', regexp=True)
    if end_index:
        textbox.delete(cursor_index, end_index)


def increase_fontsize(event, maintextbox, fontSize_var, fontSize_perc_var):
    # get size & percent
    new_size = fontSize_var.get() + 2
    new_size_perc = fontSize_perc_var.get() + 10
    font_name = file_management.load_data()["name"]

    # update textbox & set vars
    maintextbox.configure(font=(font_name, new_size))
    fontSize_var.set(new_size)
    fontSize_perc_var.set(new_size_perc)

    # configure tags to update bold and italic text (otherwise no size change)
    maintextbox.tag_config("bold", font=(font_name, new_size, "bold"))
    maintextbox.tag_config("italic", font=(
        font_name, int(new_size/1.5), "italic"))


def decrease_fontsize(event, maintextbox, fontSize_var, fontSize_perc_var):
    # get size & percent
    new_size = fontSize_var.get() - 2
    new_size_perc = fontSize_perc_var.get() - 10
    font_name = file_management.load_data()["name"]

    # update textbox & set vars
    maintextbox.configure(font=(font_name, new_size))
    fontSize_var.set(new_size)
    fontSize_perc_var.set(new_size_perc)

    # configure tags to update bold and italic text (otherwise no size change)
    maintextbox.tag_config("bold", font=(font_name, new_size, "bold"))
    maintextbox.tag_config("italic", font=(
        font_name, int(new_size/1.5), "italic"))


def new_tab(event, tabview, root):
    # make new window for naming the tab
    tabview_name_window = ctk.CTk()
    tabview_name_window.title("Choose Tab Name")

    tabname_entry = ctk.CTkEntry(
        tabview_name_window, placeholder_text="Enter Tab Name", font=("Consolas", 15), width=500)
    tabname_entry.pack(padx=20, pady=5)

    def create_new_tab(*args):
        # get new tabname by entry or generated
        new_tab_name = get_name(tabname_entry.get())

        # add new tab to tabview
        tabview.add(new_tab_name)
        # make ui for new tab
        make_UI.make_ui(tabview, new_tab_name, root)
        # select new tab
        tabview.set(new_tab_name)
        # destroy this window
        tabview_name_window.destroy()

    tabview_name_window.bind("<Return>", create_new_tab)

    enter_button = ctk.CTkButton(
        tabview_name_window, text="New Tab", command=create_new_tab)
    enter_button.pack(pady=5)

    tabview_name_window.mainloop()


def create_new_nameless_tab(tabview, root):
    # get new tabname by entry or generated
    new_tab_name = get_name("")

    # add new tab to tabview
    tabview.add(new_tab_name)
    # make ui for new tab
    make_UI.make_ui(tabview, new_tab_name, root)
    # select new tab
    tabview.set(new_tab_name)


def get_name(entered_name):
    # if the entry input isnt empty, get name from entry
    if entered_name != "":
        name = entered_name
    else:
        # get all tabnames from txt
        tab_names = file_management.get_tab_names()

        # while the name is in tab_names, ++ num till fit
        num = 1
        while f"new_file_{num}\n" in tab_names:
            num += 1

        name = f"new_file_{num}"

    # write new name in txt
    file_management.write_tab_name(name)
    return name


def delete_tab(event, tabview):
    # get selected tab & delete
    current_tab = tabview.get()
    tabview.delete(current_tab)

    # remove tab from txt
    file_management.delete_tab_name(current_tab)

    # this doesnt work / bug
    # next_tab = file_management.get_tab_names()[-1].replace("\n", "")
    # tabview.set(next_tab)


def switch_tab(event, tabview):
    current_tab = tabview.get()
    tab_names = file_management.get_tab_names()

    # Finden Sie den Index des aktuellen Tabs in der Liste der Tab-Namen
    current_tab_index = tab_names.index(f"{current_tab}\n")

    # Berechnen Sie den Index des nächsten Tabs
    next_tab_index = (current_tab_index + 1) % len(tab_names)

    # Holen Sie den Namen des nächsten Tabs
    next_tab = tab_names[next_tab_index]

    # Setzen Sie den nächsten Tab
    tabview.set(next_tab.replace("\n", ""))


def make_checkbox(event):
    event.widget.insert(event.widget.index(tk.INSERT), "[] ")


def make_bold(textbox, fontsize):
    font_name = file_management.load_data()["name"]  # Get fontname
    # Get the start index of the selection
    start_index = textbox.index("sel.first")
    # Get the end index of the selection
    end_index = textbox.index("sel.last")

    # Configure tag for bold text
    textbox.tag_config("bold", font=(font_name, fontsize, "bold"))
    # Apply bold tag to selected text
    textbox.tag_add("bold", start_index, end_index)


def make_underline(textbox):
    # Get the start index of the selection
    start_index = textbox.index("sel.first")
    # Get the end index of the selection
    end_index = textbox.index("sel.last")

    # Configure tag for underlined text
    textbox.tag_config("underline", underline=True)
    # Apply underline tag to selected text
    textbox.tag_add("underline", start_index, end_index)


def make_italic(textbox, fontsize):
    font_name = file_management.load_data()["name"]  # Get fontname
    # Get the start index of the selection
    start_index = textbox.index("sel.first")
    # Get the end index of the selection
    end_index = textbox.index("sel.last")

    # Configure tag for italic text
    textbox.tag_config("italic", font=(font_name, int(fontsize/1.5), "italic"))
    # Apply italic tag to selected text
    textbox.tag_add("italic", start_index, end_index)

    return "break"


def make_overstriked(textbox):
    # Get the start index of the selection
    start_index = textbox.index("sel.first")
    # Get the end index of the selection
    end_index = textbox.index("sel.last")

    # Configure tag for bold text
    textbox.tag_config("overstrike", overstrike=True)
    # Apply bold tag to selected text
    textbox.tag_add("overstrike", start_index, end_index)


def choose_img(event, frame, root):
    def delete_img():
        del_button.pack_forget()
        img_label.pack_forget()
        if os.path.exists(os.path.join("data", "temp_img", f"temp{timestamp}.png")):
            os.remove(os.path.join("data", "temp_img", f"temp{timestamp}.png"))
        else:
            pass

    # Öffne einen Dateidialog, um das Bild auszuwählen
    file_path = filedialog.askopenfilename(filetypes=(
        ("png files", "*.png"), ("jpg files", "*.jpg")))
    if file_path:
        # Öffne das ausgewählte Bild und speichere es im temporären Ordner
        timestamp = int(time.time())
        img = Image.open(file_path)
        img.save(os.path.join("data", "temp_img", f"temp{timestamp}.png"))

        # Erstelle das Image-Label und den Löschen-Button
        img_ctkimg = Image.open(os.path.join(
            "data", "temp_img", f"temp{timestamp}.png"))
        img_label = ctk.CTkLabel(frame, text="", image=ctk.CTkImage(
            img_ctkimg, size=(img_ctkimg.width / 2, img_ctkimg.height / 2)))
        img_label.pack(side="top", anchor="w")

        del_button = ctk.CTkButton(
            frame, text="Delete Image", command=delete_img)
        del_button.pack(pady=(0, 10), fill="x")


def paste_img_clipboard(event, frame, root):
    # del img function
    def delete_img():
        del_button.pack_forget()
        img_label.pack_forget()
        if os.path.exists(os.path.join("data", "temp_img", f"temp{timestamp}.png")):
            os.remove(os.path.join("data", "temp_img", f"temp{timestamp}.png"))
        else:
            pass

    # get img from clipboard
    image = ImageGrab.grabclipboard()
    timestamp = int(time.time())

    if image:
        # save img in temp folder
        image.save(os.path.join("data", "temp_img", f"temp{timestamp}.png"))
        # make Image obj for ctkimage
        img_ctkimg = Image.open(os.path.join(
            "data", "temp_img", f"temp{timestamp}.png"))

        # calc img size
        width = img_ctkimg.width
        height = img_ctkimg.height

        if width > 400:
            width = width / 2
            height = height / 2

        # make label
        img_label = ctk.CTkLabel(frame,
                                 image=ctk.CTkImage(img_ctkimg, size=(
                                     width, height)), text="")
        img_label.pack(side="top", anchor="w")

        # make delete button
        del_button = ctk.CTkButton(
            frame, text="Delete Image", width=width, command=delete_img)
        del_button.pack(pady=(0, 10), fill="x")
    else:
        print("no img")


def check_brackets(e, textbox):
    current_index = textbox.index(tk.INSERT)
    prev_index = f"{current_index} - 1 chars"
    next_index = f"{current_index} + 1 chars"

    pre_char = textbox.get(prev_index, current_index)
    next_char = textbox.get(current_index, next_index)

    line_start_index = f"{current_index} linestart"
    line_end_index = f"{current_index} lineend"

    if pre_char == "[" and next_char == "]":
        textbox.insert(tk.INSERT, "x")
        if not textbox.tag_ranges("overstrike"):
            textbox.tag_config("overstrike", overstrike=True)
        textbox.tag_add("overstrike", line_start_index, line_end_index)

    elif pre_char == "x" and next_char == "]":
        textbox.delete(prev_index, current_index)
        textbox.tag_remove("overstrike", line_start_index, line_end_index)

    elif pre_char == "[" and next_char == "x":
        textbox.delete(current_index, next_index)
        textbox.tag_remove("overstrike", line_start_index, line_end_index)
