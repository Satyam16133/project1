from tkinter import *
from PIL import ImageTk,Image
import random
import time;
root=Tk()
root.geometry("1600x800+0+0")
root.configure(bg="slate blue")
tops=Frame(root,width=1600,height=200,bg="Hot Pink4")
tops.pack(side=TOP)
img=(Image.open("D:/pytthon files/tkinter/gui/priject/rmlicon.png"))
img=ImageTk.PhotoImage(img)
panel=Label(tops,image=img,bg="slate blue")
panel.grid(row=0,column=1)
Label(tops,text="INSTITUTE OF ENGINEERING AND TECHNOLOGY",font=('arial' ,20, 'bold'),bg="slate blue").grid(row=1,column=1)
tops=Frame(root,width=800,height=600,bg="Hot Pink4")
tops.pack(side=LEFT)
tops1=Frame(root,width=800,height=600,bg="Hot Pink4")
tops1.pack(side=RIGHT)
Label(tops,text="UNDERGRADUATE",font=("arial", 20,"bold",'italic','underline'),bg="royal blue").grid(row=0,columnspan=4)
Label(tops,text="Sno.",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=1,column=0,pady=10)
Label(tops,text="COURSES",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=1,column=1,padx=10,pady=10)
Label(tops,text="SEAT",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=1,column=2,padx=10,pady=10)
Label(tops,text="ELIGIBILITY",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=1,column=3,padx=10,pady=10)
Label(tops,text="1",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=2,column=0,padx=20,pady=20)
Label(tops,text="2.",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=3,column=0,padx=20,pady=20)
Label(tops,text="3.",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=4,column=0,padx=20,pady=20)
Label(tops,text="4",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=5,column=0,padx=20,pady=20)

Label(tops,text="CSE",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=2,column=1)
Label(tops,text="IT.",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=3,column=1)
Label(tops,text="ME",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=4,column=1)
Label(tops,text="ECE",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=5,column=1)

Label(tops,text="60",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=2,column=2)
Label(tops,text="60",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=3,column=2)
Label(tops,text="60",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=4,column=2)
Label(tops,text="60",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=5,column=2)

Label(tops,text="AKTU",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=2,column=3)
Label(tops,text="AKTU",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=3,column=3)
Label(tops,text="AKTU",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=4,column=3)
Label(tops,text="AKTU",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=5,column=3)

Label(tops1,text="POST GRADUATE",font=("arial", 20,"bold",'italic','underline'),bg="royal blue").grid(row=0,columnspan=4,padx=20)
Label(tops1,text="Sno.",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=1,column=0,pady=10)
Label(tops1,text="COURSES",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=1,column=1,padx=10,pady=10)
Label(tops1,text="SEAT",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=1,column=2,padx=10,pady=10)
Label(tops1,text="ELIGIBILITY",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=1,column=3,padx=10,pady=10)

Label(tops1,text="1",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=2,column=0,padx=20,pady=20)
Label(tops1,text="2.",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=3,column=0,padx=20,pady=20)
Label(tops1,text="3.",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=4,column=0,padx=20,pady=20)
Label(tops1,text="4",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=5,column=0,padx=20,pady=20)

Label(tops1,text="CSE",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=2,column=1)
Label(tops1,text="IT.",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=3,column=1)
Label(tops1,text="ME",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=4,column=1)
Label(tops1,text="ECE",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=5,column=1)

Label(tops1,text="30",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=2,column=2)
Label(tops1,text="30",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=3,column=2)
Label(tops1,text="30",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=4,column=2)
Label(tops1,text="30",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=5,column=2)

Label(tops1,text="AKTU",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=2,column=3)
Label(tops1,text="AKTU",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=3,column=3)
Label(tops1,text="AKTU",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=4,column=3)
Label(tops1,text="AKTU",font=("arial" ,20,'bold','underline'),bg="royal blue").grid(row=5,column=3)





