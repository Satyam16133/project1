from tkinter import *
from tkinter import messagebox as mb
import sqlite3 as s
bt2=Tk()
bt2.resizable(0,0)
bt2.configure(bg="HotPink4")
def cse():
    import sqlite3 as s
    bt1 = Tk()
    bt1.resizable(0,0)
    bt1.configure(bg="steel blue")
    bt1.title("computer science students record")
    Label(bt1,text="Institute of engineering and technology",font=("arial" ,30,'bold','underline'),bg="steel blue").pack(side=TOP)
    Label(bt1,text="Computer Science and Engineering",font=("arial" ,30,'bold','underline'),bg="steel blue").pack(side=TOP)
    Label(bt1,text="Student Information",font=("arial" ,30,'bold','underline'),bg="steel blue").pack(side=TOP)
    top=Frame(bt1,width=100,height=100)
    top.pack(side=TOP,padx=30,pady=30)
    top1=Frame(bt1,width=100,height=300)
    top1.pack(side=RIGHT,padx=30,pady=30)
    scrollbar = Scrollbar(top,bg="red")
    scrollbar.pack( side = RIGHT, fill = Y)

    mylist = Listbox(top, yscrollcommand = scrollbar.set,width=100,height=30 )
    con=s.connect('D:/pytthon files/tkinter/gui/priject/information.db')
    rs=con.execute('Select * from info where branch="CSE"')
    (mylist.insert(END,".......... Student Informaion .........."))
    (mylist.insert(END,"                                        "))
    for r in rs:
        mylist.insert(END,"********************")
        mylist.insert(END,r[0],r[1],r[2],r[3],r[4],r[5],r[6])
        mylist.insert(END,"********************")
    con.commit()
    mylist.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command = mylist.yview )
    mainloop()
    
def me():
    import sqlite3 as s
    bt2 = Tk()
    bt2.resizable(0,0)
    bt2.configure(bg="steel blue")
    bt2.title("mechenical students record")
    Label(bt2,text="Institute of engineering and technology",font=("arial" ,30,'bold','underline'),bg="steel blue").pack(side=TOP)
    Label(bt2,text="Computer Science and Engineering",font=("arial" ,30,'bold','underline'),bg="steel blue").pack(side=TOP)
    Label(bt2,text="Student Information",font=("arial" ,30,'bold','underline'),bg="steel blue").pack(side=TOP)
    top=Frame(bt2,width=100,height=100)
    top.pack(side=TOP,padx=30,pady=30)
    top1=Frame(bt2,width=100,height=300)
    top1.pack(side=RIGHT,padx=30,pady=30)
    scrollbar = Scrollbar(top,bg="red")
    scrollbar.pack( side = RIGHT, fill = Y)

    mylist = Listbox(top, yscrollcommand = scrollbar.set,width=100,height=30 )
    con=s.connect('D:/pytthon files/tkinter/gui/priject/information.db')
    rs=con.execute('Select * from info where branch="ME"')
    (mylist.insert(END,".......... Student Informaion .........."))
    (mylist.insert(END,"                                        "))
    for r in rs:
        mylist.insert(END,"********************")
        mylist.insert(END,r[0],r[1],r[2],r[3],r[4],r[5],r[6])
        mylist.insert(END,"********************")
    con.commit()
    mylist.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command = mylist.yview )
    mainloop()

