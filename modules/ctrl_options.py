import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
from . import file_management, make_UI
from PIL import Image, ImageGrab
import time


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

    # update textbox & set vars
    maintextbox.configure(font=(file_management.load_data()["name"], new_size))
    fontSize_var.set(new_size)
    fontSize_perc_var.set(new_size_perc)


def decrease_fontsize(event, maintextbox, fontSize_var, fontSize_perc_var):
    # get size & percent
    new_size = fontSize_var.get() - 2
    new_size_perc = fontSize_perc_var.get() - 10

    # update textbox & set vars
    maintextbox.configure(font=(file_management.load_data()["name"], new_size))
    fontSize_var.set(new_size)
    fontSize_perc_var.set(new_size_perc)


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


def save(textbox, tabview, root):
    """ for widget in tabview.tab(tabview.get()).winfo_children():
        if isinstance(widget, ctk.CTkLabel) and isinstance(widget._image, ctk.CTkImage):
            print(widget._image._light_image) """

    with open(f"output/{tabview.get()}.notepad", "w") as file:
        file.write(textbox.get("1.0", "end-1c"))

    root.title("Temp Notepad")


def save_as(textbox, root, tabview):
    filename = filedialog.asksaveasfilename(
        defaultextension=".txt", initialfile=tabview.get(), filetypes=[("Txt Files", "*.txt")])

    if filename:
        with open(filename, "w") as file:
            file.write(textbox.get("1.0", "end-1c"))

        root.title("Temp Notepad")


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
    textbox.tag_config("italic", font=(font_name, fontsize, "italic"))
    # Apply italic tag to selected text
    textbox.tag_add("italic", start_index, end_index)

    return "break"


def choose_img():
    ...


def paste_img_clipboard(event, frame, root):
    # get img from clipboard
    image = ImageGrab.grabclipboard()
    timestamp = int(time.time())

    if image:
        # save img in temp folder
        image.save(f"data/temp_img/temp{timestamp}.png")
        # make Image obj for ctkimage
        img_ctkimg = Image.open(f"data/temp_img/temp{timestamp}.png")

        # make label
        img_label = ctk.CTkLabel(frame,
                                 image=ctk.CTkImage(img_ctkimg, size=(img_ctkimg.width / 2, img_ctkimg.height / 2)), text="")
        img_label.pack(side="top", anchor="w", padx=(6, 0))
    else:
        print("no img")
