# importaciones de bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

# Desarrollo de la interfaz grafica

root = Tk()
root.title("Aplicacion CRUD con base de datos")
root.geometry("600X350")

miId = StringVar()
miNombre = StringVar()
miCargo = StringVar()
miSalario = StringVar()

def conexionBBDD():
    miConexion=sqlite3.connect("base")
    miCursor=miConexion.curtsor()

    try:
        miCursor.execute('''
            CREATE TABLE empleado(
                ID INTEGER PRIMARY KEY AUTOINCREMENT
                NOMBRE VARCHAR(50) NOT NULL,
                CARGO VARCHAR(50) NOT NULL,
                SALARIO INT NOT NULL)
            )
        ''')
        messagebox.showinfo("CONEXION", "Base de datos creada exitosamente")