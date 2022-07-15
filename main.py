from sre_parse import State
from  tkinter import *

#Initializes the tkinter window
root = Tk()



#writes a thing on screen 
words = Label(root, text="Hello")
words1 = Label(root, text="Nigga")

#packs the var so that it shows up on the screen
#words.pack()


#GRID - REQUIRES TWO VALUES FOR ROWS AND COLUMNS TO PLACE IN A DEFINITE PLACE
#words.grid(row=0, column=0)
#words1.grid(row=1, column=0)


#Entry or Typing handles
e = Entry(borderwidth=2, width=50)
e.pack()
e.insert(0, "Enter Your Name : ")




#Function for Button
#.get helps to extract info from a form or entry
def click_me():
    my_label = Label(root, text= f"Hello, {e.get()}")
    my_label.pack()

#Labels Button and text    ----------- PADX changes X while PADY changes Y (PADDING)
#command helps to insert FUNCTION to a button
my_button = Button(root, text="Click Me!", command=click_me, fg="green", bg="grey")
#Adds button as a labelcd
my_button.pack()








#Executes and shows the window
root.mainloop()
