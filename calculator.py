from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.scrolledtext import ScrolledText

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
        self.txt.grid(row=0, column=1, columnspan=5)
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
        sumsign = Button(root, text='=', width=self.wid, height=self.heigh, highlightbackground='red',
                         command=self.isum)
        sumsign.grid(row=5, column=4)

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
            alltext = int(alltext)
        except:
            showinfo('EROR', 'Произошла ошибка')
            self.txt.delete('1.0', END)
            self.txt.config(state=DISABLED)
        else:
            self.txt.delete('1.0', END)
            self.txt.insert(INSERT, alltext / 100)
            self.txt.config(state=DISABLED)

    def minus_plus(self):
        self.txt.config(state=NORMAL)
        try:
            alltext = self.txt.get('1.0', END)
            alltext = int(alltext)
        except:
            showinfo('EROR', 'Произошла ошибка')
            self.txt.delete('1.0', END)
            self.txt.config(state=DISABLED)
        else:
            self.txt.delete('1.0', END)
            self.txt.insert(INSERT, alltext * -1)
            self.txt.config(state=DISABLED)

    def isum(self):
        self.txt.config(state=NORMAL)
        try:
            alltext = self.txt.get('1.0', END)
            alltext = eval(alltext)
        except:
            showinfo('EROR', 'Произошла ошибка')
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
