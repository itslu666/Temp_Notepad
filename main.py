import customtkinter as ctk
from modules import ctrl_options, make_UI, file_management


root = ctk.CTk()
root.geometry("800x500")
root.title("Temp Notepad")

# make default ui
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
root.bind('<Control-t>', lambda event: ctrl_options.new_tab(event, tabview, root))
root.bind('<Control-T>',
          lambda event: ctrl_options.create_new_nameless_tab(tabview, root))

# ctrl + w for delete tab
root.bind('<Control-w>', lambda event: ctrl_options.delete_tab(event, tabview))

# ctrl + tab for switching
root.bind('<Control-Tab>', lambda event: ctrl_options.switch_tab(event, tabview))

root.mainloop()
