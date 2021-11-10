from tkinter import *
root = Tk()
root.title("frame")

fram = LabelFrame(root, text ="my frame", bg = 'orange', padx=50, pady =50)
fram.pack(padx=10, pady=10)

button = Button(fram, text = "Button one", bg ="grey")
button1 = Button(fram, text = "Button two", bg = "grey" )

button.grid(row = 0, column = 0)
button1.grid(row=0, column = 1)
root.mainloop()