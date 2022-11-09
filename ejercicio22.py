from tkinter import *

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))
def reset():
    opcion.set(None)
    monitor.config(text="")

root = Tk()
opcion = StringVar()
opcion.set(None)
Radiobutton(root, text="Windows", variable=opcion,
            value='Windows', command=seleccionar).pack(anchor=W)

Radiobutton(root, text="Linux", variable=opcion,
            value='Linux', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="MacOs", variable=opcion,
            value='MacOs', command=seleccionar).pack(anchor=W)


monitor = Label(root)
monitor.pack()
Button(root, text="Reiniciar", command=reset).pack()

root.mainloop()
