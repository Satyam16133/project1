from tkinter import *
from PIL import ImageTk,Image
import random
import time;
root=Tk()
root.geometry("1600x800+0+0")
root.configure(bg="powder blue")


Label(root,text="INSTITUTE OF ENGINEERING AND TECHNOLOGY",font=('arial' ,20, 'bold'),fg="blue",bg="powder blue").pack(side=TOP)
Label(root,text="AYODHYA UP",font=('arial' ,20, 'bold'),fg="blue",bg="powder blue").pack(side=TOP)
f1=Frame(root,width=1400,height=100,bg="powder blue")
f1.pack(side=BOTTOM)
f2=Frame(root,width=1400,height=50,bg="powder blue")
f2.pack(side=BOTTOM)


Label(root,text="Head Faculty Profile",font=('arial' ,30, 'bold'),bg="powder blue",fg="orange").pack(side=TOP)

tops=Frame(width="1400",height="400",bg="powder blue")
tops.pack(side=LEFT)
Label(tops,text="Computer Science and Engineering",font=('arial' ,25, 'bold','italic','underline')).grid(row=0,column=1,padx=20)



Label(tops,text="ER Chandan Kumar",font=('arial' ,15, 'bold')).grid(row=1,column=0,padx=20,pady=20)
Label(tops,text="chandankumar@rmlau.ac.in",font=('arial' ,15, 'bold')).grid(row=1,column=1,padx=20,pady=20)
Label(tops,text="094157819963",font=('arial' ,15, 'bold')).grid(row=1,column=2,padx=20,pady=20)

Label(tops,text="Mechanical Engineering",font=('arial' ,25, 'bold','italic','underline')).grid(row=2,column=1,padx=20)

Label(tops,text="Er Umesh Chandra Verma",font=('arial' ,15, 'bold')).grid(row=3,column=0,padx=20,pady=20)
Label(tops,text="uc4635@gmail.com",font=('arial' ,15, 'bold')).grid(row=3,column=1,padx=20,pady=20)
Label(tops,text="09415596253",font=('arial' ,15, 'bold')).grid(row=3,column=2,padx=20,pady=20)

Label(tops,text="Information and Technology",font=('arial' ,25, 'bold','italic','underline')).grid(row=4,column=1,padx=20)

Label(tops,text="Er Praveen Mishra",font=('arial' ,15, 'bold')).grid(row=5,column=0,padx=20,pady=20)
Label(tops,text="praveen12march@hmail.com",font=('arial' ,15, 'bold')).grid(row=5,column=1,padx=20,pady=20)
Label(tops,text="09369798868",font=('arial' ,15, 'bold')).grid(row=5,column=2,padx=20,pady=20)

Label(tops,text="Electronics and Communication Enginieering",font=('arial' ,25, 'bold','italic','underline')).grid(row=6,column=1,padx=20)
Label(tops,text="Er Praveen Mishra",font=('arial' ,15, 'bold')).grid(row=7,column=0,padx=20,pady=20)
Label(tops,text="praveen12march@hmail.com",font=('arial' ,15, 'bold')).grid(row=7,column=1,padx=20,pady=20)
Label(tops,text="09369798868",font=('arial' ,15, 'bold')).grid(row=7,column=2,padx=20,pady=20)
