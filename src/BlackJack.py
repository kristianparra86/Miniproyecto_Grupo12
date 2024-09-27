
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
import random
import time


cartas = ['as_corazon', 'dos_corazon', 'tres_corazon', 'cuatro_corazon', 'cinco_corazon', 'seis_corazon',
          'siete_corazon', 'ocho_corazon', 'nueve_corazon', 'diez_corazon', 'jota_corazon', 'reina_corazon', 'rey_corazon',
          'as_picas', 'dos_picas', 'tres_picas', 'cuatro_picas', 'cinco_picas', 'seis_picas',
          'siete_picas', 'ocho_picas', 'nueve_picas', 'diez_picas', 'jota_picas', 'reina_picas', 'rey_picas',
          'as_diamante', 'dos_diamante', 'tres_diamante', 'cuatro_diamante', 'cinco_diamante', 'seis_diamante',
          'siete_diamante', 'ocho_diamante', 'nueve_diamante', 'diez_diamante', 'jota_diamante', 'reina_diamante', 'rey_diamante',
          'as_trebol', 'dos_trebol', 'tres_trebol', 'cuatro_trebol', 'cinco_trebol', 'seis_trebol',
          'siete_trebol', 'ocho_trebol', 'nueve_trebol', 'diez_trebol', 'jota_trebol', 'reina_trebol', 'rey_trebol']

maso_juego = ['as_corazon', 'dos_corazon', 'tres_corazon', 'cuatro_corazon', 'cinco_corazon', 'seis_corazon',
              'siete_corazon', 'ocho_corazon', 'nueve_corazon', 'diez_corazon', 'jota_corazon', 'reina_corazon', 'rey_corazon',
              'as_picas', 'dos_picas', 'tres_picas', 'cuatro_picas', 'cinco_picas', 'seis_picas',
              'siete_picas', 'ocho_picas', 'nueve_picas', 'diez_picas', 'jota_picas', 'reina_picas', 'rey_picas',
              'as_diamante', 'dos_diamante', 'tres_diamante', 'cuatro_diamante', 'cinco_diamante', 'seis_diamante',
              'siete_diamante', 'ocho_diamante', 'nueve_diamante', 'diez_diamante', 'jota_diamante', 'reina_diamante', 'rey_diamante',
              'as_trebol', 'dos_trebol', 'tres_trebol', 'cuatro_trebol', 'cinco_trebol', 'seis_trebol',
              'siete_trebol', 'ocho_trebol', 'nueve_trebol', 'diez_trebol', 'jota_trebol', 'reina_trebol', 'rey_trebol']


""" Principio funciones"""


"""funciones apuesta y saldo"""


def sumar_10():  # apuesta +10
    global suma_apuesta, saldo
    suma_apuesta += 10
    saldo -= 10
    etq_apuesta_1.delete(0, tk.END)
    etq_apuesta_1.insert(0, suma_apuesta)
    fondos_negativos()
    mostrar_suma_apuesta()
    mostrar_saldo()


def sumar_20():  # apuesta +20
    global suma_apuesta, saldo
    suma_apuesta += 20
    saldo -= 20
    etq_apuesta_1.delete(0, tk.END)
    etq_apuesta_1.insert(0, suma_apuesta)
    fondos_negativos()
    mostrar_suma_apuesta()
    mostrar_saldo()


def sumar_50():  # apuesta +50
    global suma_apuesta, saldo
    suma_apuesta += 50
    saldo -= 50
    etq_apuesta_1.delete(0, tk.END)
    etq_apuesta_1.insert(0, suma_apuesta)
    fondos_negativos()
    mostrar_suma_apuesta()
    mostrar_saldo()


def sumar_100():  # apuest +100
    global suma_apuesta, saldo
    suma_apuesta += 100
    saldo -= 100
    etq_apuesta_1.delete(0, tk.END)
    etq_apuesta_1.insert(0, suma_apuesta)
    fondos_negativos()
    mostrar_suma_apuesta()
    mostrar_saldo()


