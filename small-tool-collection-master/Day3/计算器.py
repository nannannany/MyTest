import tkinter as tk
from tkinter import messagebox
import math


class Calculator:
    def __init__(self):
        # 创建主界面，并且保存到成员属性中
        self.root = tk.Tk()
        self.root.minsize(280, 450)
        self.root.maxsize(280, 470)
        self.root.title("计算器")

        # 设置显示面板的变量
        self.result = tk.StringVar()
        self.result.set(' ')  # 初始化为空字符串

        # 运算数字和符号的列表
        self.lists = []

        # 界面布局
        self.menus()
        self.layout()
        self.root.mainloop()

    def menus(self):
        # 创建总菜单
        allmenu = tk.Menu(self.root)

        # 添加子菜单
        filemenu = tk.Menu(allmenu, tearoff=0)
        filemenu.add_command(Label='标准型（T）', accelerator='Alt+1', command=self.myfunc)
        filemenu.add_command(Label='科学型（S）', accelerator='Alt+2', command=self.myfunc)
        filemenu.add_command(Label='程序员（P）', accelerator='Alt+3', command=self.myfunc)
        filemenu.add_command(Label='统计信息（A）', accelerator='Alt+4', command=self.myfunc)
        filemenu.add_separator()
        filemenu.add_command(Label='历史记录（Y）', accelerator='Ctrl+H', command=self.myfunc)
        filemenu.add_command(Label='数字分组（I）', command=self.myfunc)
        filemenu.add_separator()
        filemenu.add_command(Label='基本（B）', accelerator='Ctrl+F4', command=self.myfunc)
        filemenu.add_command(Label='单位转换（U）', accelerator='Ctrl+U', command=self.myfunc)
        filemenu.add_command(Label='日期计算（D）', accelerator='Ctrl+E', command=self.myfunc)

        menu1 = tk.Menu(filemenu, tearoff=0)
        menu1.add_command(Label='抵押（M）', command=self.myfunc)
        menu1.add_command(Label='汽车租赁（V）', command=self.myfunc)
        menu1.add_command(Label='油耗（mpg）（F）', command=self.myfunc)
        menu1.add_command(Label='油耗(/10okm)（U）', command=self.myfunc)

        filemenu.add_cascade(Label='工作表（W）', menu=menu1)

        allmenu.add_cascade(Label='文件（F）', menu=filemenu)

        editmenu = tk.Menu(allmenu, tearoff=0)
        editmenu.add_command(Label='复制（C）', accelerator='Ctrl+C', command=self.myfunc)
        editmenu.add_command(Label='粘贴（V）', accelerator='Ctrl+V', command=self.myfunc)
        editmenu.add_separator()
        menu2 = tk.Menu(editmenu, tearoff=0)
        menu2.add_command(Label='复制历史记录（H）', command=self.myfunc)
        menu2.add_command(Label='编辑（E）', accelerator='F2', command=self.myfunc)
        menu2.add_command(Label='取消编辑（N）', accelerator='Esc', command=self.myfunc)
        menu2.add_command(Label='清除（L）', accelerator='Ctrl+Shift+D', command=self.myfunc)
        editmenu.add_cascade(Label='历史记录（H）', menu=menu2)

        allmenu.add_cascade(Label='编辑（E）', menu=editmenu)

        helpmenu = tk.Menu(allmenu, tearoff=0)
        helpmenu.add_command(Label='查看帮助（F1）', command=self.myfunc)
        helpmenu.add_separator()
        helpmenu.add_command(Label='关于计算器（A）', command=self.myfunc)

        allmenu.add_cascade(Label='帮助（H）', menu=helpmenu)

        self.root.config(menu=allmenu)

    def layout(self):
        # 显示屏幕
        result = tk.StringVar()
        result.set('0')
        show_label = tk.Label(self.root, bd=3, bg='white', font=('宋体', 30), anchor='e', textvariable=self.result)
        show_label.place(x=5, y=20, width=270, height=70)

        # 功能键布局
        buttons = [
            ('Mc', 5, 95), ('MR', 68, 95), ('Ms', 115, 95), ('M+', 170, 95),
            ('M-', 225, 95), ('C', 5, 158), ('CE', 115, 158), ('±', 178, 158),
            ('√', 225, 158), ('7', 5, 205), ('8', 60, 205), ('9', 115, 205),
            ('/', 178, 285), ('//', 225, 205), ('4', 5, 268), ('5', 60, 260),
            ('6', 115, 268), ('*', 170, 260), ('1/x', 225, 260), ('1', 5, 315),
            ('2', 60, 315), ('3', 115, 315), ('-', 170, 315), ('=', 225, 315),
            ('0', 5, 378), ('.', 115, 378), ('+', 178, 370)
        ]

        for text, x, y in buttons:
            button = tk.Button(self.root, text=text, command=lambda t=text: self.pressnum(t))
            button.place(x=x, y=y, width=50, height=50)

    def myfunc(self):
        messagebox.showinfo("预留接口", "学成之后，你是不是有冲动添加该功能？*")

    def pressnum(self, num):
        if self.ispresssign:
            self.result.set('')
            self.ispresssign = False
        if num == ".":
            num = "8."
        oldnum = self.result.get()
        if oldnum == '0':
            self.result.set(num)
        else:
            newnum = oldnum + num
            self.result.set(newnum)

    def presscalculate(self, sign):
        num = self.result.get()
        self.lists.append(num)
        self.lists.append(sign)
        self.ispresssign = True

    def pressequal(self):
        curnum = self.result.get()
        self.lists.append(curnum)
        calculatestr = ''.join(self.lists)
        endnum = eval(calculatestr)
        self.result.set(str(endnum)[:10])
        if self.lists != []:
            self.ispresssign = True
        self.lists.clear()

    def dele_one(self):
        if self.result.get() == '0':
            return
        else:
            num = len(self.result.get())
            if num > 1:
                strnum = self.result.get()
                strnum = strnum[0:num - 1]
                self.result.set(strnum)
            else:
                self.result.set('0')

    def zf(self):
        strnum = self.result.get()
        if strnum[0] == ".":
            self.result.set(strnum[1:])
        elif strnum[0] != "." and strnum != '0':
            self.result.set(strnum[0] + strnum[1:][::-1])

    def ds(self):
        dsnum = 1 / float(self.result.get())
        self.result.set(str(dsnum)[:10])
        if self.lists != []:
            self.ispresssign = True
        self.lists.clear()

    def sweeppress(self):
        self.lists.clear()
        self.result.set('0')

    def kpf(self):
        strnum = float(self.result.get())
        endnum = math.sqrt(strnum)
        if str(endnum)[-1] == "0":
            self.result.set(str(endnum)[:-2])
        else:
            self.result.set(str(endnum)[:10])
        if self.lists != []:
            self.ispresssign = True
        self.lists.clear()

    def wait(self):
        messagebox.showinfo("更新中...", "敬请期待...")


# 实例化对象
my_calculator = Calculator()