def it():
    import sqlite3 as s
    bt3 = Tk()
    bt3.resizable(0,0)
    bt3.configure(bg="steel blue")
    bt3.title("information technology students record")
    Label(bt3,text="Institute of engineering and technology",font=("arial" ,30,'bold','underline'),bg="steel blue").pack(side=TOP)
    Label(bt3,text="Computer Science and Engineering",font=("arial" ,30,'bold','underline'),bg="steel blue").pack(side=TOP)
    Label(bt3,text="Student Information",font=("arial" ,30,'bold','underline'),bg="steel blue").pack(side=TOP)
    top=Frame(bt3,width=100,height=100)
    top.pack(side=TOP,padx=30,pady=30)
    top1=Frame(bt3,width=100,height=300)
    top1.pack(side=RIGHT,padx=30,pady=30)
    scrollbar = Scrollbar(top,bg="red")
    scrollbar.pack( side = RIGHT, fill = Y)

    mylist = Listbox(top, yscrollcommand = scrollbar.set,width=100,height=30 )
    con=s.connect('D:/pytthon files/tkinter/gui/priject/information.db')
    rs=con.execute('Select * from info where branch="IT"')
    (mylist.insert(END,".......... Student Informaion .........."))
    (mylist.insert(END,"                                        "))
    for r in rs:
        mylist.insert(END,"********************")
        mylist.insert(END,r[0],r[1],r[2],r[3],r[4],r[5],r[6])
        mylist.insert(END,"********************")
    con.commit()
    mylist.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command = mylist.yview )
    mainloop()
    
def ece():
    import sqlite3 as s
    bt4 = Tk()
    bt4.resizable(0,0)
    bt4.configure(bg="steel blue")
    bt4.title("electronics and communication students record")
    Label(bt4,text="Institute of engineering and technology",font=("arial" ,30,'bold','underline'),bg="steel blue").pack(side=TOP)
    Label(bt4,text="Computer Science and Engineering",font=("arial" ,30,'bold','underline'),bg="steel blue").pack(side=TOP)
    Label(bt4,text="Student Information",font=("arial" ,30,'bold','underline'),bg="steel blue").pack(side=TOP)
    top=Frame(bt4,width=100,height=100)
    top.pack(side=TOP,padx=30,pady=30)
    top1=Frame(bt4,width=100,height=300)
    top1.pack(side=RIGHT,padx=30,pady=30)
    scrollbar = Scrollbar(top,bg="red")
    scrollbar.pack( side = RIGHT, fill = Y)

    mylist = Listbox(top, yscrollcommand = scrollbar.set,width=100,height=30 )
    con=s.connect('D:/pytthon files/tkinter/gui/priject/information.db')
    rs=con.execute('Select * from info where branch="IT"')
    (mylist.insert(END,".......... Student Informaion .........."))
    (mylist.insert(END,"                                        "))
    for r in rs:
        mylist.insert(END,"********************")
        mylist.insert(END,r[0],r[1],r[2],r[3],r[4],r[5],r[6])
        mylist.insert(END,"********************")
    con.commit()
    mylist.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command = mylist.yview )
    mainloop()
        
Label(bt2,text="      Institute of Engineering and Technology     ",font=("arial" ,30,'bold','italic'),bg="HotPink4").pack(side=TOP)
Label(bt2,text="....Student Record....",font=("Segoe Print" ,20,'bold','underline'),bg="HotPink3").pack(side=TOP,pady=50)
Label(bt2,text="....please click the button below....",font=("Segoe Print" ,20,'bold','underline'),bg="HotPink3").pack(side=TOP,pady=50)
top=Frame(bt2,width=600,height=100,bg="powder blue")
top.pack(side=TOP)
bt1=Button(top,text="Computer Science",font=("Segoe Print" ,10,'bold','underline'),bg="HotPink3",bd=10,command=cse)
bt1.grid(row=0,column=0)
bt2=Button(top,text="Mechenical",font=("Segoe Print" ,10,'bold','underline'),bg="HotPink3",bd=10,command=me)
bt2.grid(row=0,column=1)
bt3=Button(top,text="Information Technology",font=("Segoe Print" ,10,'bold','underline'),bg="HotPink3",bd=10,command=it)
bt3.grid(row=0,column=2)
bt4=Button(top,text="Electronics and Communication",font=("Segoe Print" ,10,'bold','underline'),bg="HotPink3",bd=10,command=ece)
bt4.grid(row=0,column=3)