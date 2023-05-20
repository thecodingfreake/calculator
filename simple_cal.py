from tkinter import *


def data(number):
    entry.insert(END, number)


def equal():
    a = str(entry.get())
    for i in a:
        if i == '+':
            b = a.split(sep='+')
            summation = 0
            for j in b:
                c = int(j)
                summation += c
            print(summation)
            break
        elif i == '-':
            b = a.split(sep='-')
            summation = 0
            for j in b:
                c = int(j)
                summation -= c
            print(summation)
            break
        elif i == '*':
            b = a.split(sep='*')
            summation = 1
            for j in b:
                c = int(j)
                summation *= c
            print(summation)
            break
        elif i == '/':
            b = a.split(sep='/')
            summation = 1
            for j in range(len(b)):
                c = int(b[int(j)-1])
                d = int(b[int(j)])
                summation = (c/d)
            print(summation)
            break


def clear():
    entry.delete((len(entry.get())-1), END)


window = Tk()
entry = Entry(window, width=80)
frame = Frame(window)
button1 = Button(window, text='1', padx=50, pady=10, command=lambda: data(1))
button2 = Button(window, text='2', padx=50, pady=10, command=lambda: data(2))
button3 = Button(window, text='3', padx=50, pady=10, command=lambda: data(3))
button4 = Button(window, text='4', padx=50, pady=10, command=lambda: data(4))
button5 = Button(window, text='5', padx=50, pady=10, command=lambda: data(5))
button6 = Button(window, text='6', padx=50, pady=10, command=lambda: data(6))
button7 = Button(window, text='7', padx=50, pady=10, command=lambda: data(7))
button8 = Button(window, text='8', padx=50, pady=10, command=lambda: data(8))
button9 = Button(window, text='9', padx=50, pady=10, command=lambda: data(9))
button0 = Button(window, text='0', padx=50, pady=10, command=lambda: data(0))
button_add = Button(window, text='+', padx=50, pady=10, command=lambda: data('+'))
button_subtract = Button(window, text='-', padx=50, pady=10, command=lambda: data('-'))
button_divide = Button(window, text='/', padx=50, pady=10, command=lambda: data('/'))
button_multiply = Button(window, text='*', padx=50, pady=10, command=lambda: data('*'))
button_equal = Button(window, text='=', padx=50, pady=10, command=equal)
button_clear = Button(window, text='clear', padx=40, pady=10, command=lambda: clear())
entry.grid(row=0, column=1, columnspan=4)
button1.grid(row=3, column=1)
button2.grid(row=3, column=2)
button3.grid(row=3, column=3)
button4.grid(row=2, column=1)
button5.grid(row=2, column=2)
button6.grid(row=2, column=3)
button7.grid(row=1, column=1)
button8.grid(row=1, column=2)
button9.grid(row=1, column=3)
button0.grid(row=4, column=1)
button_add.grid(row=3, column=4)
button_subtract.grid(row=2, column=4)
button_divide.grid(row=1, column=4)
button_multiply.grid(row=4, column=2)
button_clear.grid(row=4, column=3)
button_equal.grid(row=4, column=4)


window.mainloop()
