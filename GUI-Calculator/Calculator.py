from tkinter import *
import tkinter as tk

def BtnClic(numero):
    global operator
    operator= operator+ str(numero)
    text_input.set(operator)
 
def Clear():
    global operator
    operator =""
    text_input.set("")

def Resoldre():
    try:
        global operator
        resultat= str(eval(operator))
        text_input.set(resultat)
        operator=""
    except:
        text_input.set("ERROR")
        

app = tk.Tk()
app.title("CALCULADORA")
operator=""
text_input = StringVar()



# Operació
entry = Entry(app,text="0", font=("arial", 20, "bold"), textvariable=text_input, bd=30, insertwidth=4, bg= "powder blue", justify="right", state="disabled")
entry.grid(columnspan=4)


# Botons

Boto7 = Button(app, padx=16,pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="7", command=lambda:BtnClic(7)).grid(row=1, column=0)
Boto8 = Button(app, padx=16,pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="8", command=lambda:BtnClic(8)).grid(row=1, column=1)
Boto9 = Button(app, padx=16,pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="9", command=lambda:BtnClic(9)).grid(row=1, column=2)
BotoMultiplicar = Button(app, padx=16,pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="X", command=lambda:BtnClic("*")).grid(row=1, column=3)
Boto4 = Button(app, padx=16,pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="4", command=lambda:BtnClic(4)).grid(row=2, column=0)
Boto5 = Button(app, padx=16,pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="5", command=lambda:BtnClic(5)).grid(row=2, column=1)
Boto6 = Button(app, padx=16,pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="6", command=lambda:BtnClic(6)).grid(row=2, column=2)
BotoRestar = Button(app, padx=20,pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="-", command=lambda:BtnClic("-")).grid(row=2, column=3)
Boto1 = Button(app, padx=16,pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="1", command=lambda:BtnClic(1)).grid(row=3, column=0)
Boto2 = Button(app, padx=16,pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="2", command=lambda:BtnClic(2)).grid(row=3, column=1)
Boto3 = Button(app, padx=16,pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="3", command=lambda:BtnClic(3)).grid(row=3, column=2)
BotoSumar = Button(app, padx=16,pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="+", command=lambda:BtnClic("+")).grid(row=3, column=3)
BotoClear = Button(app, padx=11,pady=19, bd=8, fg="black", font=("arial", 17, "bold"), text="CE", command=lambda:Clear()).grid(row=4, column=0)
Boto0 = Button(app, padx=16,pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="0", command=lambda:BtnClic(0)).grid(row=4, column=1)
BotoComa = Button(app, padx=19,pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text=".", command=lambda:BtnClic(".")).grid(row=4, column=2)
BotoIgual = Button(app, padx=16,pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="=", command=lambda:Resoldre()).grid(row=4, column=3)

















app.mainloop()
