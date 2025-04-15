from tkinter import *
from db import Database
from tkinter import messagebox

db = Database("data.db")

# Configurar la screen
app = Tk()
app.title("CALENDARI D'AL·LÈRGIES")
app.geometry("700x450")
app.iconbitmap(r"sneez.ico")


# Menú 

# Funcions
def populate_list():
    llista.delete(0, END)
    for row in db.fetch():
        llista.insert(END, row)

def afegir_items():
    if data_text.get() == "" or nivell_text.get() == "" or alergens_text.get() == "" or tebarat_text.get() == "" or ebastel_text.get() == "" or simptomes_text.get() == "":
        messagebox.showerror("ESPAIS EN BLANC", "Has deixat espais sense contestar!")
        return
    db.insert(data_text.get(), nivell_text.get(), alergens_text.get(), tebarat_text.get(), ebastel_text.get(), simptomes_text.get())
    llista.delete(0, END)
    llista.insert(END, (data_text.get(), nivell_text.get(), alergens_text.get(), tebarat_text.get(), ebastel_text.get(), simptomes_text.get()))
    netejar_items()
    populate_list()

def seleccionar_item(event):
    try:
        global item_seleccionat
        index = llista.curselection()[0]
        item_seleccionat = llista.get(index)
        data_input.delete(0, END)
        data_input.insert(END, item_seleccionat[1])
        nivell_input.delete(0, END)
        nivell_input.insert(END, item_seleccionat[2])
        tebarat_input.delete(0, END)
        tebarat_input.insert(END, item_seleccionat[4])
        alergens_input.delete(0, END)
        alergens_input.insert(END, item_seleccionat[3])
        ebastel_input.delete(0, END)
        ebastel_input.insert(END, item_seleccionat[5])
        simptomes_input.delete(0, END)
        simptomes_input.insert(END, item_seleccionat[6])
    except IndexError:
        pass



def treure_items():
    db.remove(item_seleccionat[0])
    populate_list()
    netejar_items()


def editar_items():
    db.update(item_seleccionat[0], data_text.get(), nivell_text.get(), alergens_text.get(), tebarat_text.get(), ebastel_text.get(), simptomes_text.get())
    populate_list()

def netejar_items():
    data_input.delete(0, END)
    nivell_input.delete(0, END)
    tebarat_input.delete(0, END)
    alergens_input.delete(0, END)
    simptomes_input.delete(0, END)
    ebastel_input.delete(0, END)

# Dates
data_text = StringVar()
data_etiqueta = Label(app, text="DATA:", font=("bold", 14), pady=20)
data_etiqueta.grid(row=0, column=0)
data_input = Entry(app, textvariable=data_text)
data_input.grid(row=0, column=1)

# Nivell
nivell_text = StringVar()
nivell_etiqueta = Label(app, text="NIVELL:", font=("bold", 14), pady=20)
nivell_etiqueta.grid(row=1, column=0)
nivell_input = Entry(app, textvariable=nivell_text)
nivell_input.grid(row=1, column=1)

# Alèrgens
alergens_text = StringVar()
alergens_etiqueta = Label(app, text="ALÈRGENS:", font=("bold", 14), pady=20)
alergens_etiqueta.grid(row=2, column=0)
alergens_input = Entry(app, textvariable=alergens_text)
alergens_input.grid(row=2, column=1)

# Tebarat
tebarat_text = StringVar()
tebarat_etiqueta = Label(app, text="TEBARAT:", font=("bold", 14), pady=20)
tebarat_etiqueta.grid(row=0, column=2, padx="20")
tebarat_input = Entry(app, textvariable=tebarat_text)
tebarat_input.grid(row=0, column=3)

# Ebastel
ebastel_text = StringVar()
ebastel_etiqueta = Label(app, text="EBASTEL:", font=("bold", 14), pady=20)
ebastel_etiqueta.grid(row=1, column=2, padx="20")
ebastel_input = Entry(app, textvariable=ebastel_text)
ebastel_input.grid(row=1, column=3)

# Símptomes 
simptomes_text = StringVar()
simptomes_etiqueta = Label(app, text="SÍMPTOMES:", font=("bold", 14), pady=20)
simptomes_etiqueta.grid(row=2, column=2)
simptomes_input = Entry(app, textvariable=simptomes_text)
simptomes_input.grid(row=2, column=3)

# Llista
llista = Listbox(app, height=8, width=100)
llista.grid(row=4, column=0, columnspan=5, rowspan=6, pady=20, padx=35)

# Scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=4, column=5, pady=50)
llista.configure(yscroll=scrollbar.set)
scrollbar.configure(command=llista.yview)

# Selecció
llista.bind("<<ListboxSelect>>", seleccionar_item)

# Botons
afegir_btn = Button(app, text="AFEGIR", width=12, command=afegir_items)
afegir_btn.grid(row=3, column=0, pady=20)

treure_btn = Button(app, text="TREURE", width=12, command=treure_items)
treure_btn.grid(row=3, column=1)

editar_btn = Button(app, text="EDITAR", width=12, command=editar_items)
editar_btn.grid(row=3, column=2)

netejar_btn = Button(app, text="NETEJAR", width=12, command=netejar_items)
netejar_btn.grid(row=3, column=3)

# Recuperar dades
populate_list()
# Executar el programa
app.mainloop()
