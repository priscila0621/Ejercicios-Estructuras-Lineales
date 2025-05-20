import tkinter as tk
from tkinter import ttk, messagebox

# Función para verificar paréntesis balanceados y detectar errores
def verificar_balanceo_detallado(cadena):
    """
    Verifica si los paréntesis (), {}, [] están balanceados en la cadena.
    Si hay un error, indica el tipo de paréntesis y la posición exacta (empezando en 1).
    Devuelve: (balanceado: bool, mensaje: str, resumen: dict)
    """
    pila = []
    pares = {')': '(', '}': '{', ']': '['}
    resumen = {'(': 0, ')': 0, '{': 0, '}': 0, '[': 0, ']': 0}

    for i, char in enumerate(cadena):
        if char in '({[':
            pila.append((char, i))
            resumen[char] += 1
        elif char in ')}]':
            resumen[char] += 1
            if not pila:
                # No hay apertura correspondiente
                return False, f"Error: paréntesis de cierre '{char}' sin apertura en posición {i+1}.", resumen
            ultimo, pos_ultimo = pila[-1]
            if ultimo != pares[char]:
                # Paréntesis de cierre no coincide con el de apertura
                return False, (
                    f"Error: paréntesis de cierre '{char}' en posición {i+1} no coincide con "
                    f"el de apertura '{ultimo}' en posición {pos_ultimo+1}."
                ), resumen
            pila.pop()

    if pila:
        # Hay paréntesis de apertura sin cerrar
        char, pos = pila[-1]
        return False, f"Error: paréntesis de apertura '{char}' sin cerrar en posición {pos+1}.", resumen

    return True, "✅ Paréntesis balanceados correctamente.", resumen

# Sugerencia de corrección automática de paréntesis
def corregir_parentesis(cadena):
    pila = []
    resultado = []
    pares = {')': '(', '}': '{', ']': '['}
    apertura = {'(': ')', '{': '}', '[': ']'}
    # Recorre la cadena y construye el resultado corrigiendo sobre la marcha
    for char in cadena:
        if char in '({[':
            pila.append(char)
            resultado.append(char)
        elif char in ')}]':
            if pila and pila[-1] == pares[char]:
                pila.pop()
                resultado.append(char)
            else:
                # Si hay un cierre sin apertura, lo ignoramos (lo quitamos)
                continue
        else:
            resultado.append(char)
    # Al final, agregamos los cierres faltantes
    while pila:
        resultado.append(apertura[pila.pop()])
    return ''.join(resultado)

# ---------------------- INTERFAZ GRÁFICA ----------------------

ventana = tk.Tk()
ventana.title("🧠 Analizador de Paréntesis Balanceados")
ventana.geometry("650x450")
ventana.config(bg="#f5f8fc")
ventana.resizable(False, False)

# Título principal
ttk.Label(
    ventana,
    text="🔍 Verificador de Paréntesis ( ) [ ] { }",
    font=("Arial", 16, "bold"),
    background="#f5f8fc"
).pack(pady=10)

# Caja de entrada de texto
entrada = tk.Text(
    ventana,
    font=("Arial", 12),
    height=5,
    width=70
)
entrada.pack(pady=10)

# Botón para verificar
ttk.Button(
    ventana,
    text="Verificar",
    command=lambda: ejecutar_verificacion()
).pack(pady=5)

# Variables para mostrar resultados
resultado_var = tk.StringVar()
conteo_var = tk.StringVar()

# Etiqueta de resultado principal
resultado_label = ttk.Label(
    ventana,
    textvariable=resultado_var,
    font=("Arial", 13, "italic"),
    background="#f5f8fc"
)
resultado_label.pack(pady=10)

# Etiqueta de conteo de paréntesis
ttk.Label(
    ventana,
    text="📊 Conteo de Paréntesis:",
    background="#f5f8fc",
    font=("Arial", 12, "bold")
).pack()
conteo_label = ttk.Label(
    ventana,
    textvariable=conteo_var,
    font=("Consolas", 11),
    background="#f5f8fc"
)
conteo_label.pack(pady=5)

# Función para mostrar resultado
def ejecutar_verificacion():
    texto = entrada.get("1.0", tk.END).strip()
    if not texto:
        messagebox.showwarning("Entrada vacía", "Por favor ingrese una expresión.")
        return

    balanceado, mensaje, resumen = verificar_balanceo_detallado(texto)
    resultado_var.set(mensaje)
    resultado_label.config(foreground="green" if balanceado else "red")

    # Mostrar conteo de paréntesis
    resumen_text = (
        f"( : {resumen['(']}    ) : {resumen[')']}\n"
        f"{{ : {resumen['{']}}}    }} : {resumen['}']}\n"
        f"[ : {resumen['[']}    ] : {resumen[']']}"
    )
    conteo_var.set(resumen_text)

# Función para copiar resultado
def copiar_resultado():
    ventana.clipboard_clear()
    ventana.clipboard_append(resultado_var.get())
    ventana.update()
    messagebox.showinfo("Copiado", "Resultado copiado al portapapeles.")

# Función para mostrar la corrección
def mostrar_correccion():
    texto = entrada.get("1.0", tk.END).strip()
    if not texto:
        messagebox.showwarning("Entrada vacía", "Por favor ingrese una expresión.")
        return
    corregido = corregir_parentesis(texto)
    messagebox.showinfo("Cadena Corregida", f"Expresión balanceada:\n{corregido}")

# Botón copiar resultado
ttk.Button(ventana, text="Copiar resultado", command=copiar_resultado).pack(pady=10)

# Botón para corregir paréntesis
ttk.Button(ventana, text="Corregir paréntesis", command=mostrar_correccion).pack(pady=5)

ventana.mainloop()


'''
Ejemplo de uso
Mi amiga Laura (quien siempre ha sido muy puntual, aunque últimamente [especialmente desde que empezó su nuevo trabajo], ha estado llegando tarde a nuestras reuniones).
'''