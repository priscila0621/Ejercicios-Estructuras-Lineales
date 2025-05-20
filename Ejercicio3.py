import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import random

class Cancion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None
        self.anterior = None

class ListaReproduccion:
    def __init__(self):
        self.primera = None
        self.actual = None
        self.modo_aleatorio = False

    def agregar_cancion(self, nombre):
        nueva = Cancion(nombre)
        if not self.primera:
            self.primera = self.actual = nueva
        else:
            temp = self.primera
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = nueva
            nueva.anterior = temp

    def eliminar_cancion(self, nombre):
        temp = self.primera
        while temp:
            if temp.nombre == nombre:
                if temp.anterior:
                    temp.anterior.siguiente = temp.siguiente
                else:
                    self.primera = temp.siguiente
                if temp.siguiente:
                    temp.siguiente.anterior = temp.anterior
                if self.actual == temp:
                    self.actual = temp.siguiente or temp.anterior
                return True
            temp = temp.siguiente
        return False

    def siguiente_cancion(self):
        if self.modo_aleatorio:
            canciones = self.obtener_lista()
            if canciones:
                self.actual = random.choice([c for c in canciones if c != self.actual])
        elif self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente

    def anterior_cancion(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior

    def repetir(self):
        return self.actual.nombre if self.actual else "No hay canción."

    def buscar(self, nombre):
        temp = self.primera
        while temp:
            if temp.nombre == nombre:
                return True
            temp = temp.siguiente
        return False

    def obtener_lista(self):
        lista = []
        temp = self.primera
        while temp:
            lista.append(temp)
            temp = temp.siguiente
        return lista

    def guardar_lista(self, archivo):
        with open(archivo, 'w') as f:
            for cancion in self.obtener_lista():
                f.write(cancion.nombre + '\n')

    def cargar_lista(self, archivo):
        with open(archivo, 'r') as f:
            for linea in f:
                self.agregar_cancion(linea.strip())

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("🎵 Reproductor de Música Creativo 🎵")
        self.root.geometry("600x500")
        self.root.configure(bg='#d0e1f9')

        self.lista = ListaReproduccion()

        self.etiqueta = tk.Label(root, text="🎶 Canción actual: Ninguna", font=("Helvetica", 14), bg='#d0e1f9', fg='#003366')
        self.etiqueta.pack(pady=15)

        botones = [
            ("➕ Agregar Canción", self.agregar),
            ("➖ Eliminar Canción", self.eliminar),
            ("⏭️ Siguiente", self.siguiente),
            ("⏮️ Anterior", self.anterior),
            ("🔁 Repetir", self.repetir),
            ("🔀 Modo Aleatorio", self.toggle_aleatorio),
            ("🔍 Buscar Canción", self.buscar),
            ("📜 Mostrar Lista", self.mostrar_lista),
            ("💾 Guardar Lista", self.guardar),
            ("📂 Cargar Lista", self.cargar),
        ]

        for texto, comando in botones:
            b = tk.Button(root, text=texto, command=comando, width=30, bg='#88c9bf', fg='black', font=("Helvetica", 12, "bold"))
            b.pack(pady=3)

    def actualizar_etiqueta(self):
        actual = self.lista.actual.nombre if self.lista.actual else "Ninguna"
        self.etiqueta.config(text=f"🎶 Canción actual: {actual}")

    def agregar(self):
        nombre = simpledialog.askstring("Agregar", "Nombre de la canción:")
        if nombre:
            self.lista.agregar_cancion(nombre)
            self.actualizar_etiqueta()

    def eliminar(self):
        nombre = simpledialog.askstring("Eliminar", "Nombre de la canción a eliminar:")
        if nombre:
            if self.lista.eliminar_cancion(nombre):
                messagebox.showinfo("Éxito", "Canción eliminada.")
            else:
                messagebox.showwarning("Error", "Canción no encontrada.")
            self.actualizar_etiqueta()

    def siguiente(self):
        self.lista.siguiente_cancion()
        self.actualizar_etiqueta()

    def anterior(self):
        self.lista.anterior_cancion()
        self.actualizar_etiqueta()

    def repetir(self):
        if self.lista.actual:
            messagebox.showinfo("Repetir", f"Reproduciendo de nuevo: {self.lista.repetir()}")
        self.actualizar_etiqueta()

    def toggle_aleatorio(self):
        self.lista.modo_aleatorio = not self.lista.modo_aleatorio
        estado = "activado" if self.lista.modo_aleatorio else "desactivado"
        messagebox.showinfo("Modo Aleatorio", f"Modo aleatorio {estado}.")

    def buscar(self):
        nombre = simpledialog.askstring("Buscar", "Nombre de la canción a buscar:")
        if nombre:
            encontrado = self.lista.buscar(nombre)
            msg = "encontrada ✅" if encontrado else "no está ❌"
            messagebox.showinfo("Buscar", f"La canción {msg}.")

    def mostrar_lista(self):
        canciones = [c.nombre for c in self.lista.obtener_lista()]
        if canciones:
            messagebox.showinfo("Lista", "\n".join(canciones))
        else:
            messagebox.showinfo("Lista", "La lista está vacía.")

    def guardar(self):
        archivo = filedialog.asksaveasfilename(defaultextension=".txt")
        if archivo:
            self.lista.guardar_lista(archivo)
            messagebox.showinfo("Guardar", "Lista guardada exitosamente.")

    def cargar(self):
        archivo = filedialog.askopenfilename()
        if archivo:
            self.lista = ListaReproduccion()
            self.lista.cargar_lista(archivo)
            self.actualizar_etiqueta()
            messagebox.showinfo("Cargar", "Lista cargada correctamente.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()
