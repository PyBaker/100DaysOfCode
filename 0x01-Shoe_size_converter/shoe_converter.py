import tkinter as tk
from tkinter import ttk


count = 0

def clicked(answer=""): # without event because I use `command=` instead of `bind`
    global count

    if answer == 'plus':
        count = count + 1
    elif answer == 'minus':
        count = count - 1

    label1.configure(text=f'Size in US => {count}')


windows = tk.Tk()
windows.title("Shoe Size Converter by PyBaker")

label = tk.Label(windows, text="Click on the Button")
label.grid(column=0, row=0)

label1 = tk.Label(windows)
label1.grid(column=0, row=1)

custom_button2 = ttk.Button(windows, text="Minus (-) UK size", command=lambda: clicked('minus'))
custom_button2.grid(column=1, row=0, pady=10, padx=10)

custom_button = ttk.Button(windows, text="Add (+) UK size", command=lambda: clicked('plus'))
custom_button.grid(column=2, row=0, pady=10, padx=10)

windows.mainloop()
