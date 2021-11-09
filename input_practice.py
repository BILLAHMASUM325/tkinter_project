from tkinter import *
root = Tk()
root.title("input button")

entry = Entry(root, width = 50, borderwidth = 50)
entry.pack()
entry.insert(0, "Enter your name: ")
entry.focus_set()

def MyClick():
    getentry = entry.get()
    label = Label(root, text = getentry)
    label.pack()

button = Button(root, text = "Click me", padx = 10, pady = 10, command =MyClick)
button.pack()

root.mainloop()