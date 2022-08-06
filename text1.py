import tkinter as tk

parent = tk.Tk()
# create the widget.
mytext = tk.Text(parent)

# insert a string at the beginning
mytext.insert(tk.INSERT, "Python exercise")

# insert a string into the current text
mytext.insert(tk.INSERT,"hai python")

# delete the first and last character (including a newline character)
#mytext.delete('10.0',tk.END)
mytext.delete(0.0)
#mytext.delete(19.0)
mytext.pack()
parent.mainloop()