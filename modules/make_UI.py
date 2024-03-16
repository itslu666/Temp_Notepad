import customtkinter as ctk
from modules import file_management, ctrl_options, word_info


def make_ui(tabview, tabview_name, root):

    # set fontsize and %
    fontSize_var = ctk.IntVar(value=16)
    fontSize_perc_var = ctk.IntVar(value=100)
    font = (file_management.load_data()["name"], fontSize_var.get())

    textbox = ctk.CTkTextbox(tabview.tab(tabview_name), font=font)
    textbox.focus_set()
    textbox.pack(expand=True, fill="both")

    # make label to display infos
    infolabel = ctk.CTkLabel(
        tabview.tab(tabview_name), text=f"Row 1, Column 1 || Words 0 || {fontSize_perc_var.get()}%")
    infolabel.pack(side="bottom", anchor="e", padx=5)

    # keybinds ---------------------------------------------------
    # update info
    textbox.bind("<KeyRelease>", lambda event, il=infolabel, fspv=fontSize_perc_var, mt=textbox: word_info.update_rows_label(
        il, fspv, mt))

    textbox.bind("<KeyPress>", lambda event: root.title("Temp Notepad*"))

    # backspace and delete word
    textbox.bind('<Control-BackSpace>', lambda event,
                 : ctrl_options.do_backspace(event))
    textbox.bind('<Control-Delete>', lambda event,
                 : ctrl_options.do_delete(event))

    # change fontsize
    root.bind('<Control-plus>', lambda event,
              mt=textbox: ctrl_options.increase_fontsize(event, mt, fontSize_var, fontSize_perc_var))
    root.bind('<Control-minus>', lambda event,
              mt=textbox: ctrl_options.decrease_fontsize(event, mt, fontSize_var, fontSize_perc_var))

    # ctrl + s for save
    root.bind('<Control-s>',
              lambda event: ctrl_options.save(textbox, tabview, root))
    root.bind('<Control-S>',
              lambda event: ctrl_options.save_as(textbox, root, tabview))
