import customtkinter as ctk


def make_help_window():
    helpwindow = ctk.CTk()
    helpwindow.title("Help")

    ctk.CTkLabel(
        helpwindow, text="Shortcuts")
    helpwindow.mainloop()
