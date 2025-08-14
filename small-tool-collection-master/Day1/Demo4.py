# 网格化
import tkinter
top=tkinter.Tk()
comm1=tkinter.Button(top,text='hello')
comm1.grid(row=0,column=0)
comm2=tkinter.Button(top,text='python')
comm2.grid(row=0,column=1)
comm3=tkinter.Button(top,text='good')
comm3.grid(row=0,column=2)
top.mainloop()