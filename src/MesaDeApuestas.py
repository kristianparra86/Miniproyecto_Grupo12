import random, os
from tkinter import *
from tkinter import messagebox, simpledialog
from PIL import Image, ImageColor, ImageTk

#--------------------------------------------------------------- VENTANA PRINCIPAL ---------------------------------------------------------------


# DEFINICION DE RUTAS
ruta_principal = os.path.dirname(__file__)                  # SE GUARDA EN UNA VARIABLE LA RUTA DONDE SE ENCUENTRA ESTE ARCHIVO
ruta_imagenes = os.path.join(ruta_principal, "img")         # SE GUARDA EN UNA VARIABLE LA RUTA DONDE SE ENCUENTRA LA CARPETA IMG
ruta_fondos = os.path.join(ruta_imagenes, "background")     # SE GUARDA EN UNA VARIABLE LA RUTA DONDE SE ENCUENTRA LA CARPETA BACKGROUND

# VENTANA PRINCIPAL
root = Tk()
root.title("Mesa de Apuestas")
root.geometry("1074x445")                                       # DEFINIENDO TAMAÑO DE ROOT
root.resizable(False,False)                                     # BLOQUEANDO TAMAÑO A ROOT
root.iconbitmap(os.path.join(ruta_imagenes, "icon/Apuestas_icon.ico"))     # AÑADIENDO ICONO A ROOT


#--------------------------------------------------------------- VARIABLES ---------------------------------------------------------------

# TIPOGRAFIAS
font_title = "Roboto"
font_buttom = "Calibri"
font_resto = "Futura"

saldo = DoubleVar(value=1000.0) # MANTENER EL SALDO POR DEBAJO DE LOS 100000
btn_click = None
numero_seleccionado = IntVar(value=-1)

rojo = (1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36)
negro = (2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35)
nom_docenas = ["1st 12", "2nd 12", "3rd 12", "2to 1", "1to 18", "PAR", "ROJO", "NEGRO", "IMPAR", "19to 36"]

#--------------------------------------------------------------- FUNCIONES ---------------------------------------------------------------

# FUNCION PARA DAR INICIO AL JUEGO
def play():
    try:
        if float(saldo.get()) >= int(ent_importe_apuesta.get()):
            if int(numero_seleccionado.get()) >= 0:
                verificacion()
            else:
                messagebox.showinfo(title="ERROR", message=" Por favor, eliga una opcion para su apuesta.")
        else:
            if int(saldo.get()) == 0:
                respuesta = messagebox.askokcancel(title="ERROR", message="        Su saldo es $ 0.\n¿Desea realizar una recarga?")
                if respuesta == True:
                    recarga_saldo()
                else:
                    despedida()
            else:
                messagebox.showinfo(title="ERROR", message=" Su saldo es insuficiente para la apuesta que desea realizar.")
                resetear_valores()
    except ValueError:
        messagebox.showinfo(title="ERROR", message=" El valor ingresado NO es valido.\nVerifique el importe de su apuesta.")
        resetear_valores()

