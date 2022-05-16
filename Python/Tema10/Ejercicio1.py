import sys
import tkinter
from tkinter import ttk


window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(2, weight=4)

def seleccionar():

    seleccion_label.config(text=f'{seleccion.get()}')

def limpiar():

    seleccion.set(None)
    seleccion_label.config(text='')

seleccion = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text='Uno', value='uno', variable=seleccion, command=seleccionar)
r2 = ttk.Radiobutton(window, text='Dos', value='dos', variable=seleccion, command=seleccionar)
r3 = ttk.Radiobutton(window, text='Tres', value='tres', variable=seleccion, command=seleccionar)
seleccion_label = ttk.Label(window)
limpiar_button = ttk.Button(window, text='Limpiar', command=limpiar)

r1.grid(column=0, row=1, pady=10, padx=10)
r2.grid(column=0, row=2, pady=10, padx=10)
r3.grid(column=0, row=3, pady=10, padx=10)
seleccion_label.grid(column=2,row=1)
limpiar_button.grid(column=2, row=3)

window.mainloop()
sys.exit(0)  