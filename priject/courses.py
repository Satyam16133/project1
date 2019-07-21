from tkinter import *
from PIL import ImageTk,Image
import random
import time;
root=Tk()
root.geometry("1600x800+0+0")
tops=Frame(root,width=1600,height=200,bg="powder blue")
tops.pack(side=TOP)
img=(Image.open("D:/pytthon files/tkinter/gui/priject/rmlicon.png"))
img=ImageTk.PhotoImage(img)
panel=Label(tops,image=img)
panel.grid(row=0,column=1)
Label(tops,text="INSTITUTE OF ENGINEERING AND TECHNOLOGY",font=('arial' ,20, 'bold')).grid(row=1,column=1)
