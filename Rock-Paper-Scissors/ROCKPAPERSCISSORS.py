import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox

root = tk.Tk()
root.geometry("900x800")
root.title("ROCK PAPER SCISSORS")
root.config(bg="grey")
choice = ["rock", "paper", "scissors"]
user_choice = ""
computer_choice = ""
user_score = 0
computer_score = 0

def elsif():
    if user_choice == computer_choice:
        global result
        global user_score
        global computer_score
        result = "It's a draw!"
    elif user_choice == "rock" and computer_choice == "scissors":
        result = "You win!"
        user_score = user_score + 1
    elif user_choice == "scissors" and computer_choice == "rock":
        result = "The computer wins!"
        computer_score = computer_score + 1
    elif user_choice == "paper" and computer_choice == "rock":
        result = "You win!"
        user_score = user_score + 1
    elif user_choice == "rock" and computer_choice == "paper":
        result = "The computer wins!"
        computer_score = computer_score + 1
    elif user_choice == "paper" and computer_choice == "scissors":
        result = "The computer wins"
        computer_score = computer_score + 1
    elif user_choice == "scissors" and computer_choice == "paper":
        result = "You win!"
        user_score = user_score + 1



def rock():
    global user_choice
    user_choice = "rock"
    global computer_choice
    computer_choice = choice[random.randrange(len(choice))]
    elsif()
    label11 = Label(root, text=user_choice.upper(), font=("Impact", 30))
    label11.place_forget()
    label11.place(anchor="sw", rely="0.4", relx="0.12")
    label11.config(bg="white")

    label22 = Label(root, text=computer_choice.upper(), font=("Impact", 30))
    label22.place_forget()
    label22.place(anchor="se", rely="0.4", relx="0.8")
    label22.config(bg="white")

    messagebox.showinfo("SCORE TABLE", f"WINNER: \n {result} \n SCORE: \n You:{user_score} \n Computer: {computer_score}")
    label11.place_forget()
    label22.place_forget()






def paper():
    global user_choice
    user_choice = "paper"
    global computer_choice
    computer_choice = choice[random.randrange(len(choice))]
    elsif()

    label11 = Label(root, text=user_choice.upper(), font=("Impact", 30))
    label11.place_forget()
    label11.place(anchor="sw", rely="0.4", relx="0.12")
    label11.config(bg="white")

    label22 = Label(root, text=computer_choice.upper(), font=("Impact", 30))
    label22.place_forget()
    label22.place(anchor="se", rely="0.4", relx="0.8")
    label22.config(bg="white")

    messagebox.showinfo("SCORE TABLE", f"WINNER: \n {result} \n SCORE: \n You:{user_score} \n Computer: {computer_score}")
    label11.place_forget()
    label22.place_forget()
    




def scissors():
    global user_choice
    user_choice = "scissors"
    global computer_choice
    computer_choice = choice[random.randrange(len(choice))]
    elsif()
    label11 = Label(root, text=user_choice.upper(), font=("Impact", 30))
    label11.place(anchor="sw", rely="0.4", relx="0.12")
    label11.config(bg="white")

    label22 = Label(root, text=computer_choice.upper(), font=("Impact", 30))
    label22.place(anchor="se", rely="0.4", relx="0.8")
    label22.config(bg="white")

    messagebox.showinfo("SCORE TABLE", f"WINNER: \n {result} \n SCORE: \n You:{user_score} \n Computer: {computer_score}")
    label11.place_forget()
    label22.place_forget()



title = Label(root, text="ROCK PAPER SCISSORS GAME", font=("Impact", 50))
title.pack(anchor=CENTER, fill=X)
title.config()

label1 = Label(root, text="YOUR CHOICE:", font=("Impact", 30))
label1.place(anchor="sw", rely="0.3", relx="0.1")
label1.config(bg="grey")

label2 = Label(root, text="COMPUTER'S CHOICE:", font=("Impact", 30))
label2.place(anchor="se", rely="0.3", relx="0.9")
label2.config(bg="grey")

rockImg = PhotoImage(file="roca.png")
rock = Button(root, text="ROCK", image=rockImg, compound=BOTTOM, command=rock, font=("Impact", 14), ).place(anchor="se",
                                                                                                            rely="1",
                                                                                                            relx="1")

scissorsImg = PhotoImage(file="tijeras.png")
scissors = Button(root, text="SCISSORS", image=scissorsImg, command=scissors, compound=BOTTOM,
                  font=("Impact", 14)).place(anchor="se", rely="1", relx="0.292")

paperImg = PhotoImage(file="papel.png")
paper = Button(root, text="PAPER", image=paperImg, command=paper, compound=BOTTOM, font=("Impact", 14)).pack(
    side=BOTTOM)


root.mainloop()

