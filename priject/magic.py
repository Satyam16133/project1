from tkinter import *
import random
from PIL import ImageTk,Image
bt6=Tk()
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
    
stopm=False
def move(event):
    global stopm
    if not stopm:
        a=random.randint(10,1200)
        b=random.randint(10,600)
        la.place(x=a,y=b)
    stopm=False
def stopmove(event):
    if event.char=='a':
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
