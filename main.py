import customtkinter as ctk
from CTkMenuBar import *
from modules import ctrl_options, make_UI, file_management, help_window


root = ctk.CTk()
root.geometry("800x500")
root.title("Temp Notepad")

# make default ui
# make menu strip
menu = CTkMenuBar(root, bg_color="#242424")
file_menu_file = menu.add_cascade("File")
file_menu = CustomDropdownMenu(file_menu_file, master=root)
file_menu.add_option(
    "New Tab", command=lambda event=None: ctrl_options.new_tab(event, tabview, root))
file_menu.add_option(
    "New Unnamed Tab", command=lambda event=None: ctrl_options.create_new_nameless_tab(tabview, root))
file_menu.add_separator()
file_menu.add_option("Help", command=help_window.make_help_window)

file_menu_edit = menu.add_cascade("Edit")
file_menu_ed = CustomDropdownMenu(file_menu_edit, master=root)
file_menu_ed.add_option("Change Font", command=file_management.change_font)
file_menu_ed.add_option("Change Default Font",
                        command=file_management.change_default_font)

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

root.mainloop()
