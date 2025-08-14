import tkinter
top=tkinter.Tk()
top.title('python GUI')
ent1=tkinter.Entry(top,font=('Arial',16,'italic','bold'),fg='Red',relief='ridge',bd=5)
ent1.pack(padx=10,pady=20)
ent2=tkinter.Entry(top,font=('Arial',16,'italic','bold'),	fg='Red',relief='ridge',bd=3,state='disabled')
ent2.pack(padx=10,pady=30)
top.mainloop()
