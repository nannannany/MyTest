import tkinter as tk
import pickle
import tkinter.messagebox
from PIL import Image, ImageTk
import os

# 初始窗口
window = tk.Tk()
window.title('Welcome Login')
window.geometry('450x300')

# 定义画布与图片
canvas = tk.Canvas(window, height=300, width=450)
image_path = '../Image/day2-1.jpg'  # 确保图片路径正确
try:
    im = Image.open(image_path)
    image_file = ImageTk.PhotoImage(im)
    canvas.create_image(0, 0, anchor='nw', image=image_file)
except FileNotFoundError:
    print(f"图片未找到: {image_path}")

canvas.pack(side='top')

# 定义标题
tk.Label(window, text='UserName').place(x=110, y=110)
tk.Label(window, text='PassWord').place(x=110, y=150)

# 定义输入框
var_usr_name = tk.StringVar()
var_usr_name.set('123456789@qq.com')
var_usr_pwd = tk.StringVar()
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=185, y=110)
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=185, y=150)

# 登录功能
def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        usrs_info = {}
        with open('usrs_info.pickle', 'wb') as usr_file:
            pickle.dump(usrs_info, usr_file)

    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='Welcome', message=usr_name + ' 你好')
        else:
            tk.messagebox.showinfo(title='Error', message='密码错误')
    else:
        is_sign_up = tk.messagebox.askyesno('您还没有注册', '是否注册账号?')
        if is_sign_up:
            usr_sign_up()

# 注册功能
def usr_sign_up():
    # 定义注册页面二级弹窗
    def sign_to_Mofan_Python():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()

        try:
            with open('usrs_info.pickle', 'rb') as usr_file:
                exist_usr_info = pickle.load(usr_file)
        except FileNotFoundError:
            exist_usr_info = {}

        if np != npf:
            tk.messagebox.showerror('错误提示', "密码和确认密码必须一样")
        elif nn in exist_usr_info:
            tk.messagebox.showerror("错误提示", "用户名已存在")
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('欢迎', '注册成功!')

            open_computer()

    # 点击注册之后会弹出这个窗口界面
    window_sign_up = tk.Toplevel(window)
    window_sign_up.title("欢迎注册")
    window_sign_up.geometry('360x200')

    new_name = tk.StringVar()
    new_name.set('123456789@qq.com')  # 设置的是默认值
    tk.Label(window_sign_up, text='用户名').place(x=10, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=100, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='密 码').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=100, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='确认密码').place(x=10, y=90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=100, y=90)

    btn_confirm_sign_up = tk.Button(window_sign_up, text='注 册', command=sign_to_Mofan_Python)
    btn_confirm_sign_up.place(x=120, y=130)

def open_computer():
    # 根据操作系统执行关机命令
    if os.name == 'nt':  # Windows
        os.system('shutdown /s /t 1')  # 1 秒后关机
    elif os.name == 'posix':  # macOS/Linux
        os.system('sudo shutdown now')


# 创建注册和登录按钮
btn_login = tk.Button(window, text='登 录', command=usr_login)
btn_login.place(x=150, y=230)

btn_sign_up = tk.Button(window, text='注 册', command=usr_sign_up)
btn_sign_up.place(x=250, y=230)

window.mainloop()
