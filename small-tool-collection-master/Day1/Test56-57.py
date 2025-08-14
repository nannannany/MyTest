'''import tkinter as tk

top = tk.Tk()
top.title('python GUI')

lab1 = tk.Label(top, bg='white', width=35, height=2, text='当前无选择',
                fg='red', bd=6, relief='ridge', font=('隶书', 20))
lab1.grid(row=0, column=1)

var1 = tk.IntVar()
var2 = tk.IntVar()

def psel():
    if (var1.get() == 1) and (var2.get() == 0):
        lab1.config(text='你喜欢花岗辰老师')
    elif (var1.get() == 1) and (var2.get() == 1):
        lab1.config(text='你喜欢花岗辰老师，且喜欢刘含波老师')
    elif (var1.get() == 0) and (var2.get() == 0):
        lab1.config(text='你不喜欢花岗辰老师，也不喜欢刘含波老师')
    else:
        lab1.config(text='你喜欢刘含波老师')

c1 = tk.Checkbutton(top, text='花岗辰老师', width=8, height=2, bd=2, relief='ridge', variable=var1,
                    onvalue=1, offvalue=0, command=psel, font=('Verdana', 14, 'bold'))
c1.grid(row=2, column=1)

c2 = tk.Checkbutton(top, text='刘含波老师', width=8, height=2, bd=2, relief='ridge', variable=var2,
                    onvalue=1, offvalue=0, command=psel, font=('Verdana', 14, 'bold'))
c2.grid(row=3, column=1)

top.mainloop()

'''


import tkinter as tk

top = tk.Tk()
top.title('python GUI')

lab1 = tk.Label(top, bg='white', width=35, height=2, text='当前无选择',
                fg='red', bd=6, relief='ridge', font=('隶书', 20))
lab1.grid(row=0, column=1)

var1 = tk.IntVar()
var2 = tk.IntVar()

def psel():
    if (var1.get() == 1) and (var2.get() == 0):
        lab1.config(text='你喜欢1')
    elif (var1.get() == 1) and (var2.get() == 1):
        lab1.config(text='你喜欢1，且喜欢2')
    elif (var1.get() == 0) and (var2.get() == 0):
        lab1.config(text='你不喜欢1，也不喜欢2')
    else:
        lab1.config(text='你喜欢2')

c1 = tk.Checkbutton(top, text='1', width=8, height=2, bd=2, relief='ridge', variable=var1,
                    onvalue=1, offvalue=0, command=psel, font=('Verdana', 14, 'bold'))
c1.grid(row=2, column=1)

c2 = tk.Checkbutton(top, text='2', width=8, height=2, bd=2, relief='ridge', variable=var2,
                    onvalue=1, offvalue=0, command=psel, font=('Verdana', 14, 'bold'))
c2.grid(row=3, column=1)

top.mainloop()

