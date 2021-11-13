from tkinter import *
root = Tk()
root.title('Checkbox')
root.geometry('500x500')

var = IntVar()

def CheckBox():
    mylabel = Label(root, text=var.get())
    mylabel.pack()

check = Checkbutton(root,text = 'I agree with you', variable = var)
check.pack()

btn = Button(root, text = 'Show result', command = CheckBox)
btn.pack()

root.mainloop()