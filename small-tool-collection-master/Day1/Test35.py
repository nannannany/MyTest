import tkinter
top=tkinter.Tk()
top.title('python GUl')
but1=tkinter.Button(top,text='Return',font=('Verdana',16,'italic','bold'),fg='red',command=top.quit)
but1.pack(pady=15)
top.mainloop()