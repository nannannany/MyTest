import tkinter
top=tkinter.Tk()
top.title('python GUI')
ent1=tkinter.Entry(top,show='*',font=('Verdana',16))
ent1.pack(pady=12)
ent1.focus_set()
def callback():
    x=ent1.get()
    print('your password is:',x)

btn1=tkinter.Button(top,text='Send out',width=10,
fg='red',font=('Verdana',14,'bold','italic'),command=callback)
btn1.pack(side='left',padx=8)
btn2=tkinter.Button(top,text='Return',width=10,
fg='red',font=('Verdana',14,'bold','italic'),command=quit)
btn2.pack(side='left',padx=8)
top.mainloop()

