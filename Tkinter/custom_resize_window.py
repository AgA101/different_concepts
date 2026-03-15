def xor(event):
   
    fra['width'] = size[0].get()
    fra['height'] = size[1].get()
    
from tkinter import *
root = Tk()
fra = Frame(root, width=100, height = 100,bd = 20,bg = 'green')
fra.pack()

size = [Entry(root,width = 40) for i in [1,2]]
for i in size:
    i.pack()

root.bind('<space>',xor)
root.mainloop()
