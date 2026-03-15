def xor(event):
    a = tx.get()
    lab['text'] = a
from tkinter import *
root = Tk()

tx = Entry(root,width = 40)
lab = Label(root, text = 'text')
lab.pack()
tx.pack()
root.bind('<Return>',xor)
root.mainloop()
