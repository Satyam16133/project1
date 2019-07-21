from tkinter import *
from PIL import ImageTk,Image
import random
import time;
def showinfo():
    # global bt4
    bt4=Tk()
    bt4.geometry("1600x800")
    bt4.configure(bg="white")
    tops=Frame(bt4,width=1600,height=200,bg="white")
    tops.pack(side=TOP)
    tops1=Frame(bt4,width=1600,height=400,bg="powder blue")
    tops1.pack(side=TOP,pady=50)
    img1=(Image.open("D:/pytthon files/tkinter/gui/priject/capture3.png"))
    img1=ImageTk.PhotoImage(img1)
    panel=Label(tops,image=img1)
    panel.pack(side=LEFT)
    #@3global img
    img=(Image.open("D:/pytthon files/tkinter/gui/priject/capture2.png"))
    img=ImageTk.PhotoImage(img)
    panel=Label(tops1,image=img)
    panel.pack(side=LEFT)
    bt4.mainloop()
showinfo()
