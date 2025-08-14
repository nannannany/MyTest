import tkinter as tk
top=tk.Tk()
top.title('python GUI')
v=tk.StringVar()
v.set(0)
lis=['北京','上海','昆明','大连']

def calb():
    for m in lis:
        if v.get()==m:
            lab1=tk.Label(top,text='你想去的旅游城市是：'+v.get()+'!', font=('宋体',10,'bold'),fg='red',bd=3,relief='ridge', height=2)
            lab1.pack()
            btn=tk.Button(top,text='退出',width=5,height=1,fg='red', bg='white',bd=2,font=('隶书',14),command=quit)
            btn.pack()

lab = tk.Label(top, text='请选择你希望的旅游城市：', font=('宋体', 10, 'bold'), fg='Red', relief='ridge', bd=3, height=2)
lab.pack(anchor='w')

radb0 = tk.Radiobutton(top, text=lis[0], font=('Arial', 10, 'italic', 'bold'), fg='Red', relief='ridge', bd=2, width=7, value=lis[0], command=calb, variable=v)
radb0.pack(anchor='w')

radb1 = tk.Radiobutton(top, text=lis[1], font=('Arial', 10, 'italic', 'bold'), fg='Red', relief='ridge', bd=2, width=7, value=lis[1], command=calb, variable=v)
radb1.pack(anchor='w')

radb2 = tk.Radiobutton(top, text=lis[2], font=('Arial', 10, 'italic', 'bold'), fg='Red', relief='ridge', bd=2, width=7, value=lis[2], command=calb, variable=v)
radb2.pack(anchor='w')

radb3 = tk.Radiobutton(top, text=lis[3], font=('Arial', 10, 'italic', 'bold'), fg='Red', relief='ridge', bd=2, width=7, value=lis[3], command=calb, variable=v)
radb3.pack(anchor='w')

top.mainloop()
