import tkinter as tk
from tkinter import ttk

def mostrar_codigo(tipo, instruccion, datos):
    """
    Muestra el código ensamblador y binario de la instrucción seleccionada.

    Args:
        tipo (str): Tipo de instrucción (R, I, J).
        instruccion (str): Instrucción seleccionada.
        datos (tuple): Datos necesarios para la instrucción.
    """
    def registro_a_binario(registro):
        return format(int(registro), '05b')

    def inmediato_a_binario(inmediato):
        return format(int(inmediato), '016b')

    def direccion_a_binario(direccion):
        return format(int(direccion), '026b')

    if tipo == "R":
        rs, rt, rd = datos
        rs_bin = registro_a_binario(rs)
        rt_bin = registro_a_binario(rt)
        rd_bin = registro_a_binario(rd)
        funct_bin = {
            "ADD": "100000",
            "SUB": "100010",
            "AND": "100100",
            "OR": "100101",
            "SLT": "101010"
        }[instruccion]
        resultado.set(f"Instrucción ensamblador: {instruccion} {rd}, {rs}, {rt}\nCódigo binario: 000000 {rs_bin} {rt_bin} {rd_bin} 00000 {funct_bin}")
    elif tipo == "I":
        rs, rt, inmediato = datos
        rs_bin = registro_a_binario(rs)
        rt_bin = registro_a_binario(rt)
        inmediato_bin = inmediato_a_binario(inmediato)
        opcode_bin = {
            "LW": "100011",
            "SW": "101011",
            "BEQ": "000100",
            "ADDI": "001000"
        }[instruccion]
        resultado.set(f"Instrucción ensamblador: {instruccion} {rt}, {rs}, {inmediato}\nCódigo binario: {opcode_bin} {rs_bin} {rt_bin} {inmediato_bin}")
    elif tipo == "J":
        direccion = datos
        direccion_bin = direccion_a_binario(direccion)
        opcode_bin = {
            "J": "000010",
            "JAL": "000011"
        }[instruccion]
        resultado.set(f"Instrucción ensamblador: {instruccion} {direccion}\nCódigo binario: {opcode_bin} {direccion_bin}")

def seleccionar_instruccion():
    """
    Selecciona la instrucción y obtiene los datos necesarios para mostrar el código.
    """
    tipo = tipo_instruccion.get()
    instruccion = instruccion_seleccionada.get()
    if tipo == "R":
        rs = entrada_rs.get()
        rt = entrada_rt.get()
        rd = entrada_rd.get()
        datos = (rs, rt, rd)
    elif tipo == "I":
        rs = entrada_rs.get()
        rt = entrada_rt.get()
        inmediato = entrada_inmediato.get()
        datos = (rs, rt, inmediato)
    elif tipo == "J":
        direccion = entrada_direccion.get()
        datos = direccion
    mostrar_codigo(tipo, instruccion, datos)

def actualizar_menu(*args):
    """
    Actualiza el menú de instrucciones según el tipo de instrucción seleccionado.
    """
    tipo = tipo_instruccion.get()
    if tipo == "R":
        opciones = ["ADD", "SUB", "AND", "OR", "SLT"]
        entrada_rs.grid(row=3, column=1)
        entrada_rt.grid(row=4, column=1)
        entrada_rd.grid(row=5, column=1)
        entrada_inmediato.grid_remove()
        entrada_direccion.grid_remove()
        etiqueta_rs.grid(row=3, column=0)
        etiqueta_rt.grid(row=4, column=0)
        etiqueta_rd.grid(row=5, column=0)
        etiqueta_inmediato.grid_remove()
        etiqueta_direccion.grid_remove()
    elif tipo == "I":
        opciones = ["LW", "SW", "BEQ", "ADDI"]
        entrada_rs.grid(row=3, column=1)
        entrada_rt.grid(row=4, column=1)
        entrada_inmediato.grid(row=5, column=1)
        entrada_rd.grid_remove()
        entrada_direccion.grid_remove()
        etiqueta_rs.grid(row=3, column=0)
        etiqueta_rt.grid(row=4, column=0)
        etiqueta_inmediato.grid(row=5, column=0)
        etiqueta_rd.grid_remove()
        etiqueta_direccion.grid_remove()
    elif tipo == "J":
        opciones = ["J", "JAL"]
        entrada_direccion.grid(row=3, column=1)
        entrada_rs.grid_remove()
        entrada_rt.grid_remove()
        entrada_rd.grid_remove()
        entrada_inmediato.grid_remove()
        etiqueta_direccion.grid(row=3, column=0)
        etiqueta_rs.grid_remove()
        etiqueta_rt.grid_remove()
        etiqueta_rd.grid_remove()
        etiqueta_inmediato.grid_remove()
    instruccion_seleccionada.set(opciones[0])
    menu_instrucciones['menu'].delete(0, 'end')
    for opcion in opciones:
        menu_instrucciones['menu'].add_command(label=opcion, command=tk._setit(instruccion_seleccionada, opcion))

# Configuración de la ventana principal
root = tk.Tk()
root.title("Simulador de Instrucciones MIPS")
root.geometry("600x400")  # Aumentar el tamaño de la ventana
root.resizable(False, False)

# Variables
tipo_instruccion = tk.StringVar()
tipo_instruccion.set("R")
tipo_instruccion.trace('w', actualizar_menu)

instruccion_seleccionada = tk.StringVar()

resultado = tk.StringVar()

# Widgets
tk.Label(root, text="Seleccione el tipo de instrucción:", font=("Arial", 12)).grid(row=0, column=0, pady=10)
menu_tipo = ttk.Combobox(root, textvariable=tipo_instruccion, values=["R", "I", "J"])
menu_tipo.grid(row=0, column=1, pady=10)

tk.Label(root, text="Seleccione la instrucción:", font=("Arial", 12)).grid(row=1, column=0, pady=10)
menu_instrucciones = ttk.OptionMenu(root, instruccion_seleccionada, "")
menu_instrucciones.grid(row=1, column=1, pady=10)

etiqueta_rs = tk.Label(root, text="Registro fuente 1 (rs):", font=("Arial", 12))
entrada_rs = tk.Entry(root)

etiqueta_rt = tk.Label(root, text="Registro fuente 2 (rt):", font=("Arial", 12))
entrada_rt = tk.Entry(root)

etiqueta_rd = tk.Label(root, text="Registro destino (rd):", font=("Arial", 12))
entrada_rd = tk.Entry(root)

etiqueta_inmediato = tk.Label(root, text="Valor inmediato:", font=("Arial", 12))
entrada_inmediato = tk.Entry(root)

etiqueta_direccion = tk.Label(root, text="Dirección de salto:", font=("Arial", 12))
entrada_direccion = tk.Entry(root)

tk.Button(root, text="Mostrar Código", command=seleccionar_instruccion, font=("Arial", 12)).grid(row=6, column=0, columnspan=2, pady=10)

tk.Label(root, textvariable=resultado, font=("Arial", 12), wraplength=550).grid(row=7, column=0, columnspan=2, pady=10)

# Inicializar menú
actualizar_menu()

# Iniciar la aplicación
root.mainloop()