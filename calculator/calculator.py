"""
Date: 03.08.2023 -- day/month/year
Author: Sunnatjon Arslonov
Program name: Calculator
"""

from tkinter import *
import math

tk = Tk()
tk.configure(bg="black")
tk.title("Calculator")
tk.geometry("320x600")


def clear():
 inputt.delete(0,END)
 results.config(text="")
def foiz():
 inputt.insert(len(inputt.get()),"%")
def division():
 inputt.insert(len(inputt.get()),"/")
def num7():
 inputt.insert(len(inputt.get()),"7")
def num8():
 inputt.insert(len(inputt.get()),"8")
def num9():
 inputt.insert(len(inputt.get()),"9")
def kop():
 inputt.insert(len(inputt.get()),"*")
def num4():
 inputt.insert(len(inputt.get()),"4")
def num5():
 inputt.insert(len(inputt.get()),"5")
def num6():
 inputt.insert(len(inputt.get()),"6")
def minus():
 inputt.insert(len(inputt.get()),"-")
def num1():
 inputt.insert(len(inputt.get()),"1")
def num2():
 inputt.insert(len(inputt.get()),"2")
def num3():
 inputt.insert(len(inputt.get()),"3")
def plus():
 inputt.insert(len(inputt.get()),"+")
def lqavs():
 inputt.insert(len(inputt.get()),"(")
def zero():
 inputt.insert(len(inputt.get()),"0")
def rqavs():
 inputt.insert(len(inputt.get()),")")
def equal():
 hisob = inputt.get()
 results.config(text=eval(hisob)) 

results= Label(text="",font="Arial 20",width="10",bg="black",fg="#00FF00")
results.place(relx=0.2,rely=0.05)


inputt = Entry(font="Arial 15")
inputt.place(relx=0.01,rely=0.15,width="300",height='175')


c_btn = Button(text="C",width="5",height="2",fg="red",bg="#28231d",command=clear)
c_btn.place(relx=0.02,rely=0.5)

qavs_btn = Button(text="+/-",width="5",height="2",fg="limegreen",bg="#28231d")
qavs_btn.place(relx=0.27,rely=0.5)

foiz_btn = Button(text="%",width="5",height="2",fg="limegreen",bg="#28231d",command=foiz)
foiz_btn.place(relx=0.52,rely=0.5)

div_btn = Button(text="÷",width="5",height="2",fg="limegreen",bg="#28231d",command=division)
div_btn.place(relx=0.77,rely=0.5)


num7_btn = Button(text="7",width="5",height="2",fg="limegreen",bg="#28231d",command=num7)
num7_btn.place(relx=0.02,rely=0.6)

num8_btn = Button(text="8",width="5",height="2",fg="limegreen",bg="#28231d",command=num8)
num8_btn.place(relx=0.27,rely=0.6)

num9_btn = Button(text="9",width="5",height="2",fg="limegreen",bg="#28231d",command=num9)
num9_btn.place(relx=0.52,rely=0.6)

kop_btn = Button(text="x",width="5",height="2",fg="limegreen",bg="#28231d",command=kop)
kop_btn.place(relx=0.77,rely=0.6)


num4_btn = Button(text="4",width="5",height="2",fg="limegreen",bg="#28231d",command=num4)
num4_btn.place(relx=0.02,rely=0.7)

num5_btn = Button(text="5",width="5",height="2",fg="limegreen",bg="#28231d",command=num5)
num5_btn.place(relx=0.27,rely=0.7)

num6_btn = Button(text="6",width="5",height="2",fg="limegreen",bg="#28231d",command=num6)
num6_btn.place(relx=0.52,rely=0.7)

minus_btn = Button(text="--",width="5",height="2",fg="limegreen",bg="#28231d",command=minus)
minus_btn.place(relx=0.77,rely=0.7)


num1_btn = Button(text="1",width="5",height="2",fg="limegreen",bg="#28231d",command=num1)
num1_btn.place(relx=0.02,rely=0.8)

num2_btn = Button(text="2",width="5",height="2",fg="limegreen",bg="#28231d",command=num2)
num2_btn.place(relx=0.27,rely=0.8)

num3_btn = Button(text="3",width="5",height="2",fg="limegreen",bg="#28231d",command=num3)
num3_btn.place(relx=0.52,rely=0.8)

plus_btn = Button(text="+",width="5",height="2",fg="limegreen",bg="#28231d",command=plus)
plus_btn.place(relx=0.77,rely=0.8)



rqavs_btn = Button(text="(",width="5",height="2",fg="limegreen",bg="#28231d",command=lqavs)
rqavs_btn.place(relx=0.02,rely=0.9)

zero_btn = Button(text="0",width="5",height="2",fg="limegreen",bg="#28231d",command=zero)
zero_btn.place(relx=0.27,rely=0.9)

lqavs_btn = Button(text=")",width="5",height="2",fg="limegreen",bg="#28231d",command=rqavs)
lqavs_btn.place(relx=0.52,rely=0.9)

equal_btn = Button(text="=",width="5",height="2",fg="white",bg="limegreen",command=equal)
equal_btn.place(relx=0.77,rely=0.9)

tk.mainloop()
