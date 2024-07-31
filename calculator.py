from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.scrolledtext import ScrolledText
import math

root = Tk()

class Calculator:

    def __init__(self):
        self.rows = 2
        self.cols = 1
        self.deleteall = None
        self.wid = 10
        self.heigh = 5
        self.lists = ['/', '*', '-', '+']
        self.txt = None
        self.makeWidgets()

    def makeWidgets(self):
        self.txt = ScrolledText(root, width=self.wid, height=1, font=('Arial Black', 50), wrap=WORD, state=DISABLED)
        self.txt.grid(row=0, column=1, columnspan=6)
        root.bind('<Right>', self.tab)
        self.deleteall = Button(root, text='AC', height=self.heigh, width=self.wid, highlightbackground='blue',
                                command=self.delete_all)
        self.deleteall.grid(row=1, column=1)
        change = Button(root, text='+/-', height=self.heigh, width=self.wid, highlightbackground='blue',
                        command=self.minus_plus)
        change.grid(row=1, column=2)
        percent = Button(root, text='%', height=self.heigh, width=self.wid, highlightbackground='blue',
                         command=self.per_cent)
        percent.grid(row=1, column=3)
        reciprocal = Button(root, text='1/x', height=self.heigh, width=self.wid, highlightbackground='blue',
                            command=self.reciprocal)
        reciprocal.grid(row=1, column=4)
        sqrt = Button(root, text='√x', height=self.heigh, width=self.wid, highlightbackground='blue',
                      command=self.sqrt)
        sqrt.grid(row=1, column=5)
        pi = Button(root, text='π', height=self.heigh, width=self.wid, highlightbackground='blue',
                    command=lambda: self.add(math.pi))
        pi.grid(row=2, column=1)
        e = Button(root, text='e', height=self.heigh, width=self.wid, highlightbackground='blue',
                   command=lambda: self.add(math.e))
        e.grid(row=2, column=2)
        factorial = Button(root, text='x!', height=self.heigh, width=self.wid, highlightbackground='blue',
                           command=self.factorial)
        factorial.grid(row=2, column=3)
        log = Button(root, text='lg', height=self.heigh, width=self.wid, highlightbackground='blue',
                     command=self.log)
        log.grid(row=2, column=4)
        ln = Button(root, text='ln', height=self.heigh, width=self.wid, highlightbackground='blue',
                    command=self.ln)
        ln.grid(row=2, column=5)
        for i in range(1, 10):
            btn = Button(root, text=i, height=self.heigh, width=self.wid, highlightbackground='blue',
                         command=lambda i=i: self.add(i))
            if i % 3 == 0:
                btn.grid(row=self.rows, column=self.cols)
                self.rows += 1
                self.cols = 1
            else:
                btn.grid(row=self.rows, column=self.cols)
                self.cols += 1
        zero = Button(root, text='0', height=self.heigh, width=self.wid, highlightbackground='blue',
                      command=lambda: self.add('0'))
        zero.grid(row=5, column=1)
        comma = Button(root, text=',', height=self.heigh, width=self.wid, highlightbackground='blue',
                       command=lambda: self.add('.'))
        comma.grid(row=5, column=2)
        gap = Button(root, height=self.heigh, width=self.wid, highlightbackground='blue')
        gap.grid(row=5, column=3)
        a = 1
        for j in self.lists:
            sign = Button(root, text=j, width=self.wid, height=self.heigh, fg='black', highlightbackground='red',
                          command=lambda j=j: self.add(j))
            sign.grid(row=a, column=4)
            a += 1
        power = Button(root, text='^', width=self.wid, height=self.heigh, fg='black', highlightbackground='red',
                       command=lambda: self.add('**'))
        power.grid(row=5, column=4)
        sumsign = Button(root, text='=', width=self.wid, height=self.heigh, highlightbackground='red',
                         command=self.isum)
        sumsign.grid(row=5, column=5)
        open_paren = Button(root, text='(', height=self.heigh, width=self.wid, highlightbackground='blue',
                            command=lambda: self.add('('))
        open_paren.grid(row=6, column=1)
        close_paren = Button(root, text=')', height=self.heigh, width=self.wid, highlightbackground='blue',
                             command=lambda: self.add(')'))
        close_paren.grid(row=6, column=2)

    def add(self, num):
        self.txt.config(state=NORMAL)
        self.txt.insert(INSERT, num)
        self.txt.see(INSERT)
        self.deleteall.config(text='C')
        self.txt.config(state=DISABLED)

    def delete_all(self):
        self.txt.config(state=NORMAL)
        self.txt.delete('1.0', END)
        self.txt.config(state=DISABLED)
        self.deleteall.config(text='AC')

    def per_cent(self):
        self.txt.config(state=NORMAL)
        try:
            alltext = self.txt.get('1.0', END)
            alltext = eval(alltext) / 100
        except:
            showinfo('ERROR', 'Произошла ошибка')
            self.txt.delete('1.0', END)
            self.txt.config(state=DISABLED)
        else:
            self.txt.delete('1.0', END)
            self.txt.insert(INSERT, alltext)
            self.txt.config(state=DISABLED)

    def minus_plus(self):
        self.txt.config(state=NORMAL)
        try:
            alltext = self.txt.get('1.0', END)
            alltext = eval(alltext) * -1
        except:
            showinfo('ERROR', 'Произошла ошибка')
            self.txt.delete('1.0', END)
            self.txt.config(state=DISABLED)
        else:
            self.txt.delete('1.0', END)
            self.txt.insert(INSERT, alltext)
            self.txt.config(state=DISABLED)

    def isum(self):
        self.txt.config(state=NORMAL)
        try:
            alltext = self.txt.get('1.0', END).strip()
            alltext = eval(alltext)
        except:
            showinfo('ERROR', 'Произошла ошибка')
            self.txt.delete('1.0', END)
            self.txt.config(state=DISABLED)
        else:
            self.txt.delete('1.0', END)
            self.txt.insert(INSERT, alltext)
            self.txt.config(state=DISABLED)

    def sqrt(self):
        self.txt.config(state=NORMAL)
        try:
            alltext = self.txt.get('1.0', END).strip()
            alltext = math.sqrt(eval(alltext))
        except:
            showinfo('ERROR', 'Произошла ошибка')
            self.txt.delete('1.0', END)
            self.txt.config(state=DISABLED)
        else:
            self.txt.delete('1.0', END)
            self.txt.insert(INSERT, alltext)
            self.txt.config(state=DISABLED)

    def factorial(self):
        self.txt.config(state=NORMAL)
        try:
            alltext = self.txt.get('1.0', END).strip()
            num = int(eval(alltext))
            alltext = math.factorial(num)
        except:
            showinfo('ERROR', 'Произошла ошибка')
            self.txt.delete('1.0', END)
            self.txt.config(state=DISABLED)
        else:
            self.txt.delete('1.0', END)
            self.txt.insert(INSERT, alltext)
            self.txt.config(state=DISABLED)

    def log(self):
        self.txt.config(state=NORMAL)
        try:
            alltext = self.txt.get('1.0', END).strip()
            alltext = math.log10(eval(alltext))
        except:
            showinfo('ERROR', 'Произошла ошибка')
            self.txt.delete('1.0', END)
            self.txt.config(state=DISABLED)
        else:
            self.txt.delete('1.0', END)
            self.txt.insert(INSERT, alltext)
            self.txt.config(state=DISABLED)

    def ln(self):
        self.txt.config(state=NORMAL)
        try:
            alltext = self.txt.get('1.0', END).strip()
            alltext = math.log(eval(alltext))
        except:
            showinfo('ERROR', 'Произошла ошибка')
            self.txt.delete('1.0', END)
            self.txt.config(state=DISABLED)
        else:
            self.txt.delete('1.0', END)
            self.txt.insert(INSERT, alltext)
            self.txt.config(state=DISABLED)

    def reciprocal(self):
        self.txt.config(state=NORMAL)
        try:
            alltext = self.txt.get('1.0', END).strip()
            alltext = 1 / eval(alltext)
        except:
            showinfo('ERROR', 'Произошла ошибка')
            self.txt.delete('1.0', END)
            self.txt.config(state=DISABLED)
        else:
            self.txt.delete('1.0', END)
            self.txt.insert(INSERT, alltext)
            self.txt.config(state=DISABLED)

    def tab(self, event):
        self.txt.config(state=NORMAL)
        self.txt.insert(INSERT, ' ')
        self.txt.config(state=DISABLED)

Calculator()
root.mainloop()