def mostrar_saldo():  # funcion para mostrar el saldo en la etiqueta
    global saldo
    etq_saldo_1.delete(0, tk.END)
    etq_saldo_1.insert(0, saldo)


def mostrar_suma_apuesta():  # funcion para mostrar la suma total de la apuesta
    global suma_apuesta
    etq_apuesta_1.delete(0, tk.END)
    etq_apuesta_1.insert(0, suma_apuesta)


def fondos_negativos():  # compara si el saldo es negativo o la apuesta es mayor el saldo del banco
    global saldo
    if saldo <= 0:
        resp_saldo = messagebox.askquestion(
            "Cajero", "Te quedaste sin fondos, ¿Deseas Sumar 1000 mas a tu saldo?")
        if resp_saldo == "yes":
            messagebox.showinfo(
                "Suma saldo", "Se te acreditaron $1000 mas para seguir jugando")
            saldo += 1000
        else:
            messagebox.showinfo(
                "Lo Siento", "Se a quedado sin saldo, puede terminar la mano")


""""Funcion tutorial"""


def ver_tuto():  # funcion del message box para el tutorial
    respuesta = messagebox.askquestion(
        "Como Jugar", "¿Desea leer un mini tutorial del juego?")
    if respuesta == "yes":
        messagebox.showinfo("Como Jugar",
                            "Se debe sumar 21 puntos. El Crupier está obligado a pedir carta siempre que su puntuación sume 16 o menos. En el caso del crupier, los ases valen 11 mientras no se pase de 21, y 1 en caso contrario. Las cartas numéricas suman su valor, las figuras suman 10 y el 'as' vale 11 o 1, depende la situación.")
    else:
        pass


"""Funcion de repartir cartas"""


def obtener_nueva_carta():  # reparte nueva carta, elije una eandom del maso
    global maso_juego, maxi, indice
    # el maximo del random va a ser la longitud del maso del juego
    maxi = len(maso_juego)
    # con la funcion random, elije el indice de donde esta ubicada la carta
    indice = random.randint(0, maxi)-1
    # asigno esta carta a naipe, para poder ser eliminada de la lista correctamente
    naipe = maso_juego[indice]
    # se elimina el naipe del  maso para q no sea elegida nuevamnetedentro de la mano.
    maso_juego.remove(naipe)
    return naipe


def valor_mano(mano):  # calcula el valor de cada mano, sumando el valor de las cartas
    global cartas
    """Calcula el valor de mano, elige el valor del AS de acuerdo situación"""
    valor_mano = 0
    hay_as = False
    for i in mano:  # recorre las cartas de la mano
        # asigna valor a la carta, segun el indice en el que se encuentra
        valor_carta = cartas.index(i)+1
        if valor_carta > 39 and valor_carta < 53:  # calcula el valor de las cartas trebol
            valor_carta = valor_carta - 39
        if valor_carta > 26 and valor_carta < 40:  # calcula el valor de las cartas diamante
            valor_carta = valor_carta - 26
        if valor_carta > 13 and valor_carta < 27:  # calcula el valor de las cartas picas
            valor_carta = valor_carta - 13
        if valor_carta > 10 and valor_carta < 14:  # calcula el valor de las cartas corazon
            valor_carta = 10
        # busca si la mano tiene un 'as' en ella
        if i == 'as_corazon' or i == 'as_picas' or i == 'as_diamante' or i == 'as_trebol':
            hay_as = True
        valor_mano += valor_carta
    if hay_as and valor_mano <= 11:  # comprobamos si el valor de la mano es menor a 10 y si hay un 'as' presente el valor del 'as' pasa a ser 11
        valor_mano += 10
    return valor_mano


""" funcion para iniciar"""


def desea_comenzar():  # mensaje, pregunta si desea iniciar  a Jugar

    comenzar = messagebox.askquestion(
        "Bienvenido/a Black Jack INFO24 By Cristian Parra", "¿Desea Comenzar a Jugar?")
    if comenzar == "yes":
        messagebox.showinfo(
            "Comencemos", " Que disfrutes el Juego, apuesta minima para iniciar $10")
        time.sleep(0.5)
        iniciar_mano()
    else:
        messagebox.showinfo("Adios", "Vuelve Pronto")
        time.sleep(0.25)
        exit(0)


