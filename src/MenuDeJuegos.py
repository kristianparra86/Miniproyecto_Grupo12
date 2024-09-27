import random, os, subprocess, time
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageColor, ImageTk

# ---------------------------------------------------- DEFINICION DE RUTAS ----------------------------------------------------

ruta_principal = os.path.dirname(__file__)                  # SE GUARDA EN UNA VARIABLE LA RUTA DONDE SE ENCUENTRA ESTE ARCHIVO
ruta_imagenes = os.path.join(ruta_principal, "img")         # SE GUARDA EN UNA VARIABLE LA RUTA DONDE SE ENCUENTRA LA CARPETA IMG
ruta_fondos = os.path.join(ruta_imagenes, "background")     # SE GUARDA EN UNA VARIABLE LA RUTA DONDE SE ENCUENTRA LA CARPETA BACKGROUND


def Ahorcado():
    subprocess.run(["python", "src/Ahorcado.py"])
def MesaDeApuestas():
    subprocess.run(["python", "src/MesaDeApuestas.py"])
def BlackJack():
    subprocess.run(["python", "src/BlackJack.py"])
def FlapyBird():
    subprocess.run(["python", "src/FlapyBird.py"])
def TrianguloMagico():
    subprocess.run(["python", "src/TrianguloMagico.py"])

def hora():
    tiempo_actual = time.strftime("%H:%M:%S")
    reloj.config(text = tiempo_actual)
    reloj.after(1000, hora)

# ---------------------------------------------------- VENTANA PRINCIPAL ----------------------------------------------------
root = Tk()
root.title("Menú De Juegos")
root.geometry("640x427")
root.resizable(False, False)
root.iconbitmap(os.path.join(ruta_imagenes, "icon/Menu_icon.ico"))     # AÑADIENDO ICONO A ROOT

# ---------------------------------------------------- MENU ----------------------------------------------------
barra_menu = Menu(root)
root.config(menu=barra_menu)

bg_img = ImageTk.PhotoImage(Image.open(os.path.join(ruta_fondos, "FondoMenu.jpg")))
lbl_img = Label(root, image=bg_img)
lbl_img.pack(fill="both", padx=0, pady=0, ipadx=0, ipady=0)

# ---------------------------------------------------- SUB MENU----------------------------------------------------
submenu = Menu(barra_menu, bg="#e0dddb", tearoff=0, font=("Arial", 10))
barra_menu.add_cascade(label ="Juegos", menu=submenu)

submenu.add_command(label = "Ahorcado", command=Ahorcado)
submenu.add_command(label = "Mesa de Apuestas", command=MesaDeApuestas)
submenu.add_command(label = "Black Jack", command=BlackJack)
submenu.add_command(label = "Flapy Bird", command=FlapyBird)
submenu.add_command(label = "Triangulo Magico", command=TrianguloMagico)

# ---------------------------------------------------- RELOJ ---------------------------------------------------
root_hora = Frame (root, width="100", height="100", bd=2, relief="solid")
root_hora.place(relx=0.84, rely=0.9)

reloj = Label(root_hora, font = ("Arial", 16), bg="#272e39", fg = "#e0dddb")
reloj.pack(anchor = "center")

hora()


root.mainloop()
