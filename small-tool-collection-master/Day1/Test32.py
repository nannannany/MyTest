import tkinter
top=tkinter.Tk()
top.title('python GUl')

butt1=tkinter.Button(top,width=10,bg='red',fg='blue',bd=8,text='Welcome',anchor='center',
    font=('Arial',24,'bold'))
butt1.pack(pady=20)
butt2=tkinter.Button(top,width=15,bd=6,text='Eliminate',anchor='s',
    font=('Levenim MT',16,'italic'))
butt2.pack(pady=15)
butt3=tkinter.Button(top,width=10,bd=4,text='Return',anchor='e',
    font=("Verdana',18,'italic','bold"),relief='groove',cursor='cross arrow')
butt3.pack(pady=10)

top.title('python GUl')
but1=tkinter.Button(top,text='Return',font=('Verdana',16,'italic','bold'),fg='red',command=top.quit)
but1.pack(pady=15)
top.mainloop()