import tkinter as tk
import random

root = tk.Tk()
root.title("按钮移动示例")
root.geometry("400x300")
hello_button = tk.Button(root, text="Hello")
hello_button.pack()
def move_hello_button():
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    new_x = random.randint(0, window_width - hello_button.winfo_width())
    new_y = random.randint(0, window_height - hello_button.winfo_height())

    hello_button.place(x=new_x, y=new_y)
python_button = tk.Button(root, text="PYTHON", command=move_hello_button)
python_button.pack()
# 运行主循环
root.mainloop()
