import tkinter as tk
from random import *

root = tk.Tk()

root.geometry("500x400")

root["bg"] = "yellow"

root.title("Rock, Paper, Scissors")

selected = tk.Label(root,text="Your Choice = Nothing",bg="yellow", fg="black", font="Helvetica 30")
selected.pack()

selectedc = tk.Label(root,text="Computer Choice = Nothing",bg="yellow", fg="black", font="Helvetica 30")
selectedc.pack()

us = "nothing"
cs = "nothing"

RPS = ["Rock", "Paper", "Scissors"]

coms=0
ps=0

cl = tk.Label(root, text="Computer Score = 0", fg="black", font="Helvetica 20")
cl.pack()

eyn = tk.Label(root, text="Same Choice=", fg = "black", font="Helvetica 20")
eyn.pack()

pl = tk.Label(root, text="Player Score = 0", fg="black", font="Helvetica 20")
pl.pack()

def rock():
    global us
    us = "Rock"
    selected.config(text="Your Choice = Rock",fg = "black", font="Helvetica 30")
    check()
    

def paper():
    global us
    us = "Paper"
    selected.config(text="Your Choice = Paper",fg = "black", font="Helvetica 30")
    check()
    
def scissors():
    global us 
    us = "Scissors"
    selected.config(text="Your Choice = Scissors",fg = "black", font="Helvetica 30")
    check()


brock = tk.Button(root, fg="black", highlightbackground="blue", font="Helvetica 25", text="Rock" , command= rock)
brock.pack()

bpaper = tk.Button(root, fg="black", highlightbackground="pink", font="Helvetica 25", text="Paper" , command= paper)
bpaper.pack()

bscissors = tk.Button(root, fg="black", highlightbackground="green", font="Helvetica 25", text="Scissors" , command= scissors)
bscissors.pack()

def check():
    global us
    global cs
    global coms
    global ps
    cs = choice(RPS)

    if us == cs:
        eyn.config(text="Same Choice = Yes",fg = "black", font="Helvetica 20")

    if us == "Rock" and cs == "Paper":
            coms= coms+1
            eyn.config(text="Same Choice = No",fg = "black", font="Helvetica 20")
            
    if us == "Paper" and cs == "Rock":
            ps= ps+1
            eyn.config(text="Same Choice = No",fg = "black", font="Helvetica 20")
            

    if us == "Paper" and cs == "Scissors":
            coms= coms+1
            eyn.config(text="Same Choice = No",fg = "black", font="Helvetica 20")
          

    if us == "Scissors" and cs == "Paper":
            ps= ps+1
            eyn.config(text="Same Choice = No",fg = "black", font="Helvetica 20")
        

    if us == "Scissors" and cs == "Rock":
            coms= coms+1
            eyn.config(text="Same Choice = No",fg = "black", font="Helvetica 20")
         
            
    if us == "Rock" and cs == "Scissors":
            ps= ps+1
            eyn.config(text="Same Choice = No",fg = "black", font="Helvetica 20")
 
    cl.config(text = "Computer Score = {}".format(coms))
    pl.config(text = "Player Score = {}".format(ps))
    selectedc.config(text="Computer Choice = {}".format(cs),fg = "black", font="Helvetica 30")


    
