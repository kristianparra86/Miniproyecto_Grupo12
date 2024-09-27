import tkinter as tk
from tkinter import messagebox
import random
import os
from PIL import Image, ImageTk
import tkinter.font as tkFont
import sys
# Ruta del ícono, imagen de fondo y fuente (definida globalmente para que esté disponible después de compilar)
#pyinstaller --onefile --name="ElAhorcado" --windowed --icon="C:\\Users\\wbenitez\\Downloads\\Gitl\\img/icon/Ahorcado_icon.ico" --add-data "C:\\Users\\wbenitez\\Downloads\\Git\\informatorio2024-will\\fondo2.png;src" --add-data "C:\\Users\\wbenitez\\Downloads\\Git\\informatorio2024-will\\Roboto-Regular.ttf;src/fonts" --distpath "C:/Proyectos Informatorio" "C:/Users/wbenitez/Downloads/Git/informatorio2024-will/Ejercicios_ejemplos/ahorcadotkv2.py"

if hasattr(sys, '_MEIPASS'):
    ICON_PATH = os.path.join(sys._MEIPASS, "img/icon/Ahorcado_icon.ico")
    BACKGROUND_IMAGE_PATH = os.path.join(sys._MEIPASS, "img/background/Ahorcado.png")
    FONT_PATH = os.path.join(sys._MEIPASS, "src", "fonts", "Roboto-Regular.ttf")
else:
    ICON_PATH = os.path.join(os.path.dirname(__file__), "img/icon/Ahorcado_icon.ico")
    BACKGROUND_IMAGE_PATH = os.path.join(os.path.dirname(__file__), "img/background/Ahorcado.png")
    FONT_PATH = os.path.join(os.path.dirname(__file__), "src", "fonts", "Roboto-Regular.ttf")
# Diccionarios de palabras por temáticas
palabras_por_tematica = {
    "Frutas": ["manzana", "banana", "naranja", "pera", "uva", "mango", "limon", "kiwi", "sandia", "melon", 
               "fresa", "cereza", "ciruela", "durazno", "granada", "higo", "papaya", "piña", "frambuesa", 
               "grosella", "arándano", "mandarina", "pomelo", "guayaba", "lichi"],
    "Utensilios de cocina": ["cuchillo", "tenedor", "cuchara", "sarten", "olla", "colador", "batidora", 
                             "licuadora", "tostadora", "cafetera", "tetera", "rallador", "cacerola", "espumadera", 
                             "abrelatas", "pinzas", "mortero", "rodillo", "espátula", "cucharon", "cuchillo", 
                             "pelador", "tabla", "vaso", "plato"],
    "Países": ["argentina", "brasil", "canada", "dinamarca", "egipto", "francia", "alemania", "hungria", 
               "india", "japon", "kenia", "libano", "mexico", "nepal", "oman", "portugal", "qatar", 
               "rusia", "suecia", "turquia", "uruguay", "vietnam", "yemen", "zambia", "zimbabwe"],
    "Palabras reservadas en Python": ["False", "None", "True", "and", "as", "assert", "async", "await", 
                                      "break", "class", "continue", "def", "del", "elif", "else", "except", 
                                      "finally", "for", "from", "global", "if", "import", "in", "is", "lambda", 
                                      "nonlocal", "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"]
}