def desea_nueva_mano():  # mensaje, preguntando si se desea continuar jugando
    global maso_juego, cartas
    time.sleep(0.5)
    comenzar = messagebox.askquestion(
        "Black Jack 21", "¿Desea Comenzar Nueva Mano?")
    if comenzar == "yes":
        messagebox.showinfo(
            "Continuamos", " Apuesta minima de la mano $10")
        # asigno todas las cartas al maso nuevamente
        maso_juego = ['as_corazon', 'dos_corazon', 'tres_corazon', 'cuatro_corazon', 'cinco_corazon', 'seis_corazon',
                      'siete_corazon', 'ocho_corazon', 'nueve_corazon', 'diez_corazon', 'jota_corazon', 'reina_corazon', 'rey_corazon',
                      'as_picas', 'dos_picas', 'tres_picas', 'cuatro_picas', 'cinco_picas', 'seis_picas',
                      'siete_picas', 'ocho_picas', 'nueve_picas', 'diez_picas', 'jota_picas', 'reina_picas', 'rey_picas',
                      'as_diamante', 'dos_diamante', 'tres_diamante', 'cuatro_diamante', 'cinco_diamante', 'seis_diamante',
                      'siete_diamante', 'ocho_diamante', 'nueve_diamante', 'diez_diamante', 'jota_diamante', 'reina_diamante', 'rey_diamante',
                      'as_trebol', 'dos_trebol', 'tres_trebol', 'cuatro_trebol', 'cinco_trebol', 'seis_trebol',
                      'siete_trebol', 'ocho_trebol', 'nueve_trebol', 'diez_trebol', 'jota_trebol', 'reina_trebol', 'rey_trebol']
        time.sleep(0.5)
        iniciar_mano()
    else:
        messagebox.showinfo("Adios", "Vuelve Pronto")
        time.sleep(0.25)
        exit(0)


def iniciar_mano():
    """uncion q inicia la mano y reparte dos cartas cada uno"""
    global mano_crupier, mano_player, saldo, suma_apuesta
    suma_apuesta = 0
    # se asigna dos cartas a la mano del jugador
    mano_player = [obtener_nueva_carta(), obtener_nueva_carta()]
    # se asigna dos cartas a la mano del crupier
    mano_crupier = [obtener_nueva_carta(), obtener_nueva_carta()]
    sumar_10()  # se suma 10 la apuesta
    mostrar_saldo()  # muestra el saldo
    mostrar_suma_apuesta()  # muestra el total de la apuesta
    limpiar_cartas()   # limpia las cartas del game anterior
    # muestra las cartas repartidas 2 player y 1 crupier mas cartqa oculta
    mostrar_carta_player(mano_player)  # muestra carta del player
    mostrar_crupier_oculta(mano_crupier)  # muestra carta del crupier
    etq_pts_player_1.delete(0, tk.END)  # limpia la etiqueta de puntos player
    etq_pts_player_1.insert(0, valor_mano(mano_player)
                            )  # se imprime nuevo valor de la etiqueta de los puntos player
    etq_pts_crupier_1.delete(0, tk.END)
    if valor_mano(mano_player) == 21:  # si la mano player vale 21, la pauesta multiplica x4
        messagebox.showinfo(
            "Ganaste", '¡¡¡Black Jack!!!¡Felicidades Ganaste la mano, Sumaste 21!')
        saldo += (suma_apuesta*4)
        time.sleep(0.5)
        mostrar_suma_apuesta()
        mostrar_saldo()
        desea_nueva_mano()
    elif valor_mano(mano_crupier) == 21 and valor_mano(mano_player) == 21:
        time.sleep(0.5)
        messagebox.showinfo(
            "¡¡¡Empate!!!", ' Ambos obtuvieron 21 puntos')
        saldo += suma_apuesta
        mostrar_saldo()
        desea_nueva_mano()


