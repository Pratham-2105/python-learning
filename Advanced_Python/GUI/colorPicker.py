import tkinter as tk 
from tkinter import colorchooser

def choose_color():
    color_code = colorchooser.askcolor(title = "Choose a color")
    print(color_code)
    
root = tk.Tk()
root.title("Color Picker Example")
root.geometry('800x800')

button = tk.Button(root, text = "Choose coloe", comman = choose_color)
button.pack()
root.mainloop()