# FUNCION PARA VERIFICAR RESULTADO DEL JUEGO
def verificacion():
    def informando_ganancias(ratio_ganado):
        messagebox.showinfo(title="RESULTADO DE LA APUESTA", message=f" Felicidades el numero ganador es el {numero_aleatorio}.\n\n              Acaba de ganar $ {int(ent_importe_apuesta.get()) * ratio_ganado}")
        saldo.set(saldo.get() + (int(ent_importe_apuesta.get()) * ratio_ganado))
        lbl_numero_ganador.destroy()
        resetear_valores()
    def informando_perdidas():
        messagebox.showinfo(title="RESULTADO DE LA APUESTA", message=f" Lo siento, el numero ganador es el {numero_aleatorio}.\n\n            Acaba de perder $ {int(ent_importe_apuesta.get())}")
        saldo.set(saldo.get() - int(ent_importe_apuesta.get()))
        lbl_numero_ganador.destroy()
        resetear_valores()
    def apuesta_paridad(): # PAGA 1/1
        if numero_seleccionado.get() == 44 and 1 <= numero_aleatorio <= 36 and numero_aleatorio % 2 == 0:
            informando_ganancias(1)
        elif numero_seleccionado.get() == 47 and 1 <= numero_aleatorio <= 36 and numero_aleatorio % 2 != 0:
            informando_ganancias(1)
        else:
            informando_perdidas()
    def apuesta_color(): # PAGA 1/1
        if numero_seleccionado.get() == 45 and numero_aleatorio in rojo:
            informando_ganancias(1)
        elif numero_seleccionado.get() == 46 and numero_aleatorio in negro:
            informando_ganancias(1)
        else:
            informando_perdidas()
    def apuesta_multiple(a, b, c): #("1to 18" Y "19to 36" PAGA  1/1) ("2to 1" PAGA  1/1)
        lista = list(range(a, b, c))
        if numero_aleatorio in lista:
            if numero_seleccionado.get() == 40 or numero_seleccionado.get() == 41 or numero_seleccionado.get() == 42:
                informando_ganancias(2)
            else:
                informando_ganancias(1)
        else:
            informando_perdidas()

    numero_aleatorio = random.randint(0,36) # GENERAMOS UN NUMERO ALEATORIO

    # INFORMANDO EL NUMERO GANADOR
    lbl_numero_ganador = Label(frame1, text=numero_aleatorio, font=(font_buttom, 20), fg="#ffffff")
    lbl_numero_ganador.place(relx=0.48, rely=0.85)
    if numero_aleatorio in rojo:
        lbl_numero_ganador.config(bg="#E4080A")
    elif numero_aleatorio in negro:
        lbl_numero_ganador.config(bg="#000000")
    else:
        lbl_numero_ganador.config(bg="#10C803")

    # COMPROBACION
    if numero_seleccionado.get() <= 36: # PAGA 35/1
        if numero_aleatorio == numero_seleccionado.get():
            informando_ganancias(35)
        else:
            informando_perdidas()
    else:
        if numero_seleccionado.get() == 37: apuesta_multiple(1, 13,1)                               # "1st 12"
        elif numero_seleccionado.get() == 38: apuesta_multiple(13,25,1)                             # "2nd 12"
        elif numero_seleccionado.get() == 39: apuesta_multiple(25,37,1)                             # "3rd 12"
        elif numero_seleccionado.get() == 40: apuesta_multiple(3,37,3)                              # "2to 1"
        elif numero_seleccionado.get() == 41: apuesta_multiple(2,37,3)                              # "2to 1"
        elif numero_seleccionado.get() == 42: apuesta_multiple(1,37,3)                              # "2to 1"
        elif numero_seleccionado.get() == 43: apuesta_multiple(1,19,1)                              # "1to 18"
        elif numero_seleccionado.get() == 44 or numero_seleccionado.get() == 47: apuesta_paridad()  # "PAR" - "IMPAR"
        elif numero_seleccionado.get() == 45 or numero_seleccionado.get() == 46: apuesta_color()    # "ROJO" - "NEGRO"
        elif numero_seleccionado.get() == 48: apuesta_multiple(19,37,1)                             # "19to 36"

# FUNCION PARA RECARGAR SALDO
def recarga_saldo():
    recarga = simpledialog.askfloat("RECARGA","Ingrese el importa a que desea recargar.")
    if recarga:    
        if recarga <= 10000:
            saldo.set(saldo.get() + recarga)
            messagebox.showinfo(title="Felicidades", message="Su recarga ya se encuentra acreditada.")
            resetear_valores()
        else:
            messagebox.showinfo(title="ERROR", message=" El importe ingresado es superior a lo permitido.\n                TOPE DE RECARGA: $10000")
            recarga_saldo()
    else:
        despedida()

