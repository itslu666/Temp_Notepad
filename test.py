import customtkinter as tk
import json


def save_text_with_formatting():
    data = {"text": textbox.get("1.0", "end")}
    all_tags = textbox.tag_names()
    for tag in all_tags:
        ranges = textbox.tag_ranges(tag)
        tag_info = []
        for i in range(0, len(ranges), 2):
            start_index = textbox.index(ranges[i])
            end_index = textbox.index(ranges[i + 1])
            tag_info.append(
                {"start_index": start_index, "end_index": end_index})
        data[tag] = tag_info

    with open("formatted_text_info.json", "w") as file:
        json.dump(data, file, indent=4)


def restore_text_with_formatting():
    textbox.delete("1.0", "end")
    with open("formatted_text_info.json", "r") as file:
        data = json.load(file)
        text = data["text"]
        textbox.delete("1.0", "end")
        textbox.insert("1.0", text)

        for tag, tag_info in data.items():
            if tag != "text":
                for info in tag_info:
                    start_index = info["start_index"]
                    end_index = info["end_index"]
                    textbox.tag_add(tag, start_index, end_index)


root = tk.CTk()

textbox = tk.CTkTextbox(root)
textbox.pack()

# Beispiel-Text und Formatierung hinzufügen
textbox.insert("1.0", "das ist ein Beispieltext")
textbox.tag_add("bold", "1.0", "1.5")  # Füge Formatierung hinzu (fett)
textbox.tag_add("italic", "1.5", "1.9")  # Füge Formatierung hinzu (kursiv)
# Konfiguriere Formatierung (fett)
textbox.tag_config("bold", font=("Arial", 12, "bold"))
textbox.tag_config("italic", font=("Arial", 12, "italic"))

# Speichern-Button hinzufügen
save_button = tk.CTkButton(root, text="Speichern",
                           command=save_text_with_formatting)
save_button.pack()

# Wiederherstellen-Button hinzufügen
restore_button = tk.CTkButton(
    root, text="Wiederherstellen", command=restore_text_with_formatting)
restore_button.pack()

root.mainloop()
