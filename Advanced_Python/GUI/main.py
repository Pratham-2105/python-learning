import tkinter
from tkinter import *
from tkinter.ttk import Combobox

window = Tk()

window.title("Python training!")

def button_clicked():
    button.config(text = "Good Job", bg = "red", fg = "white")
    
button = Button(window, text = "Hello World !, Click Me", command = button_clicked)
button.pack(padx = 20, pady = 20)

window.geometry('900x900')

# lable = Label(window, text = "Coca-Cola", font=("Aerial BOLD", 70))
# lable.config(bg = "black", fg = "dark red")
# lable.pack(pady = 150, ipady = 50)

#scale1 = tkinter.Scale(window, from_=0, to_=100, orient = tkinter.HORIZONTAL)
# scale = tkinter.Scale(window, from_=0, to_=100, orient = tkinter.VERTICAL)
# scale.pack()

# spinbox = tkinter.Spinbox(window, from_=0, to = 10)
# spinbox.pack()

# radio_var = tkinter.StringVar()
# radiobutton1 = tkinter.Radiobutton(window, text="Male", variable=radio_var, value="male")
# radiobutton2 = tkinter.Radiobutton(window, text="Female", variable=radio_var, value="female")
# radiobutton1.pack()
# radiobutton2.pack()

# listbox = tkinter.Listbox(window)
# listbox.insert(1, "Option 1")
# listbox.insert(2, "Option 2")
# listbox.insert(3, "Option 3")
# listbox.pack()


# def combobox_selected(event):
#     selected_value = combobox.get()
#     label.config(text=f"Selected: {selected_value}")

# # Create a Label to display the selected value
# label = Label(window, text="Select an option:")
# label.pack(padx=20, pady=10)

# # Create a Combobox widget
# options = ["Option 1", "Option 2", "Option 3"]
# combobox = Combobox(window, values=options)
# combobox.pack(padx=20, pady=10)

# # Bind the combobox selection event to the handler
# combobox.bind("<<ComboboxSelected>>", combobox_selected)



window.mainloop()