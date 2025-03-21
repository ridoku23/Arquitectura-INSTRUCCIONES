def menu_principal():
    print("Seleccione el tipo de instrucción:")
    print("1. Tipo R")
    print("2. Tipo I")
    print("3. Tipo J")
    print("4. Salir")
    opcion = input("Ingrese el número de su opción: ")
    return opcion

def menu_tipo_r():
    print("Seleccione la instrucción tipo R:")
    print("1. ADD")
    print("2. SUB")
    print("3. AND")
    print("4. OR")
    print("5. SLT")
    instruccion = input("Ingrese el número de su opción: ")
    return instruccion

def menu_tipo_i():
    print("Seleccione la instrucción tipo I:")
    print("1. LW")
    print("2. SW")
    print("3. BEQ")
    print("4. ADDI")
    instruccion = input("Ingrese el número de su opción: ")
    return instruccion

def menu_tipo_j():
    print("Seleccione la instrucción tipo J:")
    print("1. J")
    print("2. JAL")
    instruccion = input("Ingrese el número de su opción: ")
    return instruccion

def obtener_datos(tipo):
    if tipo == "R":
        rs = input("Ingrese el registro fuente 1 (rs): ")
        rt = input("Ingrese el registro fuente 2 (rt): ")
        rd = input("Ingrese el registro destino (rd): ")
        return rs, rt, rd
    elif tipo == "I":
        rs = input("Ingrese el registro fuente (rs): ")
        rt = input("Ingrese el registro destino (rt): ")
        inmediato = input("Ingrese el valor inmediato: ")
        return rs, rt, inmediato
    elif tipo == "J":
        direccion = input("Ingrese la dirección de salto: ")
        return direccion

def mostrar_codigo(tipo, instruccion, datos):
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
            "1": "100000",  # ADD
            "2": "100010",  # SUB
            "3": "100100",  # AND
            "4": "100101",  # OR
            "5": "101010"   # SLT
        }[instruccion]
        print(f"Instrucción ensamblador: {instruccion} {rd}, {rs}, {rt}")
        print(f"Código binario: 000000 {rs_bin} {rt_bin} {rd_bin} 00000 {funct_bin}")
    elif tipo == "I":
        rs, rt, inmediato = datos
        rs_bin = registro_a_binario(rs)
        rt_bin = registro_a_binario(rt)
        inmediato_bin = inmediato_a_binario(inmediato)
        opcode_bin = {
            "1": "100011",  # LW
            "2": "101011",  # SW
            "3": "000100",  # BEQ
            "4": "001000"   # ADDI
        }[instruccion]
        print(f"Instrucción ensamblador: {instruccion} {rt}, {rs}, {inmediato}")
        print(f"Código binario: {opcode_bin} {rs_bin} {rt_bin} {inmediato_bin}")
    elif tipo == "J":
        direccion = datos
        direccion_bin = direccion_a_binario(direccion)
        opcode_bin = {
            "1": "000010",  # J
            "2": "000011"   # JAL
        }[instruccion]
        print(f"Instrucción ensamblador: {instruccion} {direccion}")
        print(f"Código binario: {opcode_bin} {direccion_bin}")

def main():
    while True:
        tipo = menu_principal()
        if tipo == "1":
            instruccion = menu_tipo_r()
            datos = obtener_datos("R")
            mostrar_codigo("R", instruccion, datos)
        elif tipo == "2":
            instruccion = menu_tipo_i()
            datos = obtener_datos("I")
            mostrar_codigo("I", instruccion, datos)
        elif tipo == "3":
            instruccion = menu_tipo_j()
            datos = obtener_datos("J")
            mostrar_codigo("J", instruccion, datos)
        elif tipo == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()


