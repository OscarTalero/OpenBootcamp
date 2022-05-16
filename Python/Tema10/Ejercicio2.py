import sys
import tkinter
from tkinter import Listbox, StringVar, ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(2, weight=4)

lista = ['Debian', 'Arch', 'Fedora', 'Slack']
lista_items = tkinter.StringVar(value=lista)
listbox_linux = tkinter.Listbox(window, height=5, listvariable=lista_items)

titulo = tkinter.Label(window, text='Distribuciones Linux')
listbox_linux.grid(column=1, row=1)
titulo.grid(column=1, row=0, ipadx=10, ipady=10)

window.mainloop()
sys.exit(0)  