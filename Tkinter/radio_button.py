from tkinter import *
root = Tk()
root.geometry("300x250")
 
header = Label(text="Выберите курс", padx=15, pady=10)
header.grid(row=0, column=0, sticky=W)
 
lang = IntVar()
 
python_checkbutton = Radiobutton(text="Python", value=1, variable=lang, padx=15, pady=10)
python_checkbutton.grid(row=1, column=0, sticky=W)
 
javascript_checkbutton = Radiobutton(text="JavaScript", value=2, variable=lang, padx=15, pady=10)
javascript_checkbutton.grid(row=2, column=0, sticky=W)
selection = Label(textvariable=lang, padx=15, pady=10)
selection.grid(row=3, column=0, sticky=W) 
root.mainloop()
