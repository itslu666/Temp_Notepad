import customtkinter as ctk
from modules import file_management, ctrl_options, word_info, ctk_xyframe


def make_ui(tabview, tabview_name, root):

    # set fontsize and %
    fontSize_var = ctk.IntVar(value=16)
    fontSize_perc_var = ctk.IntVar(value=100)
    font = (file_management.load_data()["name"], fontSize_var.get())

    textbox = ctk.CTkTextbox(tabview.tab(tabview_name), font=font)
    textbox.focus_set()
    textbox.pack(expand=True, fill="both", side="left")

    # make label to display infos
    infolabel = ctk.CTkLabel(
        tabview.tab(tabview_name), text=f"Row 1, Column 1 || Words 0 || {fontSize_perc_var.get()}%")
    infolabel.pack(side="bottom", anchor="e", padx=5)

    img_frame = ctk_xyframe.CTkXYFrame(
        tabview.tab(tabview_name), width=300)
    img_frame.pack(expand=True, fill="both", side="bottom", padx=10)

    # keybinds ---------------------------------------------------
    # update info
    textbox.bind("<KeyRelease>", lambda event, il=infolabel, fspv=fontSize_perc_var, mt=textbox: word_info.update_rows_label(
        il, fspv, mt))

    textbox.bind("<KeyPress>", lambda event: root.title("Temp Notepad*"))

    # check checkboxes
    textbox.bind("<ButtonRelease-1>",
                 lambda e: ctrl_options.check_brackets(e, textbox))

    # backspace and delete word
    textbox.bind('<Control-BackSpace>', lambda event,
                 : ctrl_options.do_backspace(event))
    textbox.bind('<Control-Delete>', lambda event,
                 : ctrl_options.do_delete(event))

    # change fontsize
    textbox.bind('<Control-plus>', lambda event,
                 mt=textbox: ctrl_options.increase_fontsize(event, mt, fontSize_var, fontSize_perc_var))
    textbox.bind('<Control-minus>', lambda event,
                 mt=textbox: ctrl_options.decrease_fontsize(event, mt, fontSize_var, fontSize_perc_var))

    # ctrl + s for save
    root.bind('<Control-s>',
              lambda event: file_management.save_file(textbox, tabview, root))
    root.bind('<Control-S>',
              lambda event: file_management.save_file_as(textbox, root))

    root.bind('<Control-o>',
              lambda event: file_management.open_file(tabview, root))

    # bind to put []
    textbox.bind(
        '<Control-C>', lambda event: ctrl_options.make_checkbox(event))

    # bin to make selection bold/underline/italic
    textbox.bind(
        "<Control-b>", lambda event: ctrl_options.make_bold(textbox, fontSize_var.get()))
    textbox.bind(
        "<Control-u>", lambda event: ctrl_options.make_underline(textbox))
    textbox.bind(
        "<Control-i>", lambda event: ctrl_options.make_italic(textbox, fontSize_var.get()))
    textbox.bind(
        "<Control-q>", lambda event: ctrl_options.make_overstriked(textbox))

    root.bind("<Control-I>",
              lambda event: ctrl_options.paste_img_clipboard(event, img_frame, root))
    root.bind("<Control-Alt-I>",
              lambda event: ctrl_options.choose_img(event, img_frame, root))
