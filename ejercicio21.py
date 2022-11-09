from tkinter import *
master = Tk()
nombres = StringVar()
listbox = Listbox(master)
for item in ["Jose", "Claudia", "Alejandro", "Florencia", "Miguel", "Melisa", "Simon", "Antonio"]:
 listbox.insert(END, item)
listbox.pack()
label = Label(text="Lista de nombres de personas")
label.pack()
master.mainloop()