def continuar_jugando():
    global saldo, suma_apuesta, mano_player
    mostrar_suma_apuesta()
    mano_player.append(obtener_nueva_carta())
    mostrar_carta_player(mano_player)
    etq_pts_player_1.delete(0, tk.END)
    etq_pts_player_1.insert(0, valor_mano(mano_player))
    if valor_mano(mano_player) == 21:
        time.sleep(0.5)
        messagebox.showinfo(
            "¡¡¡¡Ganaste!!!", '¡¡¡Black Jack!!! ¡Felicidades Ganaste la mano, Sumaste 21!')
        juega_crupier()
        mostrar_crupier_oculta(mano_crupier)
        saldo += (suma_apuesta*2)
        mostrar_saldo()
        etq_apuesta_1.delete(0, tk.END)
        desea_nueva_mano()
    elif valor_mano(mano_player) > 21:
        time.sleep(0.5)
        messagebox.showinfo(
            "¡¡¡Perdiste!!!", 'Lo siento, te has pasado de 21 puntos')
        mostrar_saldo()
        etq_apuesta_1.delete(0, tk.END)
        desea_nueva_mano()


def detener_pasar():
    global saldo, suma_apuesta, mano_player, mano_crupier
    juega_crupier()
    mostrar_carta_crupier(mano_crupier)
    mostrar_carta_player(mano_player)
    etq_pts_player_1.delete(0, tk.END)
    etq_pts_player_1.insert(0, valor_mano(mano_player))
    etq_pts_crupier_1.delete(0, tk.END)
    etq_pts_crupier_1.insert(0, valor_mano(mano_crupier))
    if valor_mano(mano_player) == 21:
        time.sleep(0.5)
        messagebox.showinfo(
            "¡¡¡Ganaste!!!", '¡¡¡Black Jack!!! ¡Felicidades ganaste la mano, Sumaste 21 puntos!')
        mostrar_carta_crupier(mano_crupier)
        saldo += (suma_apuesta*2)
        mostrar_saldo()
        etq_apuesta_1.delete(0, tk.END)
        desea_nueva_mano()
    elif valor_mano(mano_crupier) == 21 and valor_mano(mano_player) < 21:
        time.sleep(0.5)
        messagebox.showinfo(
            "Lo siento", '¡Perdiste el crupier las tiene mejores, Sumo 21!')
        mostrar_saldo()
        etq_apuesta_1.delete(0, tk.END)
        desea_nueva_mano()
    elif valor_mano(mano_crupier) > 21:
        time.sleep(0.5)
        messagebox.showinfo(
            "¡Felicidades!", "¡¡¡Ganaste!!! .El crupier se paso de rosca y sumo mas de 21")
        saldo += (suma_apuesta*2)
        mostrar_saldo()
        etq_apuesta_1.delete(0, tk.END)
        desea_nueva_mano()
    elif valor_mano(mano_crupier) < valor_mano(mano_player):
        time.sleep(0.5)
        messagebox.showinfo("¡Felicidades! ",
                            "¡¡¡Ganaste!!! tenes mejor puntaje que el crupier")
        saldo += (suma_apuesta*2)
        mostrar_saldo()
        etq_apuesta_1.delete(0, tk.END)
        desea_nueva_mano()
    elif valor_mano(mano_crupier) == valor_mano(mano_player):
        messagebox.showinfo(
            "¡Empate!", " Sumaron los mismos puntos y se te retorna tu apuesta")
        saldo += suma_apuesta
        mostrar_saldo()
        etq_apuesta_1.delete(0, tk.END)
        desea_nueva_mano()
    elif valor_mano(mano_player) == 21:
        messagebox.showinfo(
            "¡Black Jack!", "¡Felicidades Ganaste la mano, Sumaste 21!")
        saldo += (suma_apuesta*2)
        mostrar_saldo()
        etq_apuesta_1.delete(0, tk.END)
        desea_nueva_mano()
    elif valor_mano(mano_crupier) > valor_mano(mano_player) and valor_mano(mano_crupier) < 21:
        messagebox.showinfo(
            "¡Lo Siento!", '¡Perdiste el crupier las tiene mejores!')
        mostrar_saldo()
        etq_apuesta_1.delete(0, tk.END)
        desea_nueva_mano()