# FUNCION PARA RESETEAR LOS VALORES INGRESADOS
def resetear_valores():
    ent_importe_apuesta.delete(0, END)
    numero_seleccionado.set(-1)
    if btn_click:
        btn_click.config(bg=btn_color_original)

# FUNCION PARA GENERAR EL PAÑO DE APUESTAS
def pañoDeApuestas():
    
    def apariencia_button_1_36():
            if i in rojo:
                btn.config(bg="#e4080a", fg="#FFFFFF")
            else:
                btn.config(bg="#000000", fg="#FFFFFF")

    def apariencia_button_ext():
        btn.config(bg="#1f4537", fg="#ffffff", font=(font_buttom, 10))

    # FUNCION PARA CAMBIAR EL COLOR DE UN BUTTON AL SER SELECCIONADO
    def color_button_presionado(seleccion):
        global btn_click, btn_color_original
        if btn_click:
            btn_click.config(bg=btn_color_original)
        btn_color_original = seleccion.widget.cget("bg")
        seleccion.widget.config(bg="#10c803")
        btn_click = seleccion.widget

    # FUNCION PARA ASIGNAR EL VALOR DEL BOTON SELECCIONADO
    def captar_numero(valor):
        numero_seleccionado.set(valor)

    # BOTONES DESDE 0 AL 36 - EN FRAME "frame_paño_1"
    for i in range(3, 37, 3):
        btn = Button(frame_paño_1, text=f"{i}", command=lambda i=i: captar_numero(i), width="3", height="3")
        btn.grid(row=0, column=(i-2))
        btn.bind("<Button-1>", color_button_presionado)
        apariencia_button_1_36()

    for i in range(2, 37, 3):
        btn = Button(frame_paño_1, text=f"{i}", command=lambda i=i: captar_numero(i), width="3", height="3")
        btn.grid(row=1, column=(i-1))
        btn.bind("<Button-1>", color_button_presionado)
        apariencia_button_1_36()

    for i in range(1, 37, 3):
        btn = Button(frame_paño_1, text=f"{i}", command=lambda i=i: captar_numero(i), width="3", height="3")
        btn.grid(row=2, column=i)
        btn.bind("<Button-1>", color_button_presionado)
        apariencia_button_1_36()

    btn = Button(frame_paño_1, text="0", command=lambda i=i: captar_numero(0), width="5", height="10")
    btn.grid(row=0, rowspan=3, column=0)
    btn.bind("<Button-1>", color_button_presionado)
    apariencia_button_ext()
    btn.config(bg="#145738")

    # BOTONES APUESTA VARIOS NUMEROS - EN FRAME "frame_paño_2"
        # DOCENA (Numero de referencia 37-38-39-40-41-42)
    for i in range(3):
        btn = Button(frame_paño_2, text=nom_docenas[i], command=lambda i=i: captar_numero(i+37), width="22", height="1")
        btn.grid(row=0, column=i*2, columnspan=2)
        btn.bind("<Button-1>", color_button_presionado)
        apariencia_button_ext()

    for i in range(3):
        btn = Button(frame_paño_1, text=nom_docenas[3], command=lambda i=i: captar_numero(i+40), width="9", height="3")
        btn.grid(row=i, column=36)
        btn.bind("<Button-1>", color_button_presionado)
        apariencia_button_ext()

        # EXTRAS (Numero de referencia 43-44-45-46-47-48-49)
    for i in range(6):
        btn = Button(frame_paño_2, text=nom_docenas[i+4], command=lambda i=i: captar_numero(i+43), width="10", height="1")
        btn.grid(row=1, column=i)
        btn.bind("<Button-1>", color_button_presionado)
        apariencia_button_ext()

# FUNCION DESPEDIDA AL MOMENTO DE DEJAR EL JUEGO
def despedida():
    messagebox.showinfo(title="VUELVA PRONTO", message=" Gracias por elegirnos...")
    root.destroy()


#--------------------------------------------------------------- SOLICITUD DE DATOS ---------------------------------------------------------------

