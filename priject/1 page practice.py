from tkinter import *
from PIL import ImageTk,Image
import random
import time;
root=Tk()
root.geometry("1350x800+0+0")
stopm=False
root.title("Institute of Engineering and Technology Ayodhya UP")
#................................................................director............................................................................................

def director():
    from PIL import ImageTk,Image
    bt3=Toplevel()
    bt3.geometry("1350x800+0+0")
    bt3.configure(bg="Hot Pink3")
    bt3.title("Director Table")
    tops=Frame(bt3,width=1600,height=200,bg="Hot Pink3")
    tops.pack(side=TOP)
    img=(Image.open("D:/pytthon files/tkinter/gui/priject/rmlicon.png"))
    img=ImageTk.PhotoImage(img)
    panel=Label(tops,image=img,bg="Hot Pink3")
    panel.image=img
    panel.grid(row=0,column=1)
    Label(tops,text="INSTITUTE OF ENGINEERING AND TECHNOLOGY",font=('arial' ,20, 'bold'),bg="Hot Pink3",fg="midnight blue").grid(row=1,column=1,padx=20)
    tops1=Frame(bt3,width=300,height=300,bg="powder blue")
    tops1.pack(side=LEFT)
    img1=(Image.open("D:/pytthon files/tkinter/gui/priject/rmldirector.jpg"))
    img1=ImageTk.PhotoImage(img1)
    panel=Label(tops1,image=img1,bg="Hot Pink3")
    panel.image=img1
    panel.grid(row=0,column=1)
    tops2=Frame(bt3,width=600,height=300,bg="Hot Pink")
    tops2.pack(side=RIGHT)
    la=Label(tops2,text="Professor Ramapati Mishra started his career in industry by serving prestigious Indian AirForce   ",font=("Segoe Print" ,15, "bold"),bg="Hot Pink")
    la.grid(row=0,column=0)

    la=Label(tops2,text="in technical servicing fighter planes and its systems. Since 2001,he joined I.E.T. as Assistant in    ",font=("Segoe Print" ,15,"bold"),bg="Hot pink")
    la.grid(row=1,column=0)

    la=Label(tops2,text="  Electronics And Communication branch, then rose to be come Associate Proffesor and H.O.D, in    ",font=("Segoe Print" ,15, "bold","bold"),bg="Hot pink")
    la.grid(row=2,column=0)

    la=Label(tops2,text="same department. In year 2010 after compilition of hid P.hd he became director in different colleges   ",font=("Segoe Print" ,15, "bold"),bg="Hot Pink")
    la.grid(row=3,column=0)

    la=Label(tops2,text="in UP and Uttrakhand . After 6 years he again joined I.E.T. Since May 2018 he is leanding I.E.T.  as     ",font=("Segoe Print" ,15, "bold"),bg="Hot Pink")
    la.grid(row=4,column=0)

    la=Label(tops2,text="director taking I.E.T. to newer dimensions full of engineering activities this series of workshop is       ",font=("Segoe Print" ,15, "bold"),bg="Hot Pink")
    la.grid(row=5,column=0)
    la=Label(tops2,text="an example",font=("Segoe Print" ,15, "bold"),bg="Hot Pink")
    la.grid(row=6,column=0)

#.......................................................................director...............................................................................
#.......................................................................vice chacellor.........................................................................

def vice():
    from PIL import ImageTk,Image
    import random
    import time;
    bt4=Toplevel()
    bt4.geometry("1350x800")
    bt4.configure(bg="white")
    bt4.title("Vice Chancellor")
    tops=Frame(bt4,width=1600,height=200,bg="white")
    tops.pack(side=TOP)
    tops1=Frame(bt4,width=1600,height=400,bg="powder blue")
    tops1.pack(side=TOP,pady=50)
    img1=(Image.open("D:/pytthon files/tkinter/gui/priject/capture3.png"))
    img1=ImageTk.PhotoImage(img1)
    panel=Label(tops,image=img1)
    panel.pack(side=LEFT)
    img=(Image.open("D:/pytthon files/tkinter/gui/priject/capture2.png"))
    img=ImageTk.PhotoImage(img)
    panel=Label(tops1,image=img)
    panel.pack(side=LEFT)
    bt4.mainloop()
