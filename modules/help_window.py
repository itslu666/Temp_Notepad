import customtkinter as ctk
from CTkTable import *


def make_help_window():
    helpwindow = ctk.CTk()
    helpwindow.title("Help")

    # tabs
    tabs_table = CTkTable(helpwindow, row=4, column=2)

    tabs_table.insert(0, 0, "CTRL + t")
    tabs_table.insert(0, 1, "New Tab")
    tabs_table.insert(1, 0, "CTRL + SHIFT + t")
    tabs_table.insert(1, 1, "New Named Tab")
    tabs_table.insert(2, 0, "CTRL + w")
    tabs_table.insert(2, 1, "Close Tab")
    tabs_table.insert(3, 0, "CTRL + TAB")
    tabs_table.insert(3, 1, "Switch Tab")

    tabs_table.pack(expand=True, fill="both", padx=20, pady=20)

    # file
    file_table = CTkTable(helpwindow, row=3, column=2)

    file_table.insert(0, 0, "CTRL + s")
    file_table.insert(0, 1, "Save to output directory")
    file_table.insert(1, 0, "CTRL + SHIFT + s")
    file_table.insert(1, 1, "Choose saving directory")
    file_table.insert(2, 0, "CTRL + o")
    file_table.insert(2, 1, "Open file")

    file_table.pack(expand=True, fill="both", padx=20, pady=20)

    # edit
    edit_table = CTkTable(helpwindow, row=7, column=2)

    edit_table.insert(0, 0, "CTRL + b")
    edit_table.insert(0, 1, "Make selection bold")
    edit_table.insert(1, 0, "CTRL + u")
    edit_table.insert(1, 1, "Make selection underlined")
    edit_table.insert(2, 0, "CTRL + i")
    edit_table.insert(2, 1, "Make selection italic")
    edit_table.insert(3, 0, "CTRL + q")
    edit_table.insert(3, 1, "Make selection overstriked")
    edit_table.insert(4, 0, "CTRL + +")
    edit_table.insert(4, 1, "Increase text size")
    edit_table.insert(5, 0, "CTRL + -")
    edit_table.insert(5, 1, "Decrease text size")
    edit_table.insert(6, 0, "CTRL + SHIFT + c")
    edit_table.insert(6, 1, "Make checkbox")

    edit_table.pack(expand=True, fill="both", padx=20, pady=20)

    # images
    image_table = CTkTable(helpwindow, row=4, column=2)

    image_table.insert(0, 0, "CTRL + SHIFT + i")
    image_table.insert(0, 1, "Insert image from clipboard")
    image_table.insert(1, 0, "CTRL + SHIFT + ALT + i")
    image_table.insert(1, 1, "Choose image")
    image_table.insert(2, 0, "MouseUp / MouseDown")
    image_table.insert(2, 1, "Scroll up and down")
    image_table.insert(3, 0, "SHIFT + MouseUp / MouseDown")
    image_table.insert(3, 1, "Move left and right")

    image_table.pack(expand=True, fill="both", padx=20, pady=20)
    helpwindow.mainloop()