def juega_crupier():  # juega el crupier, pide cartas menos su puntaje sea menor q 17
    global mano_crupier
    while valor_mano(mano_crupier) < 17:
        nueva_carta = obtener_nueva_carta()
        mano_crupier.append(nueva_carta)
    return mano_crupier


# redimensionar las img de cartas
def size_cards(carta):
    global carta_img
    carta_img = Image.open(carta)
    card_size_card = carta_img.resize((100, 140))
    carta_img = ImageTk.PhotoImage(card_size_card)
    return carta_img


# funcion q muestra las cartas del jugador e inserta las imagenes de cada carta en cada label
def mostrar_carta_player(mano):
    global player_img1, player_img2, player_img3, player_img4, player_img5
    player_spot = 0
    for carta in mano:
        player_spot += 1
        if player_spot == 1:
            player_img1 = size_cards(f'src/img/cards/{carta}.png')
            player_label_1.config(image=player_img1)
        elif player_spot == 2:
            player_img2 = size_cards(f'src/img/cards/{carta}.png')
            player_lebel_2.config(image=player_img2)
        elif player_spot == 3:
            player_img3 = size_cards(f'src/img/cards/{carta}.png')
            player_label_3.config(image=player_img3)
        elif player_spot == 4:
            player_img4 = size_cards(f'src/img/cards/{carta}.png')
            player_label_4.config(image=player_img4)
        elif player_spot == 5:
            player_img5 = size_cards(f'src/img/cards/{carta}.png')
            player_label_5.config(image=player_img5)


# funcion q muestra las cartas del crupier e inserta las imagenes de cada carta en cada label
def mostrar_carta_crupier(mano):
    global crupier_img1, crupier_img2, crupier_img3, crupier_img4, crupier_img5
    crupier_spot = 0
    for carta in mano:
        crupier_spot += 1
        if crupier_spot == 1:
            crupier_img1 = size_cards(f'src/img/cards/{carta}.png')
            crupier_label_1.config(image=crupier_img1)
        elif crupier_spot == 2:
            crupier_img2 = size_cards(f'src/img/cards/{carta}.png')
            crupier_label_2.config(image=crupier_img2)
        elif crupier_spot == 3:
            crupier_img3 = size_cards(f'src/img/cards/{carta}.png')
            crupier_label_3.config(image=crupier_img3)
        elif crupier_spot == 4:
            crupier_img4 = size_cards(f'src/img/cards/{carta}.png')
            crupier_label_4.config(image=crupier_img4)
        elif crupier_spot == 5:
            crupier_img5 = size_cards(f'src/img/cards/{carta}.png')
            crupier_label_5.config(image=crupier_img5)


# funcion que muestra en el crupier solo una carta visible y la otra oculta
def mostrar_crupier_oculta(mano):
    global crupier_img1, crupier_img2
    crupier_spot = 0
    for carta in mano:
        crupier_spot += 1
        if crupier_spot == 1:
            crupier_img1 = size_cards(f'src/img/cards/{carta}.png')
            crupier_label_1.config(image=crupier_img1)
        elif crupier_spot == 2:
            crupier_img2 = size_cards(
                f'src/img/cards/carta_oculta.png')  # muestra carta oculta
            crupier_label_2.config(image=crupier_img2)


def limpiar_cartas():  # limpia las cartas  del game anterior
    player_label_1.config(image='')
    player_lebel_2.config(image='')
    player_label_3.config(image='')
    player_label_4.config(image='')
    player_label_5.config(image='')

    crupier_label_1.config(image='')
    crupier_label_2.config(image='')
    crupier_label_3.config(image='')
    crupier_label_4.config(image='')
    crupier_label_5.config(image='')


"""Fin funciones

"""

