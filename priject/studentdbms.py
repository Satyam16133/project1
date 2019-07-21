from tkinter import *
from tkinter import messagebox as mb
import sqlite3 as s
root=Tk()
root.resizable(0,0)
root.geometry("300x300")
root.configure(bg="pink")
def insertrecord():
    
    con=s.connect('D:/pytthon files/tkinter/gui/priject/information.db')
    con.execute('create table info(name varchar(20),father varchar(20),branch varchar(20),rollno varchar(20),mobile varchar(20),gender varchar(10),year int)')
    con.commit()
    mb.showinfo("message","tabel created")

bt=Button(root,text="Insert record",command=insertrecord)
bt.grid(row=4,columnspan=2,pady=10)
root.mainloop()
