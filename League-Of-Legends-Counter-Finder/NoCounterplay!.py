#Mòduls
from tkinter import *
import tkinter as tk
import requests
from bs4 import BeautifulSoup
from tkinter import messagebox
import webbrowser


def trobar_champ():
    global champ
    champ = personatgeTriat.get()
    

def buscar():
    try:
        
         trobar_champ()
         llista.delete(0, END)
         pagina=requests.get("https://lolcounter.com/champions/"+champ)
         soup = BeautifulSoup(pagina.content, "html.parser")
         block = soup.find(class_="weak-block")
         champblock = block.find_all(class_="champ-block")
         counter_1 = champblock[0].find(class_="name").get_text()
         counter_2 = champblock[1].find(class_="name").get_text()
         counter_3 = champblock[2].find(class_="name").get_text()
         counter_4 = champblock[3].find(class_="name").get_text()
         counter_5 = champblock[4].find(class_="name").get_text()
         counters = [counter_1, counter_2, counter_3, counter_4, counter_5]
         subtitol.config(text= "Best " + champ + ' counters:')
         loop_number=1
         for element in counters:
             llista.insert(loop_number, element)
             loop_number += 1
        
    except:
        messagebox.showerror("ERROR", "There might be a mistake with the champion's name")
        
def buscar_runes():
    trobar_champ()
    jugant = llista.get(llista.curselection())
    webbrowser.open('https://u.gg/lol/champions/' + jugant + '/build?opp=' + champ)


#Finestra
app = tk.Tk()
app.geometry("420x450")
app.title("NO COUNTERPLAY!")
app.iconbitmap("icon.ico")


#Títol
titol = Label(app, text="NO COUNTERPLAY!", font=("impact", 44))
titol.grid(row= 0, column=3)

#Subtitol
subtitol = Label(app, text="Search for a Champion", font=("impact", 22))
subtitol.grid(row=1, column=3)


#Input del personatge
var = StringVar()
personatgeTriat = Entry(app, textvariable=var, font=("arial", 14), width=35)
personatgeTriat.grid(row=2, column=3, pady=25, padx=5)

#Botó de buscar
icono = PhotoImage(file = "buscar.png")
buscar = Button(image=icono, command=buscar)
buscar.grid(row=2, column=3, sticky=E)

#Llista
llista = Listbox(app, bg="#D2D2D2",height=5, width=25, font=("arial", 20))
llista.grid(row=3, column=3, pady=5, padx=15)


#Botó de buscar runes
runes = Button(text="SEARCH FOR THE BEST RUNES", command=buscar_runes, font=("arial", 14))
runes.grid(row=4, column=3, pady=13)

#Main loop de l'app
app.mainloop()
