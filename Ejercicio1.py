import tkinter as tk                   # Importa el módulo principal de Tkinter para interfaces gráficas
from tkinter import ttk, messagebox    # Importa ttk para widgets modernos y messagebox para mostrar mensajes emergentes

# ---------------------- FUNCIONES DE PROCESAMIENTO DE TEXTO ----------------------

def invertir_palabras(frase):
    """
    Invierte el orden de las palabras en la frase.
    Ejemplo: "Hola mundo bonito" -> "bonito mundo Hola"
    """
    palabras = frase.strip().split()   # Elimina espacios y separa la frase en palabras
    pila = list(palabras)              # Crea una copia de la lista de palabras (simula una pila)
    resultado = []
    while pila:                        # Mientras la pila tenga elementos
        resultado.append(pila.pop())   # Saca la última palabra y la agrega al resultado
    return ' '.join(resultado)         # Une las palabras invertidas en una sola cadena

def invertir_letras(frase):
    """
    Invierte las letras de cada palabra, pero mantiene el orden de las palabras.
    Ejemplo: "Hola mundo" -> "aloH odnum"
    """
    return ' '.join([palabra[::-1] for palabra in frase.strip().split()])

def invertir_completo(frase):
    """
    Invierte completamente la frase (letras y palabras).
    Ejemplo: "Hola mundo" -> "odnum aloH"
    """
    palabras = invertir_palabras(frase)  # Invierte el orden de las palabras
    return palabras[::-1]                # Invierte todos los caracteres de la frase resultante

def contar_palabras(frase):
    """
    Cuenta el número de palabras en la frase.
    """
    return f"Número de palabras: {len(frase.strip().split())}"

def ordenar_alfabetico(frase):
    """
    Ordena las palabras de la frase alfabéticamente (ignorando mayúsculas/minúsculas).
    """
    palabras = sorted(frase.strip().split(), key=lambda x: x.lower())
    return ' '.join(palabras)

# ---------------------- FUNCIÓN PRINCIPAL DE EJECUCIÓN ----------------------

def ejecutar():
    """
    Obtiene la frase y la opción seleccionada, ejecuta la función correspondiente
    y muestra el resultado en la interfaz.
    """
    frase = entrada.get("1.0", tk.END).strip()   # Obtiene el texto de la caja de entrada
    if not frase:
        messagebox.showwarning("Entrada vacía", "Por favor, escribe una frase.")  # Muestra advertencia si está vacío
        return

    opcion = opciones.get()                      # Obtiene la opción seleccionada del combobox
    if opcion == "Invertir palabras":
        resultado = invertir_palabras(frase)
    elif opcion == "Invertir letras de cada palabra":
        resultado = invertir_letras(frase)
    elif opcion == "Invertir completamente":
        resultado = invertir_completo(frase)
    elif opcion == "Contar palabras":
        resultado = contar_palabras(frase)
    elif opcion == "Ordenar alfabéticamente":
        resultado = ordenar_alfabetico(frase)
    else:
        resultado = "Opción no válida"

    resultado_var.set(resultado)                 # Muestra el resultado en la etiqueta de la interfaz

# ---------------------- CONFIGURACIÓN DE LA INTERFAZ GRÁFICA ----------------------

ventana = tk.Tk()                               # Crea la ventana principal
ventana.title("🌀 Inversor de Frases Avanzado") # Título de la ventana
ventana.geometry("600x400")                     # Tamaño de la ventana
ventana.config(bg="#e8f0fe")                    # Color de fondo
ventana.resizable(False, False)                 # No permite cambiar el tamaño

# Título principal
ttk.Label(
    ventana,
    text="Herramienta de Inversión de Texto",
    font=("Arial", 16, "bold"),
    background="#e8f0fe"
).pack(pady=10)

# Caja de entrada de texto multilínea
entrada = tk.Text(
    ventana,
    font=("Arial", 12),
    height=4,
    width=60
)
entrada.pack(pady=10)

# Etiqueta para seleccionar opción
ttk.Label(
    ventana,
    text="Seleccione una opción:",
    background="#e8f0fe"
).pack()

# Combobox con las opciones de acción
opciones = ttk.Combobox(
    ventana,
    state="readonly",
    font=("Arial", 12),
    width=35
)
opciones['values'] = (
    "Invertir palabras",
    "Invertir letras de cada palabra",
    "Invertir completamente",
    "Contar palabras",
    "Ordenar alfabéticamente"
)
opciones.current(0)    # Selecciona la primera opción por defecto
opciones.pack(pady=5)

# Botón para ejecutar la acción seleccionada
ttk.Button(
    ventana,
    text="Ejecutar",
    command=ejecutar
).pack(pady=10)

# Etiqueta para mostrar el resultado
resultado_var = tk.StringVar()   # Variable para almacenar el resultado
resultado_label = ttk.Label(
    ventana,
    textvariable=resultado_var,
    font=("Arial", 12, "italic"),
    background="#e8f0fe",
    wraplength=500
)
resultado_label.pack(pady=20)

ventana.mainloop()   # Inicia el bucle principal de la interfaz gráfica