# Crea una instancia de la clase Tk, que representa la ventana principal
ventana = tk.Tk()
# Establece el título de la ventana principal
ventana.title("BLACK JACK-Informatorio-Parra Cristian")
ventana.iconbitmap('src/img/icon/BlackJack_icon.ico')
# Establece el tamaño de la ventana principal a 900x550 píxeles
ventana.geometry("900x550")
# establece tamaño fijo de ventana
ventana.resizable(False, False)


"""Frame 1"""
frame_1 = Frame(ventana)
frame_1.config(background="Green", bd=1, relief="solid", cursor="target")
frame_1.pack(fill="both")

# para mostrar el puntaje del Player
etq_pts_player = tk.Label(frame_1, text="Puntos Player")
etq_pts_player.config(bg="grey75", fg="black", border=2,
                      font="arial 10", justify="right")
etq_pts_player.place(relx=0.85, rely=0.2, width=100, height=30)

etq_pts_player_1 = tk.Entry(frame_1)
etq_pts_player_1.config(bg="white", fg="black", border=2,
                        font="arial 55", justify="right")
etq_pts_player_1.place(relx=0.85, rely=0.3, width=100, height=80)

# para mostrar el puntaje del crupier
etq_pts_crupier = tk.Label(frame_1, text="Puntos Crupier")
etq_pts_crupier.config(bg="grey75", fg="black", border=2,
                       font="arial 10", justify="right")
etq_pts_crupier.place(relx=0.85, rely=0.65, width=100, height=30)

etq_pts_crupier_1 = tk.Entry(frame_1)
etq_pts_crupier_1.config(bg="white", fg="black", border=2,
                         font="arial 55", justify="right")
etq_pts_crupier_1.place(relx=0.85, rely=0.75, width=100, height=80)


"""Frame 1_1   player"""

frame_player = LabelFrame(frame_1,  text='Player',
                          bd=0, bg='green', font='arial 16')
frame_player.grid(row=0, column=0, padx=10, pady=15)

player_label_1 = Label(frame_player, text='', bg='green')
player_label_1.grid(row=0, column=0, pady=10, padx=5)

player_lebel_2 = Label(frame_player, text='', bg='green')
player_lebel_2.grid(row=0, column=1, pady=10, padx=5)

player_label_3 = Label(frame_player, text='', bg='green')
player_label_3.grid(row=0, column=2, pady=10, padx=5)

player_label_4 = Label(frame_player, text='', bg='green')
player_label_4.grid(row=0, column=3, pady=10, padx=5)

player_label_5 = Label(frame_player, text='', bg='green')
player_label_5.grid(row=0, column=4, pady=10, padx=5)


"""Frame 1_2   Crupier"""
frame_crupier = LabelFrame(frame_1,  text='Crupier',
                           bd=0, bg='green', font='arial 16')
frame_crupier.grid(row=1, column=0, padx=10, pady=0)


crupier_label_1 = Label(frame_crupier, text='', bg='green')
crupier_label_1.grid(row=0, column=0, pady=10, padx=5)

crupier_label_2 = Label(frame_crupier, text='', bg='green')
crupier_label_2.grid(row=0, column=1, pady=10, padx=5)

crupier_label_3 = Label(frame_crupier, text='', bg='green')
crupier_label_3.grid(row=0, column=2, pady=10, padx=5)

crupier_label_4 = Label(frame_crupier, text='', bg='green')
crupier_label_4.grid(row=0, column=3, pady=10, padx=5)

crupier_label_5 = Label(frame_crupier, text='', bg='green')
crupier_label_5.grid(row=0, column=4, pady=10, padx=5)


"""Frame 2"""

frame_2 = Frame(ventana, width="900", height="100")
frame_2.config(background="green", bd=1, relief="solid")
frame_2.pack(expand=True, fill="both")


# se muestra el monto apuesta de la apuesta
etq_apuesta = tk.Label(frame_2, text="Valor Apuesta")
etq_apuesta.config(bg="grey75", fg="black", border=2,
                   font="arial 10", justify="right")
etq_apuesta.place(relx=0.01, rely=0.08, width=90, height=30)

