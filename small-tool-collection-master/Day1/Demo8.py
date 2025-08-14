# 置于上下左右
import tkinter
top=tkinter.Tk()
comm1=tkinter.Button(top,text='Top')
comm1.pack(side='top')
comm2=tkinter.Button(top,text='Botton')
comm2.pack(side='bottom')
comm3=tkinter.Button(top,text='Left')
comm3.pack(side='left')
comm4=tkinter.Button(top,text='Right')
comm4.pack(side='right')
top.mainloop()