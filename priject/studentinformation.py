from tkinter import *
from tkinter import messagebox as mb
import sqlite3 as s
bt0=Tk()
bt0.resizable(0,0)
bt0.configure(bg="royal blue")
#.............................................bt1..................................................................................................

def insert():
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

#.................................................................................bt2..............................................................................

def show():
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


#..............................................................................END................................................................................
    
Label(bt0,text="....Student Information Details....",font=("Segoe Print" ,25,'bold','underline'),bg="royal blue").grid(row=0,column=1)
bt1=Button(bt0,text="Regitraion",font=("arial" ,20, 'bold','italic'),bd=10,command=insert)
bt1.grid(row=1,columnspan=2,pady=25)

bt2=Button(bt0,text="Information",font=("arial" ,20, 'bold','italic'),bd=10,command=show)
bt2.grid(row=2,columnspan=2,pady=25)


