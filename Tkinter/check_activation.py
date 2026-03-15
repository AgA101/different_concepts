from tkinter import *

root = Tk()

c = [IntVar() for i in range(3)]
txt = Label(root, text='', width=100, height=30, font="Verdana 12")


class TextState:
    on = ''
    off = ''


text = TextState()


def update_label():
    """Обновляет надпись по текущему состоянию флажков."""
    text.on = 'Включены: '
    text.off = 'Выключены: '
    names = ['первый', 'второй', 'третий']

    for i in range(len(c)):
        if c[i].get() == 1:
            text.on += names[i] + ', '
        else:
            text.off += names[i] + ', '

    txt['text'] = text.on.rstrip(', ') + '  |  ' + text.off.rstrip(', ')


checks = [Checkbutton(root, text=f"{i+1}", variable=(c[i]), command=update_label) for i in range(3)]

for check in checks:
    check.pack()
txt.pack()

update_label()

root.mainloop()
