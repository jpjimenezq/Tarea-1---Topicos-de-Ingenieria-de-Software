import tkinter as tk
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def guardarNombre():
    nombre = entrada.get()
    try:
        conexion = mysql.connector.connect(
            host=os.getenv("HOST_DB"),
            user=os.getenv("USER_DB"),
            password=os.getenv("PASSWORD_DB"),
            database=os.getenv("DATABASE_DB")
        )

        cursor = conexion.cursor()
        cursor.execute("INSERT INTO usuarios (nombre) VALUES (%s)", (nombre,))
        conexion.commit()
        cursor.close()
        conexion.close()

        etiqueta_resultado.config(text=f"Hola, {nombre}! Tu nombre ha sido guardado.", fg="green")
        entrada.delete(0, tk.END)
    except Exception as e:
        etiqueta_resultado.config(text=f"Error al guardar el nombre: {str(e)}", fg="red")

ventana = tk.Tk()
ventana.title("Guardar Nombre")
ventana.state('zoomed')

frame_centro = tk.Frame(ventana)
frame_centro.place(relx=0.5, rely=0.5, anchor='center')

etiqueta = tk.Label(frame_centro, text="¿Cómo te llamas?", font=("Arial", 18))
etiqueta.pack(pady=10)

entrada = tk.Entry(frame_centro, font=("Arial", 16))
entrada.pack(pady=10)

boton = tk.Button(frame_centro, text="Guardar", command=guardarNombre, font=("Arial", 16))
boton.pack(pady=10)

etiqueta_resultado = tk.Label(frame_centro, text="", font=("Arial", 18))
etiqueta_resultado.pack(pady=10)

ventana.mainloop()
