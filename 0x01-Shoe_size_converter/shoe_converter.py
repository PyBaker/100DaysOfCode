from ctypes import sizeof
import tkinter as tk
from tkinter import *
from tkinter import ttk


uk_size = 0

def clicked(answer=""): # without event because I use `command=` instead of `bind`
    global uk_size

    if answer == 'plus':
        uk_size = uk_size + 1
    elif answer == 'minus':
        uk_size = uk_size - 1

    us_size = uk_size + 1

    label1.configure(text=f'{uk_size} Size in US => {us_size}')


windows = tk.Tk()
windows.geometry('360x260')
windows.title("Shoe Size Converter by PyBaker")

Grid.rowconfigure(windows,0,weight=3)
Grid.columnconfigure(windows,0,weight=1)

label = tk.Label(windows, text="Click on the Button")
label.grid(column=0, row=0)

label1 = tk.Label(windows)
label1.grid(column=0, row=2)

custom_button2 = ttk.Button(windows, text="Minus (-) UK size", command=lambda: clicked('minus'))
custom_button2.grid(column=0, row=1, sticky="NSEW", pady=40, padx=40)

custom_button = ttk.Button(windows, text="Add (+) UK size", command=lambda: clicked('plus'))
custom_button.grid(column=0, row=3, sticky="NSEW",  pady=40, padx=40)

windows.mainloop()
