# Buscar_Registro.py

from datos import total_registros, codigos_exp, dnis
from mostrar_registro import mostrar_registro

def buscar_registro():
    if total_registros == 0:
        print("No hay registros en el sistema.")
        return

    busqueda = input(
        "Ingrese el código de expediente (EXP-1001) o el DNI: "
    ).strip().upper()

    encontrado = False

    for i in range(total_registros):
        if (
            codigos_exp[i].upper() == busqueda
            or dnis[i] == busqueda
        ):
            mostrar_registro(i)
            encontrado = True

    if not encontrado:
        print(f"No se encontró ningún registro con: {busqueda}")