class Ahorcado:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego del Ahorcado")

        # Establecer tamaño de la ventana y hacer que no sea redimensionable
        self.root.geometry("400x450")  # Tamaño de la ventana: 400x450 píxeles
        self.centrar_ventana(400, 450)  # Centra la ventana en la pantalla
        self.root.resizable(False, False)  # Deshabilitar la redimensión de la ventana
        self.custom_bold_font_large = tkFont.Font(family="Roboto", size=14, weight="bold")

        # Establecer el ícono de la ventana
        if os.path.exists(ICON_PATH):
            self.root.iconbitmap(ICON_PATH)
        else:
            print(f"Advertencia: El ícono no se encuentra en {ICON_PATH}")
        
        # Cargar la imagen de fondo
        if os.path.exists(BACKGROUND_IMAGE_PATH):
            self.background_image = Image.open(BACKGROUND_IMAGE_PATH)
            self.background_image = self.background_image.resize((400, 450), Image.Resampling.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(self.background_image)
        else:
            print(f"Advertencia: La imagen de fondo no se encuentra en {BACKGROUND_IMAGE_PATH}")
            self.bg_photo = None

        # Crear un Canvas para colocar la imagen de fondo
        self.canvas = tk.Canvas(self.root, width=400, height=450)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Cargar la fuente Roboto-Regular y crear la fuente en negrita
        self.custom_font = tkFont.Font(family="Roboto", size=10)
        self.bold_font = tkFont.Font(family="Roboto", size=10, weight="bold")
        
        # Variables del juego
        self.tematica = tk.StringVar(value="Frutas")
        self.intentos_restantes = 5
        self.palabra_secreta = ""
        self.letras_adivinadas = set()
        self.progreso = []

        # Configuración de la interfaz
        self.setup_ui()

    def centrar_ventana(self, width, height):
        # Obtener el tamaño de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcular la posición x e y para centrar la ventana
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # Establecer la geometría de la ventana para que aparezca centrada
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def setup_ui(self):
        # Menú de selección de temática
        tk.Label(self.canvas, text="Selecciona una temática:", font=self.custom_bold_font_large, bg="#ffffff", fg="#51727E").place(x=200, y=20, anchor="center")
        y_offset = 60
        for tematica in palabras_por_tematica.keys():
            tk.Radiobutton(self.canvas, text=tematica, variable=self.tematica, value=tematica, bg="#ffffff", highlightthickness=0, font=self.custom_font).place(x=20, y=y_offset)
            y_offset += 30

        # Botones de control
        tk.Button(self.canvas, text="Comenzar a jugar", command=self.iniciar_juego, bg="#ffffff", font=self.bold_font).place(relx=0.5, y=220, anchor="center")
        tk.Button(self.canvas, text="Salir", command=self.root.quit, bg="#ffffff", font=self.bold_font).place(x=195, y=260, anchor="center")

        # Mostrar intentos restantes
        self.label_intentos = tk.Label(self.canvas, text=f"Intentos restantes: {self.intentos_restantes}",  font=self.bold_font, fg="red", bg="#ffffff")
        self.label_intentos.place(x=130, y=300)

        # Mostrar progreso (centrado) - ReadOnly
        self.label_progreso = tk.Label(self.canvas, text="Progreso:", font=self.bold_font, bg="#ffffff")
        self.label_progreso.place(relx=0.5, y=330, anchor="center")

        self.entrada_progreso = tk.Entry(self.canvas, justify="center", state="readonly", font=self.custom_font)
        self.entrada_progreso.place(relx=0.5, y=360, anchor="center", width=200)

        # Entrada para adivinar letras
        self.entrada_letra = tk.Entry(self.canvas, font=self.custom_font, width=5, justify="center")
        self.entrada_letra.place(relx=0.5, y=390, anchor="center")

        # Botón para adivinar letra (inicialmente deshabilitado)
        self.boton_adivinar = tk.Button(self.canvas, text="Adivinar letra", command=self.adivinar_letra, bg="#ffffff", state="disabled", font=self.bold_font)
        self.boton_adivinar.place(relx=0.5, y=420, anchor="center")

    def iniciar_juego(self):
        self.intentos_restantes = 5
        self.letras_adivinadas = set()
        self.palabra_secreta = obtener_palabra_secreta(self.tematica.get()).lower()
        self.progreso = ["_"] * len(self.palabra_secreta)
        self.actualizar_pantalla()

        # Habilitar el botón de adivinar letra
        self.boton_adivinar.config(state="normal")

    def actualizar_pantalla(self):
        self.label_intentos.config(text=f"Intentos restantes: {self.intentos_restantes}")
        self.entrada_progreso.config(state="normal")
        self.entrada_progreso.delete(0, tk.END)
        self.entrada_progreso.insert(0, " ".join(self.progreso))
        self.entrada_progreso.config(state="readonly")

    def validar_entrada(self, texto):
        # Validar que la entrada sea una letra y que solo sea una
        return len(texto) == 1 and texto.isalpha()

    def adivinar_letra(self):
        letra = self.entrada_letra.get().lower()

        # Validar la entrada antes de continuar
        if not self.validar_entrada(letra):
            self.centrar_popup("Entrada inválida", "Por favor, ingresa solo una letra.")
            self.entrada_letra.delete(0, tk.END)
            return

        if letra in self.letras_adivinadas:
            self.centrar_popup("Letra repetida", "Ya has adivinado esa letra. Intenta con otra.")
            self.entrada_letra.delete(0, tk.END)  # Borrar el contenido del campo de entrada
            return

        self.letras_adivinadas.add(letra)

        if letra in self.palabra_secreta:
            for i, char in enumerate(self.palabra_secreta):
                if char == letra:
                    self.progreso[i] = letra
            if "_" not in self.progreso:
                self.centrar_popup("Ganaste", f"¡Felicidades! Has adivinado la palabra: {self.palabra_secreta}")
                self.iniciar_juego()
        else:
            self.intentos_restantes -= 1
            if self.intentos_restantes == 0:
                self.centrar_popup("Perdiste", f"¡Perdiste! La palabra secreta era: {self.palabra_secreta}")
                self.iniciar_juego()

        self.entrada_letra.delete(0, tk.END)  # Asegurarse de borrar el contenido del campo de entrada después de procesar
        self.actualizar_pantalla()

    def centrar_popup(self, titulo, mensaje):
        # Crear un pop-up centrado
        popup = tk.Toplevel(self.root)
        popup.title(titulo)
        popup.geometry("300x100")

        # Centrar el pop-up en la ventana principal
        popup_x = self.root.winfo_x() + (self.root.winfo_width() // 2) - 150
        popup_y = self.root.winfo_y() + (self.root.winfo_height() // 2) - 50
        popup.geometry(f"+{popup_x}+{popup_y}")

        tk.Label(popup, text=mensaje, wraplength=250, font=self.custom_font).pack(pady=10)
        tk.Button(popup, text="OK", command=popup.destroy, font=self.bold_font).pack(pady=10)

def obtener_palabra_secreta(tematica):
    return random.choice(palabras_por_tematica[tematica])

if __name__ == "__main__":
    root = tk.Tk()
    juego = Ahorcado(root)
    root.mainloop()
