import tkinter as tk

root = tk.Tk()
root.title("Canvas Example")

canvas = tk.Canvas(root, width = 400, height = 300)
canvas.pack()

canvas.create_line(0, 0, 200, 100)
canvas.create_rectangle(50, 50, 150, 150, fill = "blue")
root.mainloop()