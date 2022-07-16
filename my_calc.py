from tkinter import *
from turtle import title

#Initialize
root = Tk()
root.title("Calculator")
root.iconbitmap('icon/favicon.ico')







#entryy / TOP WINDOW WHERE THE NUMBERS ARE DISPLAYEd
e = Entry(root, width=35, borderwidth=5, bg="#78b2bf")
e.grid(row=0, column=0, columnspan=4)



# -------- ALL THE NUMBERS ARE INSERTED HERE ------ 
def on_click(number):
    e.insert("end",  number)


#THE CLEAR BUTTON'S FUNTION 
def clear_b():
    e.delete(0, END)


# ------- ADDITION ---------- 
def add_sign():
    try:
        global f_num 
        global sign_ok
        f_num = float(e.get())
        sign_ok = "add"
        e.delete(0, END)
    except:
        pass

# -------- SUBTRACTION ----------
def sub_sign():
    try:
        global f_num 
        global sign_ok
        f_num = float(e.get())
        sign_ok = "subt"
        e.delete(0, END)
    except:
        pass

# --------- MULTIPLICATION -------
def multi_sign():
    try:
        global f_num 
        global sign_ok
        f_num = float(e.get())
        sign_ok = "multi"
        e.delete(0, END)
    except:
        pass

#------- DIVIDE BUTTON'S FUNTION ---------
def div_sign():
    try:
        global f_num 
        global sign_ok
        f_num = float(e.get())
        sign_ok = "div"
        e.delete(0, END)
    except:
        pass


#--------- SPACE FOR DECIMAL BUTTON --------------
def dec_sign():
    pass

#------------ TAKES THE NUMBER FROM THE SCREEN AND ADDS IT WITH THE GLOBAL VAR I.E. FIRST NUMBER ---------
def on_enter():
    try:
        second_number = float(e.get())
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
    except:
        pass
    



button_7 = Button(root, text="7" ,padx=18, pady=20, command= lambda : on_click(7)).grid(row=1, column=0)
button_8 = Button(root, text="8", padx=18, pady=20, command= lambda : on_click(8)).grid(row=1, column=1)
button_9 = Button(root, text="9", padx=18, pady=20, command= lambda : on_click(9)).grid(row=1, column=2)
button_4 = Button(root, text="4", padx=18, pady=20, command= lambda : on_click(4)).grid(row=2, column=0)
button_5 = Button(root, text="5", padx=18, pady=20, command= lambda : on_click(5)).grid(row=2, column=1)
button_6 = Button(root, text="6", padx=18, pady=20, command= lambda : on_click(6)).grid(row=2, column=2)
button_1 = Button(root, text="1", padx=18, pady=20, command= lambda : on_click(1)).grid(row=3, column=0)
button_2 = Button(root, text="2", padx=18, pady=20, command= lambda : on_click(2)).grid(row=3, column=1)
button_3 = Button(root, text="3", padx=18, pady=20, command= lambda : on_click(3)).grid(row=3, column=2)
button_0 = Button(root, text="0", padx=18, pady=20, command= lambda : on_click(0)).grid(row=4, column=0)



button_add = Button(root, text="+", padx=18, pady=20, command=add_sign).grid(row=1, column=3)
button_sub = Button(root, text="-", padx=19, pady=20, command=sub_sign).grid(row=2, column=3)
button_multi = Button(root, text="*", padx=19, pady=20, command=multi_sign).grid(row=3, column=3)

#----------------DECIMAL BUTTON STILL NOT FUNCTIONAL------------------------
button_decimal = Button(root, text="N/A", padx=12, pady=20, state=DISABLED).grid(row=4, column=1)


button_div = Button(root, text="/", padx=20, pady=20, command=div_sign).grid(row=4, column=2)
button_equals = Button(root, text="=", padx=17, pady=20, command=on_enter, bg="#41d63c").grid(row=4, column=3)
button_clear = Button(root, text="Clear", padx=90, pady=10, command=clear_b, bg="#bd3937").grid(row=5, column=0, columnspan=4)


#--------- LOCKS THE SCREEN FROM RESIZING --------
root.resizable(width=False, height=False)

#RUNS THE WINDOW
root.mainloop()
