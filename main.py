import customtkinter
from tkinter import PhotoImage
from faker import Faker
from collections import OrderedDict

# background GUI
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# main app
root = customtkinter.CTk()
ico_path = "icon_gene.ico"
icon = PhotoImage(file=ico_path)
root.title("Generator")
root.geometry("700x500")
root.tk.call('wm', 'iconphoto', root._w, icon)


# a
def Gene():
    num = int(text.get())
    fake = Faker()
    entry1.delete(1.0, customtkinter.END)

    for _ in range(num):
        name = fake.name()
        entry1.insert(customtkinter.END, name + "\n")


# Button
frame = customtkinter.CTkFrame(master=root)
label = customtkinter.CTkLabel(master=frame, text="Generate Names", font=("Roboto", 25))
entry1 = customtkinter.CTkTextbox(
    master=frame, font=("Roboto", 15), width=375, height=275
)
text = customtkinter.CTkEntry(master=frame)
button = customtkinter.CTkButton(master=frame, text="Generate", command=Gene)
checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember")
# spin = customtkinter.CTkOptionMenu(master=frame)


# Layout
frame.pack(pady=20, padx=60, fill="both", expand=True)
label.pack(pady=12, padx=10)
entry1.pack(pady=12, padx=10, expand=True, fill="both")
text.pack(pady=12, padx=10)
button.pack(pady=12, padx=10)
checkbox.pack(pady=3, padx=10)

root.mainloop()