# se muestra el monto apuesta de la apuesta
etq_apuesta_1 = tk.Entry(frame_2)
etq_apuesta_1.config(bg="white", fg="black", border=2,
                     font="arial 15", justify="right")
etq_apuesta_1.place(relx=0.12, rely=0.08, width=80, height=30)

# se muestra el saldo de la cuenta en pesos
etq_saldo = tk.Label(frame_2, text="Saldo")
etq_saldo.config(bg="grey75", fg="black", border=2,
                 font="arial 10", justify="right")
etq_saldo.place(relx=0.01, rely=0.6, width=90, height=30)

# se muestra el saldo de la cuenta en pesos
etq_saldo_1 = tk.Entry(frame_2)
etq_saldo_1.config(bg="white", fg="black", border=2,
                   font="arial 15", justify="right")
etq_saldo_1.place(relx=0.12, rely=0.6, width=80, height=30)

# boton de apuesta +10
btn_apuesta_10 = tk.Button(frame_2, text="Apuesta +$10", command=sumar_10)
btn_apuesta_10.config(bg="grey75", fg="black", font="arial 11")
btn_apuesta_10.place(
    relx=0.47, rely=0.3, width=110, height=35)

# boton de apuesta +20
btn_apuesta_20 = tk.Button(frame_2, text="Apuesta +$20",
                           command=sumar_20)
btn_apuesta_20.config(
    bg="grey75", fg="black", font="arial 11")
btn_apuesta_20.place(
    relx=0.6, rely=0.3, width=110, height=35)


# boton de apuesta +50
btn_apuesta_50 = tk.Button(frame_2, text="Apuesta +$50", command=sumar_50)
btn_apuesta_50.config(bg="grey75", fg="black", font="arial 11")
btn_apuesta_50.place(relx=0.73, rely=0.3, width=110, height=35)

# boton de apuesta +100
btn_apuesta_100 = tk.Button(frame_2, text="Apuesta +$100", command=sumar_100)
btn_apuesta_100.config(bg="grey75", fg="black", font="arial 11")
btn_apuesta_100.place(relx=0.86, rely=0.3, width=110, height=35)

# boton pedir otra carta
btn_pedir = tk.Button(frame_2, text="Pedir",
                      command=continuar_jugando)
btn_pedir.config(bg="grey75", fg="black", font="arial12")
btn_pedir.place(relx=0.235, rely=0.2, width=90, height=55)

# boton para pasar y crupier juega auto
btn_pasar = tk.Button(frame_2, text="Pasar",
                      command=detener_pasar)
btn_pasar.config(bg="grey75", fg="black", font="arial12")
btn_pasar.place(relx=0.345, rely=0.2, width=90, height=55)


"""Frame 3"""
# frame pie, donde esta boton tutorial
frame_3 = Frame(ventana, width="900", height="200")
frame_3.config(background="grey75", bd=0)
frame_3.pack(expand=True, fill="both")

# boton tutorial
btn_tuto = tk.Button(frame_3, text="Tutorial", command=ver_tuto, )
btn_tuto.config(bg="green4", fg="white", font="arial 12")
btn_tuto.place(rely=0.1, relx=0.45, width=70, height=30)

# iniciamos mostrando una carta de cada jugador al reves

# asignamos a carta el valor de calta oculta
carta = 'carta_oculta'
# se inicia con una carta dada vuelta para cada jugador, solo para buena impresion grafica
crupier_img1 = size_cards(f'src/img/cards/{carta}.png')
crupier_label_1.config(image=crupier_img1)
player_img1 = size_cards(f'src/img/cards/{carta}.png')
player_label_1.config(image=player_img1)
# seteamos valo apuesta a 0(cero)
suma_apuesta = 0
# se inicializa el saldo para jugar
saldo = 1000
mano_player = []
mano_crupier = []
# muerstra el saldo
mostrar_saldo()
# muestra total de apuestas
mostrar_suma_apuesta()
# se inicia  preguntando si desea comenzar a jugar o abandonar el juego
desea_comenzar()


ventana.mainloop()