#............................................................................vicechacellor..........................................................................

#............................................................................database of students..................................................................    
def database():
    from tkinter import messagebox as mb
    import sqlite3 as s
    from PIL import ImageTk,Image
    bt0=Toplevel()
    bt0.resizable(0,0)
    bt0.configure(bg="powder blue")
    bt0.title("Student Database")
    
    img=(Image.open('D:/pytthon files/tkinter/gui/priject/rmlicon.png'))
    img=ImageTk.PhotoImage(img)
    panel=Label(bt0,image=img,bg="powder blue")
    panel.image=img
    panel.grid(row=0,column=1)
#.............................................bt1..................................................................................................

    def insert():
        from tkinter import messagebox as mb
        import sqlite3 as s
        bt1=Toplevel()
        bt1.resizable(0,0)
        bt1.configure(bg="powder blue")
        bt1.title("Registraion Form")
        img=(Image.open('D:/pytthon files/tkinter/gui/priject/capture3.png'))
        img=ImageTk.PhotoImage(img)
        panel=Label(bt1,image=img,bg="white")
        panel.image=img
        panel.grid(row=0,columnspan=2)
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
        Label(bt1,text="Student Registration Form",font=("arial" ,25,'bold','underline'),bg="powder blue").grid(row=1,columnspan=2,padx=10,pady=10)  
        Label(bt1,text="Enter Student Name .....",font="arial 15",bg="powder blue").grid(row=2,column=0,pady=10)
        Label(bt1,text="Enter Student Father's name... ",font="arial 15",bg="powder blue").grid(row=3,column=0,pady=10)
        Label(bt1,text="Enter Student Branch name...",font="arial 15",bg="powder blue").grid(row=4,column=0,pady=10)
        Label(bt1,text="Enter Student Rollno...",font="arial 15",bg="powder blue").grid(row=5,column=0,pady=10)
        Label(bt1,text="Enter Student Mobile no...",font="arial 15",bg="powder blue").grid(row=6,column=0,pady=10)
        Label(bt1,text="Enter Student Gender....",font="arial 15",bg="powder blue").grid(row=7,column=0,pady=10)
        Label(bt1,text="Enter Student year....",font="arial 15",bg="powder blue").grid(row=8,column=0,pady=10)
        txt1=Entry(bt1,bd=4)
        txt1.grid(row=2,column=1,pady=10,padx=10)
        txt2=Entry(bt1,bd=4)
        txt2.grid(row=3,column=1,pady=10,padx=10)
        txt3=Entry(bt1,bd=4)
        txt3.grid(row=4,column=1,pady=10,padx=10)
        txt4=Entry(bt1,bd=4)
        txt4.grid(row=5,column=1,pady=10,padx=10)
        txt5=Entry(bt1,bd=4)
        txt5.grid(row=6,column=1,pady=10,padx=10)
        txt6=Entry(bt1,bd=4)
        txt6.grid(row=7,column=1,pady=10,padx=10)
        txt7=Entry(bt1,bd=4)
        txt7.grid(row=8,column=1,pady=10,padx=10)
        bt=Button(bt1,text="Insert Record",font=("arial",15,'bold'),command=insertrecord,width=20,bd=10,bg="steel blue")
        bt.grid(row=9,columnspan=2,pady=10)
        Label(bt1,text="NOTE-: RECORD SHOULD BE ENTER IN UPPERCASE CHARACTER........",font="arial 15",bg="powder blue").grid(row=10,column=0,pady=10)
        bt1.mainloop()

