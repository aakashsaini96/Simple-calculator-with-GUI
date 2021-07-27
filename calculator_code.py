from tkinter import *
import random

root= Tk()

root.title("Simple Calculator")
root.config(bg="#B2BABB")

#Entry field (or Output field)
e=Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#All the functions related to different button clicks
def button_click(num):
    number=e.get()+str(num)
    e.delete(0, END)
    e.insert(0, number)

def button_clear():
    e.delete(0, END)

def button_add():
    global first_num
    first_num=float(e.get())
    e.delete(0, END)
    global func
    func='+'

def button_sub():
    global first_num
    first_num=float(e.get())
    e.delete(0, END)
    global func
    func='-'

def button_multiply():
    global first_num
    first_num=float(e.get())
    e.delete(0, END)
    global func
    func='*'

def button_divide():
    global first_num
    first_num=float(e.get())
    e.delete(0, END)
    global func
    func='/'

def button_equal():
    second_num=float(e.get())
    e.delete(0, END)
    if func=='+':
        ans=first_num+second_num
        e.insert(0, str(ans))
    elif func=='-':
        ans=first_num-second_num
        e.insert(0, str(ans))
    elif func=='*':
        ans=first_num*second_num
        e.insert(0, str(ans))
    else:
        ans=first_num/second_num
        e.insert(0, str(ans))


#creating all the buttons
button_1=Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2=Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3=Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4=Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5=Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6=Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7=Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8=Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9=Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0=Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_plus=Button(root, text="+", padx=39, pady=20, bg="#D5D8DC", command=button_add)
button_clr=Button(root, text="CLR", padx=82, pady=20, command=button_clear)
button_minus=Button(root, text="-", padx=41, pady=20, bg="#D5D8DC", command=button_sub)
button_mul=Button(root, text="*", padx=41, pady=20, bg="#D5D8DC", command=button_multiply)
button_div=Button(root, text="/", padx=41, pady=20, bg="#D5D8DC", command=button_divide)
button_eq=Button(root, text="=", padx=88, pady=20, bg="#AED6F1", command=button_equal)


#Add the buttons to root
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_clr.grid(row=4, column=1, columnspan=2)
button_eq.grid(row=5, column=1, columnspan=2)
button_plus.grid(row=5, column=0)
button_minus.grid(row=6, column=0)
button_mul.grid(row=6, column=1)
button_div.grid(row=6, column=2)


root.mainloop()
