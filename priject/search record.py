from tkinter import *
import sqlite3 as s
bt1=Tk()
bt1.resizable(0,0)
bt1.geometry("300x300")
bt1.configure(bg="pink")
V1=StringVar()
V2=StringVar()
V3=StringVar()
def selectrecord():
    v1=txt1.get()
    con=s.connect('D:/pytthon files/tkinter/gui/priject/student.db')
    
    result=con.execute('Select * from student where rollno=?',v1)
    
    for r in result:
        V1.set(r[1])
        V2.set(r[2])
        V3.set(r[3])
    
Label(bt1,text="Roll no",font=("arial", 15, 'bold','italic'),bg="pink").grid(row=0,column=0,padx=10,pady=10)
Label(bt1,text="Name",font=("arial", 15, 'bold','italic'),bg="pink").grid(row=1,column=0,padx=10,pady=10)
Label(bt1,text="Branch",font=("arial", 15, 'bold','italic'),bg="pink").grid(row=2,column=0,padx=10,pady=10)
Label(bt1,text="Year",font=("arial", 15, 'bold','italic'),bg="pink").grid(row=3,column=0,padx=10,pady=10)
txt1=Entry(bt1,bd=4)
txt1.grid(row=0,column=1,pady=10,padx=20)
txt2=Entry(bt1,bd=4,textvariable=V1)
txt2.grid(row=1,column=1,pady=10,padx=20)
txt3=Entry(bt1,bd=4,textvariable=V2)
txt3.grid(row=2,column=1,pady=10,padx=20)
txt4=Entry(bt1,bd=4,textvariable=V3)
txt4.grid(row=3,column=1,pady=10,padx=20)
bt=Button(bt1,text="Show record",command=selectrecord)
bt.grid(row=4,columnspan=2,pady=10)
bt1.mainloop()
