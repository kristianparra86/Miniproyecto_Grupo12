import tkinter as tk
from tkinter import messagebox


class Triangulo_magico:
    def __init__(self):
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title("Triángulo Mágico")
        self.ventana_principal.geometry("600x450+200+180")
        self.ventana_principal.config(bg="olivedrab")
        self.ventana_principal.iconbitmap("src/img/icon/Triangulo_icon.ico")

        etiqueta_bienvenida = tk.Label(self.ventana_principal, text="¡Bienvenido al juego del Triángulo Mágico!")
        etiqueta_bienvenida.pack(pady=15)
        etiqueta_bienvenida.config(fg="snow", font=("Times New Roman", 14, "bold"), bg="olivedrab")

        etiqueta_instrucciones = tk.Label(self.ventana_principal, text="Ingresa 6 números enteros, entre 1 y 99, para formar un triángulo mágico. ¡Suerte!")
        etiqueta_instrucciones.pack()
        etiqueta_instrucciones.config(font=("Helvetica", 11, "bold"), bg="olivedrab")

        self.marco_entradas = tk.Frame(self.ventana_principal, bg="olivedrab")
        self.marco_entradas.pack(pady=50, padx=20)

        self.entrada_1 = tk.Entry(self.marco_entradas, width=5)
        self.entrada_1.grid(row=0, column=2)
        self.entrada_1.config(borderwidth=2, relief="solid", justify="center", font=("Times New Roman", 14), bg="orange2")

        self.entrada_2 = tk.Entry(self.marco_entradas, width=5)
        self.entrada_2.grid(row=1, column=1)
        self.entrada_2.config(borderwidth=2, relief="solid", justify="center", font=("Times New Roman", 14), bg="orange2")

        self.entrada_3 = tk.Entry(self.marco_entradas, width=5)
        self.entrada_3.grid(row=1, column=3)
        self.entrada_3.config(borderwidth=2, relief="solid", justify="center", font=("Times New Roman", 14), bg="orange2")

        self.entrada_4 = tk.Entry(self.marco_entradas, width=5)
        self.entrada_4.grid(row=2, column=0)
        self.entrada_4.config(borderwidth=2, relief="solid", justify="center", font=("Times New Roman", 14), bg="orange2")

        self.entrada_5 = tk.Entry(self.marco_entradas, width=5)
        self.entrada_5.grid(row=2, column=2)
        self.entrada_5.config(borderwidth=2, relief="solid", justify="center", font=("Times New Roman", 14), bg="orange2")

        self.entrada_6 = tk.Entry(self.marco_entradas, width=5)
        self.entrada_6.grid(row=2, column=4)
        self.entrada_6.config(borderwidth=2, relief="solid", justify="center", font=("Times New Roman", 14), bg="orange2")

        self.entradas = [self.entrada_1, self.entrada_2, self.entrada_3, self.entrada_4, self.entrada_5, self.entrada_6]

        self.botones_de_accion = tk.Frame(self.ventana_principal, bg="olivedrab")
        self.botones_de_accion.pack()
        self.botones_de_accion.rowconfigure(0, weight=1)
        self.botones_de_accion.columnconfigure(0, weight=1)

        self.boton_jugar = tk.Button(self.botones_de_accion, text="Jugar", command=self.jugar, width=8, height=1, bg="lawn green", fg="blue", font=("Calibri", 14, "bold"))
        self.boton_jugar.grid(row=0, column=1, sticky="nsew", pady=20)
        self.boton_reiniciar = tk.Button(self.botones_de_accion, text="Reiniciar", command=self.reiniciar, width=6, height=1, bg="yellow2", font=("Calibri", 11, "bold"))
        self.boton_reiniciar.grid(row=1, column=0, pady=20, padx=30)
        self.boton_ayuda = tk.Button(self.botones_de_accion, text="Ayuda", command=self.ayuda, width=6, height=1, bg="goldenrod1", font=("Calibri", 11, "bold"))
        self.boton_ayuda.grid(row=1, column=1, pady=20, padx=30)
        self.boton_salir = tk.Button(self.botones_de_accion, text="Salir", command=self.ventana_principal.quit, width=6, height=1, bg="orangered2", font=("Calibri", 11, "bold"))
        self.boton_salir.grid(row=1, column=2, pady=20, padx=30)

        self.contador_intentos = 3

        self.ventana_principal.mainloop()

    def jugar(self):
        numeros = []
        for entry in self.entradas:
            try:
                num = int(entry.get())
                if num in numeros or not 1 <= num <= 99:
                    messagebox.showerror("Error", "Por favor, ingresa numeros que estén en el rango de 1 al 99. Si queres conocer más acerca de cómo crear un Triángulo Mágico presioná Ayuda.")
                    return
                numeros.append(num)
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingresa solo números enteros. Si queres conocer más acerca de cómo crear un Triángulo Mágico presioná Ayuda.")
                return

        if len(numeros) != 6:
            messagebox.showerror("Error", "Debes ingresar 6 números.")
            return
        self.contador_intentos -= 1

        if self.es_magico(numeros):
            self.mensaje_final_ganador()

        else:
            self.limpiar_campos()
            if self.contador_intentos == 0:
                self.mostrar_mensaje_final()
            else:
                messagebox.showwarning("¡Inténtalo de nuevo!", f"Lo siento, el triángulo no es Mágico. Te quedan {self.contador_intentos} intentos.")

    def limpiar_campos(self):
        for entry in self.entradas:
            entry.delete(0, tk.END)


    def es_magico(self, numeros):
        
        triangulo = [
            [numeros[0], numeros[1], numeros[3]],
            [numeros[0], numeros[2], numeros[5]],
            [numeros[3], numeros[4], numeros[5]]
        ]

        suma_lado_1 = sum(triangulo[0])
        suma_lado_2 = sum(triangulo[1])
        suma_lado_3 = sum(triangulo[2])

        if suma_lado_1 == suma_lado_2 == suma_lado_3:
            return True
        else:
            return False

    def reiniciar(self):
        for entry in self.entradas:
            entry.delete(0, tk.END)
        self.contador_intentos = 3

    def ayuda(self):
        ventana_ayuda = tk.Toplevel(self.ventana_principal, bg="lightcyan2")
        ventana_ayuda.geometry("700x210+100+80")
        ventana_ayuda.title("Ayuda")
        etiqueta_ayuda = tk.Label(ventana_ayuda, pady=20, font=("Times New Roman", 12, "bold"), bg="lightcyan2")
        etiqueta_ayuda.config(text="Un Triángulo Mágico, es un juego sencillo de ingenio matemático, que se compone de seis casillas\n"
                            "y consiste en ingresar seis valores numéricos naturales en los espacios disponibles, sin repetición\n"
                            "de manera tal que al hacer la suma recta de cada lado del triangulo, \n"
                            "ésta obtenga como resultado el mismo número para los tres lados del triángulo.")   
        etiqueta_ayuda.pack()

        boton_ayuda_cerrar = tk.Button(ventana_ayuda, text="Cerrar", command=ventana_ayuda.destroy, width=6, height=1, bg="brown1", font=("Calibri", 10))
        boton_ayuda_cerrar.pack(pady=20)

    def mostrar_mensaje_final(self):
        resultado = messagebox.askquestion("Fin del juego", "Lo siento, te quedaste sin intentos. ¿Quieres volver a jugar?")
        if resultado == 'yes':
            self.reiniciar()
        else:
            self.ventana_principal.quit()
    
    def mensaje_final_ganador(self):
        resultado = messagebox.askquestion("¡Muy bien hecho!", "Haz completado un Triángulo Mágico. ¿Quieres volver a jugar?")
        if resultado == 'yes':
            self.reiniciar()
        else:
            self.ventana_principal.quit()

if __name__ == "__main__":
    juego = Triangulo_magico()