#.................................................................................bt2..............................................................................

    def show():
        import sqlite3 as s
        bt2=Toplevel()
        bt2.resizable(0,0)
        bt2.configure(bg="HotPink4")
        bt2.title("Student Database record")
        img=(Image.open('D:/pytthon files/tkinter/gui/priject/rmlicon.png'))
        img=ImageTk.PhotoImage(img)
        panel=Label(bt2,image=img,bg="hot pink4")
        panel.image=img
        panel.pack(side=TOP)
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
            Label(bt2,text="Mechenical Engineering",font=("arial" ,30,'bold','underline'),bg="steel blue").pack(side=TOP)
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
            Label(bt3,text="Information and Technology",font=("arial" ,30,'bold','underline'),bg="steel blue").pack(side=TOP)
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
            Label(bt4,text="Electronic and Communication Engineering",font=("arial" ,30,'bold','underline'),bg="steel blue").pack(side=TOP)
            Label(bt4,text="Student Information",font=("arial" ,30,'bold','underline'),bg="steel blue").pack(side=TOP)
            top=Frame(bt4,width=100,height=100)
            top.pack(side=TOP,padx=30,pady=30)
            top1=Frame(bt4,width=100,height=300)
            top1.pack(side=RIGHT,padx=30,pady=30)
            scrollbar = Scrollbar(top,bg="red")
            scrollbar.pack( side = RIGHT, fill = Y)

            mylist = Listbox(top, yscrollcommand = scrollbar.set,width=100,height=30 )
            con=s.connect('D:/pytthon files/tkinter/gui/priject/information.db')
            rs=con.execute('Select * from info where branch="ECE"')
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
        bt1=Button(top,text="Computer Science",font=("Segoe Print" ,20,'bold','underline'),bg="HotPink3",bd=10,command=cse)
        bt1.grid(row=0,column=0)
        bt2=Button(top,text="Mechenical",font=("Segoe Print" ,20,'bold','underline'),bg="HotPink3",bd=10,command=me)
        bt2.grid(row=0,column=1)
        bt3=Button(top,text="Information Technology",font=("Segoe Print" ,20,'bold','underline'),bg="HotPink3",bd=10,command=it)
        bt3.grid(row=0,column=2)
        bt4=Button(top,text="Electronics and Communication",font=("Segoe Print" ,20,'bold','underline'),bg="HotPink3",bd=10,command=ece)
        bt4.grid(row=0,column=3)
        #Label(top,text="Thanks for visit").grid(row=1,columnspan=4)

#..............................................................................END................................................................................
   
    Label(bt0,text="....Student Information Details....",font=("Segoe Print" ,25,'bold','underline'),bg="powder blue").grid(row=1,column=1)
    bt1=Button(bt0,text="Regitraion",font=("arial" ,20, 'bold','italic'),bd=10,command=insert,bg="steel blue")
    bt1.grid(row=2,columnspan=2,pady=25)

    bt2=Button(bt0,text="Information",font=("arial" ,20, 'bold','italic'),bd=10,command=show,bg="steel blue")
    bt2.grid(row=3,columnspan=2,pady=25)


       
   
#......................................................................database of students.........................................................................    
                                                          
