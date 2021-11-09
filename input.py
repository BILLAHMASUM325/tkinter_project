from tkinter import *
root = Tk()
root.title("input button")

myentry = Entry(root, width =50, borderwidth = 50)
myentry.pack()
myentry.insert(0, "Enter your name: ")
myentry.focus_set()

def MyClick():
    getentry = myentry.get()
    mylabel = Label(root, text = getentry)
    mylabel.pack()

mybtn = Button(root, text = "Click Me", padx = 10, pady = 10, command = MyClick)
mybtn.pack()

root.mainloop()