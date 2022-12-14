from tkinter import *

# importing the choosecolor package
from tkinter import colorchooser


# Function that will be invoked when the
# button will be clicked in the main window
def choose_color():
    # variable to store hexadecimal code of color
    color_code = colorchooser.askcolor(title="Choose color")
    print(color_code)
    root.config(background=color_code[1])


root = Tk()
button = Button(root, text="Select color",
                command=choose_color)
button.pack()
root.geometry("300x300")
root.mainloop()