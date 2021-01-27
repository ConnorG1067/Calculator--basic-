from tkinter import* 
import tkinter as tk



root = tk.Tk()
        
canvas = Canvas(root, height= 400, width=300)
canvas.pack()
        
screen = Text(root, width=300, height= 80, bg='#668cff', font=18)
screen.place(relwidth=1, relheight=0.2)


############### NUMBERS ###############
oneb = Button(root, text="1", font=18)
oneb.place(relwidth=0.2, relheight=0.2, rely=0.2)

twob = Button(root, text="2", font=18)
twob.place(relwidth=0.2, relheight=0.2, relx=0.2, rely=0.2)

threeb = Button(root, text="3", font=18)
threeb.place(relwidth=0.2, relheight=0.2, relx=0.4, rely=0.2)

fourb = Button(root, text="4", font=18)
fourb.place(relwidth=0.2, relheight=0.2, rely=0.4)

fiveb = Button(root, text="5", font=18)
fiveb.place(relwidth=0.2, relheight=0.2, relx=0.2, rely=0.4)

sixb = Button(root, text="6", font=18)
sixb.place(relwidth=0.2, relheight=0.2, relx=0.4, rely=0.4)

sevenb = Button(root, text="7", font=18)
sevenb.place(relwidth=0.2, relheight=0.2, rely=0.6)

eightb = Button(root, text="8", font=18)
eightb.place(relwidth=0.2, relheight=0.2, relx=0.2, rely=0.6)

nineb = Button(root, text="9", font=18)
nineb.place(relwidth=0.2, relheight=0.2, relx=0.4, rely=0.6)

zerob = Button(root, text="0", font=18)
zerob.place(relwidth=0.6, relheight=0.2, rely=0.8)


############### SYMBOLS ###############
divide = Button(root, text = "/", font = 18)
divide.place(relx= 0.6, rely= 0.2, relwidth=0.4, relheight=0.2)

multi = Button(root, text = "X", font = 18)
multi.place(relx= 0.6, rely= 0.4, relwidth=0.4, relheight=0.2)

sub = Button(root, text = "-", font = 18)
sub.place(relx= 0.6, rely= 0.6, relwidth=0.4, relheight=0.2)

add = Button(root, text = "+", font = 18)
add.place(relx= 0.6, rely= 0.8, relwidth=0.4, relheight=0.2)

root.mainloop()

