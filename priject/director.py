from tkinter import *
from PIL import ImageTk,Image
bt3=Tk()
bt3.geometry("1600x800+0+0")
bt3.configure(bg="Hot Pink3")
bt3.title("Director Table")
tops=Frame(bt3,width=1600,height=200,bg="Hot Pink3")
tops.pack(side=TOP)
img=(Image.open("D:/pytthon files/tkinter/gui/priject/rmlicon.png"))
img=ImageTk.PhotoImage(img)
panel=Label(tops,image=img,bg="Hot Pink3")
panel.grid(row=0,column=1)
Label(tops,text="INSTITUTE OF ENGINEERING AND TECHNOLOGY",font=('arial' ,20, 'bold'),bg="Hot Pink3").grid(row=1,column=1)
tops1=Frame(bt3,width=300,height=300,bg="powder blue")
tops1.pack(side=LEFT)
img1=(Image.open("D:/pytthon files/tkinter/gui/priject/rmldirector.jpg"))
img1=ImageTk.PhotoImage(img1)
panel=Label(tops1,image=img1)
panel.grid(row=0,column=1)
tops2=Frame(bt3,width=600,height=300,bg="light green")
tops2.pack(side=RIGHT)
la=Label(tops2,text="Professor Ramapati Mishra started his career in industry by serving prestigious Indian AirForce   ",font=("arial" ,15, "bold"),bg="light green")
la.grid(row=0,column=0)

la=Label(tops2,text="in technical servicing fighter planes and its systems. Since 2001,he joined I.E.T. as Assistant in    ",font=("arial" ,15,"bold"),bg="light green")
la.grid(row=1,column=0)

la=Label(tops2,text="  Electronics And Communication branch, then rose to be come Associate Proffesor and H.O.D, in    ",font=("arial" ,15, "bold","bold"),bg="light green")
la.grid(row=2,column=0)

la=Label(tops2,text="same department. In year 2010 after compilition of hid P.hd he became director in different colleges   ",font=("arial" ,15, "bold"),bg="light green")
la.grid(row=3,column=0)

la=Label(tops2,text="in UP and Uttrakhand . After 6 years he again joined I.E.T. Since May 2018 he is leanding I.E.T.  as     ",font=("arial" ,15, "bold"),bg="light green")
la.grid(row=4,column=0)

la=Label(tops2,text="director taking I.E.T. to newer dimensions full of engineering activities this series of workshop is       ",font=("arial" ,15, "bold"),bg="light green")
la.grid(row=5,column=0)
la=Label(tops2,text="an example",font=("arial" ,15, "bold"),bg="light green")
la.grid(row=6,column=0)

                                                          





