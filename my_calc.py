from tkinter import *

#Initialize
root = Tk()
root.title("Calculator")

#Title Calculator
title_calc = Label(root, text="CALCULATOR")
#title_calc.grid(row=0, column=0)





#entryy
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4)



def on_click(number):
    e.insert("end",  number)

def clear_b():
    e.delete(0, END)

def add_sign():
    global f_num 
    global sign_ok
    f_num = float(e.get())
    sign_ok = "add"
    e.delete(0, END)

def sub_sign():
    global f_num 
    global sign_ok
    f_num = float(e.get())
    sign_ok = "subt"
    e.delete(0, END)


def multi_sign():
    global f_num 
    global sign_ok
    f_num = float(e.get())
    sign_ok = "multi"
    e.delete(0, END)


def div_sign():
    global f_num 
    global sign_ok
    f_num = float(e.get())
    sign_ok = "div"
    e.delete(0, END)


def dec_sign():
    pass

def on_enter():
    second_number = float(e.get())
    print(f_num)
    print(second_number)
    global sign_ok
    e.delete(0, END)
    if sign_ok == "add":
        e.insert(0, float(f_num  + second_number))
    elif sign_ok == "subt":
        e.insert(0, float(f_num  - second_number))
    elif sign_ok == "multi":
        e.insert(0, float(f_num  * second_number))
    elif sign_ok == "div":
        e.insert(0, float(f_num  / second_number))
    



button_7 = Button(root, text="7" ,padx=20, pady=20, command= lambda : on_click(7)).grid(row=1, column=0)
button_8 = Button(root, text="8", padx=20, pady=20, command= lambda : on_click(8)).grid(row=1, column=1)
button_9 = Button(root, text="9", padx=20, pady=20, command= lambda : on_click(9)).grid(row=1, column=2)
button_4 = Button(root, text="4", padx=20, pady=20, command= lambda : on_click(4)).grid(row=2, column=0)
button_5 = Button(root, text="5", padx=20, pady=20, command= lambda : on_click(5)).grid(row=2, column=1)
button_6 = Button(root, text="6", padx=20, pady=20, command= lambda : on_click(6)).grid(row=2, column=2)
button_1 = Button(root, text="1", padx=20, pady=20, command= lambda : on_click(1)).grid(row=3, column=0)
button_2 = Button(root, text="2", padx=20, pady=20, command= lambda : on_click(2)).grid(row=3, column=1)
button_3 = Button(root, text="3", padx=20, pady=20, command= lambda : on_click(3)).grid(row=3, column=2)
button_0 = Button(root, text="0", padx=20, pady=20, command= lambda : on_click(0)).grid(row=4, column=0)



button_add = Button(root, text="+", padx=20, pady=20, command=add_sign).grid(row=1, column=3)
button_sub = Button(root, text="-", padx=20, pady=20, command=sub_sign).grid(row=2, column=3)
button_multi = Button(root, text="*", padx=20, pady=20, command=multi_sign).grid(row=3, column=3)
button_decimal = Button(root, text=".", padx=20, pady=20, state=DISABLED).grid(row=4, column=1)
button_div = Button(root, text="/", padx=20, pady=20, command=div_sign).grid(row=4, column=2)
button_equals = Button(root, text="=", padx=20, pady=20, command=on_enter).grid(row=4, column=3)
button_clear = Button(root, text="Clear", padx=90, pady=10, command=clear_b).grid(row=5, column=0, columnspan=4)

root.mainloop()
