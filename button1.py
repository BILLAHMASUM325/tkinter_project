from tkinter import *
root = Tk()
root.title("Button")

def my_Button():
    mylabel = Label(root, text = "it's working").grid(row = 1, column = 0)

mybutton = Button(root, text ="Click me", fg = 'red', bg = 'green', padx ='10', pady = 40, command = my_Button)

mybutton.grid(row = 0, column = 0)



root.mainloop()