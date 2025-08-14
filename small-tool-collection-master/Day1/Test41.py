import tkinter as tk
top=tk.Tk()
top.title('python GUI')
top.geometry('300x150+10+10')
lab1=tk.Label(top,text='山静雁声远，水清荷飘香!',
    font=('Verdana',16,'italic','bold'),fg='red',relief='ridge')
lab1.pack(pady=10)
itp = tk.PhotoImage(file = 'E:\\12月09日--12：09.png')
lab2=tk.Label(top, font=('Verdana',16,'italic','bold'),fg='red',relief='ridge',image=itp)
lab2.pack(pady=10)
top.mainloop()
