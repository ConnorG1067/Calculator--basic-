from tkinter import* 
import tkinter as tk



root = tk.Tk()

########## Variables ##########
equation = StringVar()
expression = ""


########## Functions ##########
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def clearscreen():
    global expression
    expression = ""
    equation.set("")

def equals():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("error")
        expression.set("")


########## Tkinter Base ##########
canvas = Canvas(root, height= 400, width=300)
canvas.pack()
        
screen = Entry(root, bg='#668cff', font=18, textvariable=equation)
screen.place(relwidth=1, relheight=0.2)

clear = Button(root, font=18, text="CLEAR", command=clearscreen)
clear.place(relwidth=0.2, relheight=0.05)

############### NUMBERS ###############
oneb = Button(root, text="1", font=18, command=lambda: press(1))
oneb.place(relwidth=0.2, relheight=0.2, rely=0.2)

twob = Button(root, text="2", font=18, command=lambda: press(2))
twob.place(relwidth=0.2, relheight=0.2, relx=0.2, rely=0.2)

threeb = Button(root, text="3", font=18, command=lambda: press(3))
threeb.place(relwidth=0.2, relheight=0.2, relx=0.4, rely=0.2)

fourb = Button(root, text="4", font=18, command=lambda: press(4))
fourb.place(relwidth=0.2, relheight=0.2, rely=0.4)

fiveb = Button(root, text="5", font=18, command=lambda: press(5))
fiveb.place(relwidth=0.2, relheight=0.2, relx=0.2, rely=0.4)

sixb = Button(root, text="6", font=18, command=lambda: press(6))
sixb.place(relwidth=0.2, relheight=0.2, relx=0.4, rely=0.4)

sevenb = Button(root, text="7", font=18, command=lambda: press(7))
sevenb.place(relwidth=0.2, relheight=0.2, rely=0.6)

eightb = Button(root, text="8", font=18, command=lambda: press(8))
eightb.place(relwidth=0.2, relheight=0.2, relx=0.2, rely=0.6)

nineb = Button(root, text="9", font=18, command=lambda: press(9))
nineb.place(relwidth=0.2, relheight=0.2, relx=0.4, rely=0.6)

zerob = Button(root, text="0", font=18, command=lambda: press(0))
zerob.place(relwidth=0.2, relheight=0.2, rely=0.8)

decimalb = Button(root, text=".", font=18, command=lambda: press("."))
decimalb.place(relwidth=0.2, relheight=0.2, relx=0.2, rely=0.8)

equalsb = Button(root, text="=", font=18, command=equals)
equalsb.place(relwidth=0.2, relheight=0.2, relx=0.4, rely=0.8)


############### SYMBOLS ###############
divide = Button(root, text = "/", font = 18, command=lambda: press("/"))
divide.place(relx= 0.6, rely= 0.2, relwidth=0.4, relheight=0.2)

multi = Button(root, text = "X", font = 18, command=lambda: press("*"))
multi.place(relx= 0.6, rely= 0.4, relwidth=0.4, relheight=0.2)

sub = Button(root, text = "-", font = 18, command=lambda: press("-"))
sub.place(relx= 0.6, rely= 0.6, relwidth=0.4, relheight=0.2)

add = Button(root, text = "+", font = 18, command=lambda: press("+"))
add.place(relx= 0.6, rely= 0.8, relwidth=0.4, relheight=0.2)

root.mainloop()