#..................................................................courses of iet...................................................................................
def course():
    from PIL import ImageTk,Image
    bt2=Toplevel()
    bt2.geometry("1350x800+0+0")
    bt2.configure(bg="white")
    tops=Frame(bt2,width=1350,height=200)
    tops.pack(side=TOP)
    img=(Image.open('D:/pytthon files/tkinter/gui/priject/rmlicon.png'))
    img=ImageTk.PhotoImage(img)
    panel=Label(tops,image=img,bg="white")
    panel.image=img
    panel.grid(row=0,column=1)
    Label(tops,text="INSTITUTE OF ENGINEERING AND TECHNOLOGY",font=('arial' ,20, 'bold'),fg="midnight blue",bg="white").grid(row=1,column=1)
    tops=Frame(bt2,width=800,height=600,bg="white")
    tops.pack(side=LEFT)
    tops1=Frame(bt2,width=800,height=600,bg="white")
    tops1.pack(side=RIGHT)
    Label(tops,text="UNDERGRADUATE (B.tech)",font=("Segoe Print", 20,"bold",'italic','underline'),bg="white").grid(row=0,columnspan=4)
    Label(tops,text="Sno.",font=("arial" ,20,'bold','underline')).grid(row=1,column=0,pady=10)
    Label(tops,text="COURSES",font=("arial" ,20,'bold','underline')).grid(row=1,column=1,padx=10,pady=10)
    Label(tops,text="SEAT",font=("arial" ,20,'bold','underline')).grid(row=1,column=2,padx=10,pady=10)
    Label(tops,text="ELIGIBILITY",font=("arial" ,20,'bold','underline')).grid(row=1,column=3,padx=10,pady=10)
    Label(tops,text="1",font=("arial" ,20,'bold','underline')).grid(row=2,column=0,padx=20,pady=20)
    Label(tops,text="2.",font=("arial" ,20,'bold','underline')).grid(row=3,column=0,padx=20,pady=20)
    Label(tops,text="3.",font=("arial" ,20,'bold','underline')).grid(row=4,column=0,padx=20,pady=20)
    Label(tops,text="4",font=("arial" ,20,'bold','underline')).grid(row=5,column=0,padx=20,pady=20)

    Label(tops,text="CSE",font=("arial" ,20,'bold','underline')).grid(row=2,column=1)
    Label(tops,text="IT.",font=("arial" ,20,'bold','underline')).grid(row=3,column=1)
    Label(tops,text="ME",font=("arial" ,20,'bold','underline')).grid(row=4,column=1)
    Label(tops,text="ECE",font=("arial" ,20,'bold','underline')).grid(row=5,column=1)

    Label(tops,text="60",font=("arial" ,20,'bold','underline')).grid(row=2,column=2)
    Label(tops,text="60",font=("arial" ,20,'bold','underline')).grid(row=3,column=2)
    Label(tops,text="60",font=("arial" ,20,'bold','underline')).grid(row=4,column=2)
    Label(tops,text="60",font=("arial" ,20,'bold','underline')).grid(row=5,column=2)

    Label(tops,text="AKTU",font=("arial" ,20,'bold','underline')).grid(row=2,column=3)
    Label(tops,text="AKTU",font=("arial" ,20,'bold','underline')).grid(row=3,column=3)
    Label(tops,text="AKTU",font=("arial" ,20,'bold','underline')).grid(row=4,column=3)
    Label(tops,text="AKTU",font=("arial" ,20,'bold','underline')).grid(row=5,column=3)

    Label(tops1,text="POST GRADUATE (M.tech)",font=("Segoe Print", 20,"bold",'italic','underline'),bg="white").grid(row=0,columnspan=4,padx=20)
    Label(tops1,text="Sno.",font=("arial" ,20,'bold','underline')).grid(row=1,column=0,pady=10)
    Label(tops1,text="COURSES",font=("arial" ,20,'bold','underline')).grid(row=1,column=1,padx=10,pady=10)
    Label(tops1,text="SEAT",font=("arial" ,20,'bold','underline')).grid(row=1,column=2,padx=10,pady=10)
    Label(tops1,text="ELIGIBILITY",font=("arial" ,20,'bold','underline')).grid(row=1,column=3,padx=10,pady=10)

    Label(tops1,text="1",font=("arial" ,20,'bold','underline')).grid(row=2,column=0,padx=20,pady=20)
    Label(tops1,text="2.",font=("arial" ,20,'bold','underline')).grid(row=3,column=0,padx=20,pady=20)
    Label(tops1,text="3.",font=("arial" ,20,'bold','underline')).grid(row=4,column=0,padx=20,pady=20)
    Label(tops1,text="4",font=("arial" ,20,'bold','underline')).grid(row=5,column=0,padx=20,pady=20)

    Label(tops1,text="CSE",font=("arial" ,20,'bold','underline')).grid(row=2,column=1)
    Label(tops1,text="IT.",font=("arial" ,20,'bold','underline')).grid(row=3,column=1)
    Label(tops1,text="ME",font=("arial" ,20,'bold','underline')).grid(row=4,column=1)
    Label(tops1,text="ECE",font=("arial" ,20,'bold','underline')).grid(row=5,column=1)

    Label(tops1,text="30",font=("arial" ,20,'bold','underline')).grid(row=2,column=2)
    Label(tops1,text="30",font=("arial" ,20,'bold','underline')).grid(row=3,column=2)
    Label(tops1,text="30",font=("arial" ,20,'bold','underline')).grid(row=4,column=2)
    Label(tops1,text="30",font=("arial" ,20,'bold','underline')).grid(row=5,column=2)

    Label(tops1,text="AKTU",font=("arial" ,20,'bold','underline')).grid(row=2,column=3)
    Label(tops1,text="AKTU",font=("arial" ,20,'bold','underline')).grid(row=3,column=3)
    Label(tops1,text="AKTU",font=("arial" ,20,'bold','underline')).grid(row=4,column=3)
    Label(tops1,text="AKTU",font=("arial" ,20,'bold','underline')).grid(row=5,column=3)


