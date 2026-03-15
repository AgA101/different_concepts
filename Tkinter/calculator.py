from tkinter import *
root = Tk()
root['bg'] = 'skyblue'
root.geometry('515x800+1000+0')

class Main(Frame):
    def __init__(self,root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = '0'
        self.lbl = Label(text=self.formula,font=('Times New Roman', 25), bg='skyblue', fg='#000')
        self.lbl.place(x=10, y=15)
        btns = ['c', 'DEL', '.', '%','=',
                '1', '2', '3', '4','5',
                '6', '7', '8', '9','0',
                '+', '-', '*', '/','√X',
                'A','B','C','','X^y',
                'D','E','F','','']
        x,y = 0, 70
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg='#FFF',font=18,command=com).place(x=x, y=y, width=103, height=95)
            x += 103
            if x > 500:
                x = 0
                y += 90
        def per():
            for i in range(len(self.formula)):
                if self.formula[i] in '+-*/':
                    x = self.formula[i]
                    j = i
                    a = self.formula[:j]
                    b = self.formula[j+1:]
                    if x == '+':
                        self.formula = str(int(a) + int(b))
                    elif x == '-':
                        self.formula = str(int(a) - int(b))
                    elif x == '*':
                        self.formula = str(int(a) * int(b))
                    elif x == '/':
                        self.formula = str(int(a) / int(b))
                    
        def per2():
            s,s2 = 0,0
            x = 0
            for i in range(len(self.formula)):
                if self.formula[i] in '+-*/':
                    x = self.formula[i]
                    j = i
            if x != 0:
                a = self.formula[:j]
                b = self.formula[j+1:]
                for i in range(len(a)):
                    s += int(a[len(a)-1 - i]) * 2 ** i
                for i in range(len(b)):
                    s2 += int(b[len(b)-1 - i]) * 2 ** i
                if x == '+':
                    self.formula = str(s + s2)
                elif x == '-':
                    self.formula = str(s - s2)
                elif x == '*':
                    self.formula = str(s * s2)
                elif x == '/':
                    self.formula = str(s / s2)
            
            else:
                a = self.formula
                for i in range(len(a)):
                    s += int(a[len(a)-1 - i]) * 2 ** i
                self.formula = str(s)
                    
        def per3():
            s,s2 = 0,0
            x = 0
            for i in range(len(self.formula)):
                if self.formula[i] in '+-*/':
                    x = self.formula[i]
                    j = i
            if x != 0:
                a = self.formula[:j]
                b = self.formula[j+1:]
                for i in range(len(a)):
                    s += int(a[len(a)-1 - i]) * 8 ** i
                for i in range(len(b)):
                    s2 += int(b[len(b)-1 - i]) * 8 ** i
                if x == '+':
                    self.formula = str(s + s2)
                elif x == '-':
                    self.formula = str(s - s2)
                elif x == '*':
                    self.formula = str(s * s2)
                elif x == '/':
                    self.formula = str(s / s2)
            else:
                a = self.formula
                for i in range(len(a)):
                    s += int(a[len(a)-1 - i]) * 8 ** i
                self.formula = str(s)
        
        def per4():
            s,s2 = 0,0
            x = 0
            for i in range(len(self.formula)):
                if self.formula[i] in '+-*/':
                    x = self.formula[i]
                    j = i
            if x != 0:
                a = self.formula[:j]
                b = self.formula[j+1:]
                for i in range(len(a)):
                    if a[len(a)-1 - i] == 'A':
                        s += 10 * 16 ** i
                    elif a[len(a)-1 - i] == 'B':
                        s += 11 * 16 ** i
                    elif a[len(a)-1 - i] == 'C':
                        s += 12 * 16 ** i
                    elif a[len(a)-1 - i] == 'D':
                        s += 13 * 16 ** i
                    elif a[len(a)-1 - i] == 'E':
                        s += 14 * 16 ** i
                    elif a[len(a)-1 - i] == 'F':
                        s += 15 * 16 ** i
                    else:
                        s += int(a[len(a)-1 - i]) * 16 ** i
            
                for i in range(len(b)):
                    if b[len(b)-1 - i] == 'A':
                        s2 += 10 * 16 ** i
                    elif b[len(b)-1 - i] == 'B':
                        s2 += 11 * 16 ** i
                    elif b[len(b)-1 - i] == 'C':
                        s2 += 12 * 16 ** i
                    elif b[len(b)-1 - i] == 'D':
                        s2 += 13 * 16 ** i
                    elif b[len(b)-1 - i] == 'E':
                        s2 += 14 * 16 ** i
                    elif b[len(b)-1 - i] == 'F':
                        s2 += 15 * 16 ** i
                    else:
                        s2 += int(b[len(b)-1 - i]) * 16 ** i
                    
                if x == '+':
                    self.formula = str(s + s2)
                elif x == '-':
                    self.formula = str(s - s2)
                elif x == '*':
                    self.formula = str(s * s2)
                elif x == '/':
                    self.formula = str(s / s2)
            else:
                a = self.formula
                for i in range(len(a)):
                    if a[len(a)-1 - i] == 'A':
                        s += 10 * 16 ** i
                    elif a[len(a)-1 - i] == 'B':
                        s += 11 * 16 ** i
                    elif a[len(a)-1 - i] == 'C':
                        s += 12 * 16 ** i
                    elif a[len(a)-1 - i] == 'D':
                        s += 13 * 16 ** i
                    elif a[len(a)-1 - i] == 'E':
                        s += 14 * 16 ** i
                    elif a[len(a)-1 - i] == 'F':
                        s += 15 * 16 ** i
                    else:
                        s += int(a[len(a)-1 - i]) * 16 ** i
                self.formula = str(s)
                
        def per6():
            b = self.formula
            s = ''
            while int(b) != 0:
                s += str(int(b) % 2)
                b = int(b) // 2
            self.formula = s[::-1]
        def per7():
            b = self.formula
            s = ''
            while int(b) != 0:
                s += str(int(b) % 8)
                b = int(b) // 8
            self.formula = s[::-1]
        def per8():
            b = self.formula
            s = ''
            while int(b) != 0:
                if int(b) % 16 == 10:
                    s += 'A'
                elif int(b) % 16 == 11:
                    s += 'B'
                elif int(b) % 16 == 12:
                    s += 'C'
                elif int(b) % 16 == 13:
                    s += 'D'
                elif int(b) % 16 == 14:
                    s += 'E'
                elif int(b) % 16 == 15:
                    s += 'F'
                else:
                    s += str(int(b) % 16)
                b = int(b) // 16
            self.formula = str(s[::-1])
              
        header = Label(text='нач-ная С.СЧ.').place(x=x, y=y, width=103, height=95)
        lang = IntVar()
        checkbutton1 = Radiobutton(text="10-ная", value=1, variable=lang, command = per).place(x=x + 103, y=y , width=103, height=95)
        checkbutton2 = Radiobutton(text="2-ная", value=2, variable=lang, command = per2).place(x=x + 206, y=y , width=103, height=95)   
        checkbutton3 = Radiobutton(text="8-ная", value=3, variable=lang, command = per3).place(x=x + 309, y=y , width=103, height=95)
        checkbutton4 = Radiobutton(text="16-ная", value=4, variable=lang, command = per4).place(x=x + 412, y=y , width=103, height=95)

        header2 = Label(text='кон-ная С.СЧ.').place(x=x, y=y + 95 , width=103, height=95)
        ang = IntVar()
        checkbutton5 = Radiobutton(text="10-ная", value=1, variable=ang).place(x=x + 103, y=y + 95 , width=103, height=95)
        checkbutton6 = Radiobutton(text="2-ная", value=2, variable=ang, command = per6).place(x=x + 206, y=y + 95  , width=103, height=95)   
        checkbutton7 = Radiobutton(text="8-ная", value=3, variable=ang, command = per7).place(x=x + 309, y=y + 95  , width=103, height=95)
        checkbutton8 = Radiobutton(text="16-ная", value=4, variable=ang, command = per8).place(x=x + 412, y=y + 95  , width=103, height=95)
    def logicalc(self, oper):
        if oper == 'c':
            self.formula = ''
        elif oper == 'DEL':
            self.formula = self.formula[0:-1]
        elif oper == '√X':
            self.formula = str((eval(self.formula))**(1/2))
        elif oper == 'X^y':
            self.formula = self.formula + '**'
        elif oper == '%':
            self.formula = str(eval(self.formula) / 100)
        elif oper == '=':
            self.formula = str(eval(self.formula))
    
        else:
            if self.formula == '0':
                self.formula = ''
            self.formula += oper
        self.update()

    def update(self):
        if self.formula == '':
            self.formula = '0'
        self.lbl.configure(text=self.formula)

a = Main(root)
a.pack()
root.mainloop()
