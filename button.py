from tkinter import *
root = Tk()
root.title("Button")

def myButton():
    print("It's working")

mybutton = Button(root,text="Click me", fg = "red", bg ="green", padx = 10, pady = 40, command = myButton)

mybutton.grid(row = 0, column = 0)

root.mainloop()