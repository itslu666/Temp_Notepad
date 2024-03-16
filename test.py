import tkinter as tk


def change_font():
    selected_text = text_box.selection_get()  # Get the selected text
    # Get the start index of the selection
    start_index = text_box.index("sel.first")
    # Get the end index of the selection
    end_index = text_box.index("sel.last")

    # Add a tag to the selected text
    text_box.tag_add("selected", start_index, end_index)
    # Change font for the selected text
    text_box.tag_config("selected", font=("Arial", 12))


root = tk.Tk()

text_box = tk.Text(root)
text_box.pack()

text_box.insert("1.0", "This is some sample text.")

change_font_button = tk.Button(root, text="Change Font", command=change_font)
change_font_button.pack()

root.mainloop()
