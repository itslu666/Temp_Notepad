import os
import customtkinter as ctk
from CTkMenuBar import *
from modules import ctrl_options, make_UI, file_management, help_window


def get_appearance_mode():
    with open(os.path.join("data", "appearance_mode.txt"), "r") as file:
        return file.read()


def change_appearance_mode():
    appearance_mode = get_appearance_mode()
    with open(os.path.join("data", "appearance_mode.txt"), "w") as file:
        if appearance_mode == "light":
            file.write("dark")
            ctk.set_appearance_mode("dark")
            appearance_mode = "dark"
            menu.configure(bg_color="#242424")
        else:
            file.write("light")
            ctk.set_appearance_mode("light")
            appearance_mode = "light"
            menu.configure(bg_color="white")
    file.close()


def always_on_top():
    current_state = root.attributes("-topmost")
    new_state = not current_state  # Umkehrung des aktuellen Zustands
    root.attributes("-topmost", new_state)


appearance_mode = get_appearance_mode()

ctk.set_appearance_mode(appearance_mode)
root = ctk.CTk()
root.geometry("800x500")
root.title("Temp Notepad")

# make default ui
# make menu strip
if appearance_mode == "light":
    menu_color = "white"
else:
    menu_color = "#242424"

menu = CTkMenuBar(root, bg_color=menu_color)
file_menu_file = menu.add_cascade("File")
file_menu = CustomDropdownMenu(file_menu_file, master=root)
file_menu.add_option(
    "New Tab", command=lambda event=None: ctrl_options.new_tab(event, tabview, root))
file_menu.add_option(
    "New Unnamed Tab", command=lambda event=None: ctrl_options.create_new_nameless_tab(tabview, root))
file_menu.add_separator()
file_menu.add_option(
    "Save", command=lambda: root.event_generate("<Control-s>"))
file_menu.add_option(
    "Save As", command=lambda: root.event_generate("<Control-S>"))
file_menu.add_option(
    "Open", command=lambda: root.event_generate("<Control-o>"))
file_menu.add_separator()
file_menu.add_option("Help", command=help_window.make_help_window)
file_menu.add_option("Change Appearance Mode",
                     command=lambda: change_appearance_mode())
file_menu.add_option("Always on Top", command=always_on_top)

file_menu_edit = menu.add_cascade("Edit")
file_menu_ed = CustomDropdownMenu(file_menu_edit, master=root)
file_menu_ed.add_option("Change Font", command=file_management.change_font)

tabview = ctk.CTkTabview(root)
tabview.add("new_file")
tabview.pack(expand=True, fill="both")


# make textbox and rest
make_UI.make_ui(tabview, "new_file", root)

# reset tab names
with open("data/tab_names.txt", "w") as file:
    file.write("")

# add new tab name
file_management.write_tab_name("new_file")

# ctrl t for new tab
root.bind('<Control-T>', lambda event: ctrl_options.new_tab(event, tabview, root))
root.bind('<Control-t>',
          lambda event: ctrl_options.create_new_nameless_tab(tabview, root))

# ctrl + w for delete tab
root.bind('<Control-w>', lambda event: ctrl_options.delete_tab(event, tabview))

# ctrl + tab for switching
root.bind('<Control-Tab>', lambda event: ctrl_options.switch_tab(event, tabview))
root.protocol("WM_DELETE_WINDOW", lambda: file_management.on_close(root))

root.mainloop()
