from tkinter import *
from tkinter import messagebox as mb
import sqlite3 as s
bt2=Tk()
bt2.resizable(0,0)
bt2.configure(bg="HotPink4")
def show():
    con=s.connect('D:/pytthon files/tkinter/gui/priject/studentinformation.db')
    rs=con.execute('Select * from student')
    
    con.commit()
    for r in rs:
        print(r[0],r[1],r[2],r[3],r[4],r[5],r[6])
        msg.configure(r)
    
Label(bt2,text="      Institute of Engineering and Technology     ",font=("arial" ,30,'bold','italic'),bg="HotPink4").pack(side=TOP)
Label(bt2,text="....Student Record....",font=("Segoe Print" ,20,'bold','underline'),bg="HotPink3").pack(side=TOP,pady=50)
Label(bt2,text="....please click the button below....",font=("Segoe Print" ,20,'bold','underline'),bg="HotPink3").pack(side=TOP,pady=50)

bt=Button(bt2,text="Show Record",font=("Segoe Print" ,20,'bold','underline'),bg="HotPink3",bd=10,command=show)
bt.pack(side=TOP,pady=50)
msg1=Label(bt2)
msg1.pack(side=TOP)
msg2=Label(bt2)
msg2.pack(side=TOP)
msg3=Label(bt2)
msg3.pack(side=TOP)
msg4=Label(bt2)
msg4.pack(side=TOP)
msg5=Label(bt2)
msg5.pack(side=TOP)
msg6=Label(bt2)
msg6.pack(side=TOP)
msg7=Label(bt2)
msg7.pack(side=TOP)
