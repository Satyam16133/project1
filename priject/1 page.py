from tkinter import *
from PIL import ImageTk,Image
import random
import time;
root=Tk()
root.geometry("1600x800+0+0")

                                                          

menubar=Menu(root,bg="red")
root.config(menu=menubar)
filemenu=Menu(menubar)
menubar.add_cascade(label="File",menu=filemenu)
tops=Frame(root,width=1600,height=200,bg="Hot Pink4")
tops.pack(side=TOP)
img=(Image.open("D:/pytthon files/tkinter/gui/priject/rmlicon.png"))
img=ImageTk.PhotoImage(img)
panel=Label(tops,image=img)
panel.grid(row=0,column=1)
Label(tops,text="INSTITUTE OF ENGINEERING AND TECHNOLOGY",font=('arial' ,20, 'bold')).grid(row=1,column=1)
img2=(Image.open("D:/pytthon files/tkinter/gui/priject/rml1.jpg"))
img2=ImageTk.PhotoImage(img2)
panel2=Label(root,image=img2)
panel2.pack(side=TOP)
tops1=Frame(root,width=1600,height=50)
tops1.pack(side=TOP)
bt1=Button(tops1,padx=5,pady=5,bd=2 , fg="black" ,font=('arial' ,20,'bold'), text="Students Database",bg="Hot Pink4").grid(row=0,column=0)
bt2=Button(tops1,padx=60,pady=5,bd=2 , fg="black" ,font=('arial' ,20,'bold'), text="Courses",bg="Hot Pink4").grid(row=0,column=1)
bt3=Button(tops1,padx=5,pady=5,bd=2 , fg="black" ,font=('arial' ,20,'bold'), text="Director",bg="Hot Pink4").grid(row=0,column=2)
bt4=Button(tops1,padx=5,pady=5,bd=2 , fg="black" ,font=('arial' ,20,'bold'), text="Vice Chancellor",bg="Hot Pink4").grid(row=0,column=3)
bt5=Button(tops1,padx=5,pady=5,bd=2 , fg="black" ,font=('arial' ,20,'bold'), text="Faculty Member",bg="Hot Pink4").grid(row=0,column=4)
bt6=Button(tops1,padx=5,pady=5,bd=2 , fg="black" ,font=('arial' ,20,'bold'), text="Campus View",bg="Hot Pink4").grid(row=0,column=5)

tops2=Frame(root,width=1600,height=50,bg="powder blue")
tops2.pack(side=TOP)
root.mainloop()
