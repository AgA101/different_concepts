from functools import partial
from tkinter import *

root = Tk()
a = 100
fra = Frame(root, width=a, height=a, bd=20, bg='green')

def resize(event, size):
    """Меняет размер fra на size x size."""
    fra['width'] = size
    fra['height'] = size

fra.pack()

# Конфиг кнопок: (подпись, размер окна)
BUTTON_CONFIG = [
    ("маленький", 10),
    ("средний", 50),
    ("большой", 100),
]
buttons = [Button(root, text=text) for text, _ in BUTTON_CONFIG]
for btn, (_, size) in zip(buttons, BUTTON_CONFIG):
    btn.bind('<Button-1>', partial(resize, size=size))
    btn.pack()


root.mainloop()