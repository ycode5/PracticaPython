import tkinter
from  tkinter import ttk
window=tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

boton_seleccionado= tkinter.StringVar()
boton_seleccionado1= tkinter.StringVar()
boton_seleccionado2= tkinter.StringVar()
boton_seleccionado3= tkinter.StringVar()

checkbox=ttk.Checkbutton(window,text='opcion 1',variable=boton_seleccionado)
checkbox.grid(column=0,row=1)
checkbox=ttk.Checkbutton(window,text='opcion 2',variable=boton_seleccionado1)
checkbox.grid(column=0,row=2)
checkbox=ttk.Checkbutton(window,text='opcion 3',variable=boton_seleccionado2)
checkbox.grid(column=0,row=3)
checkbox=ttk.Checkbutton(window,text='opcion 4',variable=boton_seleccionado3)
checkbox.grid(column=0,row=4)


lista_label=ttk.Label(window, text='Lista: ')
lista_label.grid(column=0,row=0,sticky=tkinter.W, padx=5,pady=5)


window.mainloop()
