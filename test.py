import tkinter as tk
from tkinter import ttk


def find_widgets_in_tab(tab):
    # Erhalte alle Widgets im Tab
    tab_widgets = tab.winfo_children()
    return tab_widgets


root = tk.Tk()

# TabView erstellen
tabview = ttk.Notebook(root)
tabview.pack(fill="both", expand=True)

# Tabs erstellen
tab1 = tk.Frame(tabview)
tab2 = tk.Frame(tabview)
tabview.add(tab1, text="Tab 1")
tabview.add(tab2, text="Tab 2")

# Beispiel-Widgets in den Tabs erstellen
label1 = tk.Label(tab1, text="Label in Tab 1")
label1.pack()
button1 = tk.Button(tab1, text="Button in Tab 1")
button1.pack()

label2 = tk.Label(tab2, text="Label in Tab 2")
label2.pack()
button2 = tk.Button(tab2, text="Button in Tab 2")
button2.pack()

# Alle Widgets im Tab 1 finden
widgets_in_tab1 = find_widgets_in_tab(tab1)
print("Widgets im Tab 1:", widgets_in_tab1)

# Text des Labels im Tab 1 ändern
for widget in widgets_in_tab1:
    if isinstance(widget, tk.Label):
        widget.config(text="Neuer Text im Label")

root.mainloop()