# FRAME 1
frame1 = Frame (root, width="430", height="430")
frame1.grid_propagate(False)
frame1.grid(row=0, column=0)

# IMAGEN DE FONDO EN FRAME 1
bg_img = ImageTk.PhotoImage(Image.open(os.path.join(ruta_fondos, "RuletaDeApuestas.jpg")))
lbl_img = Label(frame1, image=bg_img)
lbl_img.pack(fill="both", padx=0, pady=0, ipadx=0, ipady=0)

# INFORMACION DE DE DATOS Y SOLICITUDES
lbl_bienvenida = Label (frame1,text="¡BIENVENIDO!", bg="#7ca283", fg="#ffffff", font=(font_title, 20))
btn_enter = Button (frame1, text="GIRAR", command=play, bg="#000000", fg="#ffffff", font=(font_buttom, 12))

lbl_bienvenida.place(relx=0.5, rely=0.1, anchor="center")
btn_enter.place(relx=0.51, rely=0.6, anchor="center", relwidth=0.2, relheight=0.06)


#--------------------------------------------------------------- INSTRUCCIONES ---------------------------------------------------------------

# FRAME2 
frame2 = Frame (root, width="614", height="430", bg="#145738")
frame2.grid_propagate(False)
frame2.grid(row=0, column=1)

# FRAME INSTRUCCIONES
frame_instrucciones = Frame(frame2, width="610", height="85", bg="#145738")
frame_instrucciones.place(relx=0, rely=0)

lbl_instrucciones_title = Label (frame_instrucciones, text="INSTRUCCIONES", justify="center", bg="#145738", fg="#ffffff", font=(font_title, 15))
lbl_instrucciones_title.place(relx=0.38, rely=0.05)
lbl_instrucciones_pasos = Label (frame_instrucciones, text="Ingresar el importe de la apuesta.\nSeleccionar su apuesta.\nPresione ENTER.", justify="left", bg="#145738", fg="#ffffff", font=(font_resto, 10))
lbl_instrucciones_pasos.place(relx=0.02, rely=0.33)


#--------------------------------------------------------------- PAÑO DE APUESTAS ---------------------------------------------------------------

# FRAMES PAÑO DE APUESTAS
frame_paño_1 = Frame(frame2, bg="#145738")
frame_paño_1.place(x=70, y=90)

frame_paño_2 = Frame(frame2, bg="#145738")
frame_paño_2.place(x=70, y=259)

pañoDeApuestas()

#--------------------------------------------------------------- RESULTADOS ---------------------------------------------------------------

# FRAMES PAÑO RESULTADO
frame_resultado = Frame(frame2, width="610", height="112", bg="#145738")
frame_resultado.place(relx=0, rely=0.74)

lbl_importe_apuesta = Label (frame_resultado, text="Ingrese el importe de su apuesta $", justify="right", bg="#145738", fg="#ffffff", font=(font_resto, 12))
ent_importe_apuesta = Entry (frame_resultado, font=(font_resto, 10), width=11)
lbl_info_saldo = Label(frame_resultado, text=f"Su saldo actual es de $   ", bg="#7ca283", fg="#ffffff", font=(font_resto, 13))
lbl_saldo = Label(frame_resultado, textvariable=saldo, bg="#7ca283", fg="#ffffff", font=(font_resto, 13))

lbl_importe_apuesta.place(relx=0.18, rely=0.3)
ent_importe_apuesta.place(relx=0.65, rely=0.4, anchor="center")
lbl_info_saldo.place(relx=0.76, rely=0.85, anchor="center")
lbl_saldo.place(relx=0.94, rely=0.85, anchor="center")


root.mainloop()





#------------------------------------------------------------ INFORMACION Y CODIGOS AUXILIARES ---------------------------------------------------------------
#Color de Fondo ->"#145738"
#Color de Button Apusetas Multiples ->"#1f4537"
#Color Verde -> "#10c803"
#Color Rojo -> "#e4080a"
#Color Negro -> "#000000"
#Color Blanco -> "#ffffff"