#..............................................................................courses..........................................................................

#..........................................................................faculty..............................................................................

def faculty():
    from PIL import ImageTk,Image
    import random
    import time;
    bt5=Tk()
    bt5.geometry("1350x800+0+0")
    bt5.configure(bg="steel blue")
    bt5.title("head faculty of college")


    Label(bt5,text="INSTITUTE OF ENGINEERING AND TECHNOLOGY",font=('Segoe Print' ,25, 'bold','underline'),fg="midnight blue",bg="steel blue").pack(side=TOP)
    Label(bt5,text="AYODHYA UP",font=('Segoe Print' ,20, 'bold','underline'),fg="midnight blue",bg="steel blue").pack(side=TOP)
    f1=Frame(bt5,width=1400,height=50,bg="steel blue")
    f1.pack(side=BOTTOM)
    f2=Frame(bt5,width=1400,height=50,bg="steel blue")
    f2.pack(side=BOTTOM)


    Label(bt5,text="**Head Faculty Profile**",font=('arial' ,30, 'bold','underline','italic'),bg="steel blue",fg="midnight blue").pack(side=TOP)

    tops=Frame(bt5,width="1400",height="700",bg="steel blue")
    tops.pack(side=LEFT)
    Label(tops,text="...Computer Science and Engineering...",font=('Segoe Print' ,20, 'bold','italic','underline'),bg="steel blue").grid(row=0,column=1,padx=20)



    Label(tops,text="ER Chandan Kumar",font=('arial' ,15, 'bold'),bg="steel blue").grid(row=1,column=0,padx=20,pady=20)
    Label(tops,text="chandankumar@rmlau.ac.in",font=('arial' ,15, 'bold'),bg="steel blue").grid(row=1,column=1,padx=20,pady=20)
    Label(tops,text="094157819963",font=('arial' ,15, 'bold'),bg="steel blue").grid(row=1,column=2,padx=20,pady=20)

    Label(tops,text="...Mechanical Engineering...",font=('Segoe Print' ,20, 'bold','italic','underline'),bg="steel blue").grid(row=2,column=1,padx=20)

    Label(tops,text="Er Umesh Chandra Verma",font=('arial' ,15, 'bold'),bg="steel blue").grid(row=3,column=0,padx=20,pady=20)
    Label(tops,text="uc4635@gmail.com",font=('arial' ,15, 'bold'),bg="steel blue").grid(row=3,column=1,padx=20,pady=20)
    Label(tops,text="09415596253",font=('arial' ,15, 'bold'),bg="steel blue").grid(row=3,column=2,padx=20,pady=20)

    Label(tops,text="...Information and Technology...",font=('Segoe Print' ,20, 'bold','italic','underline'),bg="steel blue").grid(row=4,column=1,padx=20)

    Label(tops,text="Er Praveen Mishra",font=('arial' ,15, 'bold'),bg="steel blue").grid(row=5,column=0,padx=20,pady=20)
    Label(tops,text="praveen12march@hmail.com",font=('arial' ,15, 'bold'),bg="steel blue").grid(row=5,column=1,padx=20,pady=20)
    Label(tops,text="09369798868",font=('arial' ,15, 'bold'),bg="steel blue").grid(row=5,column=2,padx=20,pady=20)

    Label(tops,text="...Electronics and Communication Enginieering...",font=('Segoe Print' ,20,'bold','italic','underline'),bg="steel blue").grid(row=6,column=1,padx=20)
    Label(tops,text="Er Praveen Mishra",font=('arial' ,15, 'bold'),bg="steel blue").grid(row=7,column=0,padx=20,pady=20)
    Label(tops,text="praveen12march@hmail.com",font=('arial' ,15, 'bold'),bg="steel blue").grid(row=7,column=1,padx=20,pady=20)
    Label(tops,text="09369798868",font=('arial' ,15, 'bold'),bg="steel blue").grid(row=7,column=2,padx=20,pady=20)
