from tkinter import*
from PIL import ImageTk ,Image
from tkinter import filedialog
import os

root=Tk()
root.geometry("500x500")

imagen1=ImageTk.PhotoImage(Image.open("abrir.png"))
imagen2=ImageTk.PhotoImage(Image.open("guardar.png"))
imagen3=ImageTk.PhotoImage(Image.open("salir.jpg"))

titulo=""

def thanos():
    root.destroy()

def abrir():
    global titulo
    texto.delete(1.0,END)
    input1.delete(1.0,END)
    text_file = filedialog.askopenfilename(tittle="Se esta abriendo el archivo",filetypes=(("Texto archivos", "*.txt"),))
    print(text_file)
    










input1=Entry(root)
input1.place(relx=0.7 , rely=0.1, anchor=CENTER)
boton1=Button(root,image=imagen1)
boton1.place(relx=0.05,rely=0.1,anchor=CENTER)
boton2=Button(root,image=imagen2)
boton2.place(relx=0.15,rely=0.1,anchor=CENTER)
boton3=Button(root,image=imagen3,command=thanos)
boton3.place(relx=0.25,rely=0.1,anchor=CENTER)
label1=Label(root,text="Titulo del Archivo")
label1.place(relx=0.48,rely=0.1,anchor=CENTER)
texto=Text(root,width=50,height=20)
texto.place(relx=0.5,rely=0.5,anchor=CENTER)



root.mainloop()