from tkinter import *
from tkinter import messagebox as mb
import sqlite3 as s
bt1=Tk()
bt1.resizable(0,0)
bt1.configure(bg="powder blue")
bt1.title("Registraion Form")
def insertrecord():
    v1=txt1.get()
    v2=txt2.get()
    v3=txt3.get()
    v4=txt4.get()
    v5=txt5.get()
    v6=txt6.get()
    v7=txt7.get()
    con=s.connect('D:/pytthon files/tkinter/gui/priject/information.db')
    con.execute('insert into info values(?,?,?,?,?,?,?)',(v1,v2,v3,v4,v5,6,v7))
    con.commit()
    mb.showinfo("message","Record Enters....")
Label(bt1,text="Student Registration Form",font=("arial" ,25,'bold','underline'),bg="powder blue").grid(row=0,columnspan=2,padx=10,pady=10)  
Label(bt1,text="Enter Student Name .....",font="arial 15",bg="powder blue").grid(row=1,column=0,pady=10)
Label(bt1,text="Enter Student Father's name... ",font="arial 15",bg="powder blue").grid(row=2,column=0,pady=10)
Label(bt1,text="Enter Student Branch name...",font="arial 15",bg="powder blue").grid(row=3,column=0,pady=10)
Label(bt1,text="Enter Student Rollno...",font="arial 15",bg="powder blue").grid(row=4,column=0,pady=10)
Label(bt1,text="Enter Student Mobile no...",font="arial 15",bg="powder blue").grid(row=5,column=0,pady=10)
Label(bt1,text="Enter Student Gender....",font="arial 15",bg="powder blue").grid(row=6,column=0,pady=10)
Label(bt1,text="Enter Student year....",font="arial 15",bg="powder blue").grid(row=7,column=0,pady=10)
txt1=Entry(bt1,bd=4)
txt1.grid(row=1,column=1,pady=10,padx=10)
txt2=Entry(bt1,bd=4)
txt2.grid(row=2,column=1,pady=10,padx=10)
txt3=Entry(bt1,bd=4)
txt3.grid(row=3,column=1,pady=10,padx=10)
txt4=Entry(bt1,bd=4)
txt4.grid(row=4,column=1,pady=10,padx=10)
txt5=Entry(bt1,bd=4)
txt5.grid(row=5,column=1,pady=10,padx=10)
txt6=Entry(bt1,bd=4)
txt6.grid(row=6,column=1,pady=10,padx=10)
txt7=Entry(bt1,bd=4)
txt7.grid(row=7,column=1,pady=10,padx=10)
bt=Button(bt1,text="Insert Record",font=("arial",10,'bold'),command=insertrecord,width=20,bd=10)
bt.grid(row=8,columnspan=2,pady=10)
Label(bt1,text="NOTE-: RECORD SHOULD BE ENTER IN UPPERCASE CHARACTER........",font="arial 15",bg="powder blue").grid(row=9,column=0,pady=10)
bt1.mainloop()
