from tkinter import *
root = Tk()
root.title("Tkinter_python")

label1 = Label(root,text = 'Hello World').grid(row=2, column = 2)
label2 = Label(root,text = "Hello").grid(row = 1, column = 1)
#label1.grid(row=0, column = 0)
#label2.grid(row = 0, column = 1)
#label.pack()

root.mainloop()
