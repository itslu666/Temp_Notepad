import customtkinter as ctk

root = ctk.CTk()
tabview = ctk.CTkTabview(root)

tabview.add("tab1")
tabview.add("tab2")
tabview.add("tab3")

print(tabview.get())

root.mainloop()
