from pytube import YouTube
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import webbrowser




def Download():
    
    URL = link.get()
    yt = YouTube(URL)
    if (llista.current() == 2 ):
       thumbnailURL = yt.thumbnail_url
       webbrowser.open(thumbnailURL)
    elif (llista.current() == 1):
        folder_selected = filedialog.askdirectory()
        yt.streams.filter(only_audio=True).first().download(folder_selected)
    elif (llista.current() == 0):
        folder_selected = filedialog.askdirectory()
        yt.streams.first().download(folder_selected)
        
        





#Finestra
app = tk.Tk()
app.geometry("550x370")
app.title("YOUTUBE VIDEO DOWNLOADER")



#Títol
titol = Label(app, text="YT VIDEO DOWNLOADER", font=("impact", 44))
titol.grid(row= 0, column=3, padx=5)

#InsertarURLTXT
inputURLTXT = Label(app, text="Insert your URL:", font=("impact", 22))
inputURLTXT.grid(row=1, column=3)


# Link
var1 = StringVar()
link = Entry(app, textvariable=var1, font=("arial", 14), width=35)
link.grid(row=2, column=3, pady=25, padx=5)

# FormatTXT
SelFormatTXT = Label(app, text="Select format:", font=("impact", 22))
SelFormatTXT.grid(row=3, column=3)

# Llista format
llista = ttk.Combobox(app, values=["Video and Audio", "Only Audio", "Thumbnail"], state="readonly")
llista.grid(row=4, column=3)


# Download
DownloadBTN = Button(app, text="DOWNLOAD!", font=("impact", 22), bd=10, bg="powder blue", command=Download)
DownloadBTN.grid(row=8, column=3, padx=20, pady=20)






#Main loop de l'app
app.mainloop()