#...................................................................faculty.......................................................................................    
#..............................................................magic......................................................................................
def magic():
    #import random
    from PIL import ImageTk,Image
    bt6=Toplevel()
    import random
    bt6.title("Catch me MaGic")
    bt6.geometry("1350x800+0+0")
    bt6.configure(bg="white")
    def pp():
        from PIL import ImageTk,Image
        la=Toplevel()
        la.geometry("1350x800")
        la.title("About Application")
        la.configure(bg="steel blue")
        img=(Image.open("D:/pytthon files/tkinter/gui/priject/capture3.png"))
        img=ImageTk.PhotoImage(img)
        panel=Label(la,image=img,bg="steel blue")
        panel.image=img
        panel.grid(row=0,column=1,pady=10)
        img=(Image.open("D:/pytthon files/tkinter/gui/priject/python.jpg"))
        img=ImageTk.PhotoImage(img)
        panel=Label(la,image=img,bg="steel blue")
        panel.image=img
        panel.grid(row=1,column=0,padx=10)
        img=(Image.open("D:/pytthon files/tkinter/gui/priject/python2.jpg"))
        img=ImageTk.PhotoImage(img)
        panel=Label(la,image=img,bg="steel blue")
        panel.image=img
        panel.grid(row=1,column=2,padx=10)
        img=(Image.open("D:/pytthon files/tkinter/gui/priject/satyam.jpg"))
        img=ImageTk.PhotoImage(img)
        panel=Label(la,image=img,bg="steel blue")
        panel.image=img
        panel.grid(rowspan=5,column=0,padx=10)
        Label(la,text="This is a GUI Application based on Python3",font=("Segoe Print",25,'bold','underline'),bg="steel blue").grid(row=1,column=1,pady=30,padx=20)
        Label(la,text="This Application is developed by",font=("Segoe Print",25,'bold','underline'),bg="steel blue").grid(row=2,column=1,pady=30,padx=20)
        Label(la,text="Satyam Shukla",font=("Segoe Print",25,'bold','underline'),bg="steel blue").grid(row=3,column=1,pady=10,padx=10)
        Label(la,text="Computer Science Student of",font=("Segoe Print",20,'bold','underline'),bg="steel blue").grid(row=4,column=1,pady=10,padx=10)
        Label(la,text="Institute of Engineering and Technology Ayodhya up",font=("Segoe Print",20,'bold','underline'),bg="steel blue").grid(row=5,column=1,pady=10,padx=20)

         
    def move(event):
        global stopm
        if not stopm:
            a=random.randint(10,1200)
            b=random.randint(10,600)
            la.place(x=a,y=b)
        stopm=False
    def stopmove(event):
        if event.char=='s':
            global stopm
            stopm=True

    Label(bt6,text="...If you want see about Application...",font=("segoe Print",25,'bold','underline'),bg="white",fg="midnight blue").pack(side=TOP,pady=10)
    Label(bt6,text="...Press the Button given below...",font=("Segoe Print",25,'bold','underline'),bg="white",fg="midnight blue").pack(side=TOP,pady=10)
    img=(Image.open("D:/pytthon files/tkinter/gui/priject/its.jpg"))

    img=ImageTk.PhotoImage(img)
    panel=Label(bt6,image=img,bg="white")
    panel.image=img
    panel.pack(side=LEFT,padx=20,pady=10)
                                                     
    la=Button(bt6,text="Catch Me",font=("Segoe Print",15,'bold','italic'),fg="midnight blue",command=pp,bg="steel blue",bd=8)
    la.place(x=200,y=100)
    la.bind('<Enter>',move)
    bt6.bind('<Key>',stopmove)
    bt6.mainloop

#.........................................................................................magic..................................................................    
#def move(event):
   # place(x=event.x,y=event.y)

    
menubar=Menu(root,bg="steel blue")
root.config(menu=menubar)
filemenu=Menu(menubar)
menubar.add_cascade(label="File",menu=filemenu)
tops=Frame(root,width=1600,height=200,bg="Hot Pink4")
tops.pack(side=TOP)
img=(Image.open("D:/pytthon files/tkinter/gui/priject/rmlicon.png"))
img=ImageTk.PhotoImage(img)
panel=Label(tops,image=img)
panel.grid(row=0,column=1)
Label(tops,text="INSTITUTE OF ENGINEERING AND TECHNOLOGY",font=('arial' ,20, 'bold'),fg="midnight blue").grid(row=1,column=1)
img2=(Image.open("D:/pytthon files/tkinter/gui/priject/rml1.jpg"))
img2=ImageTk.PhotoImage(img2)
panel2=Label(root,image=img2)
panel2.pack(side=TOP)
tops1=Frame(root,width=1600,height=50)
tops1.pack(side=TOP)
bt0=Button(tops1,padx=5,pady=5,bd=2 , fg="black" ,font=('arial' ,20,'bold'), text="Students Database",bg="HotPink4",command=database).grid(row=0,column=0)
bt2=Button(tops1,padx=60,pady=5,bd=2 , fg="black" ,font=('arial' ,20,'bold'), text="Courses",bg="Hot Pink4",command=course).grid(row=0,column=1)
bt3=Button(tops1,padx=5,pady=5,bd=2 , fg="black" ,font=('arial' ,20,'bold'), text="Director",bg="Hot Pink4",command=director).grid(row=0,column=2)
bt4=Button(tops1,padx=5,pady=5,bd=2 , fg="black" ,font=('arial' ,20,'bold'), text="Vice Chancellor",bg="Hot Pink4",command=vice).grid(row=0,column=3)
bt5=Button(tops1,padx=5,pady=5,bd=2 , fg="black" ,font=('arial' ,20,'bold'), text="Faculty Member",bg="Hot Pink4",command=faculty).grid(row=0,column=4)
bt6=Button(tops1,padx=5,pady=5,bd=2 , fg="black" ,font=('arial' ,20,'bold'), text="Magic View  ",bg="Hot Pink4",command=magic).grid(row=0,column=5)
#la=Label(root,text="Satyam Shukla")
#root.bind('<Motion>',move)
         

tops2=Frame(root,width=1600,height=50,bg="powder blue")
tops2.pack(side=TOP)
root.mainloop()
