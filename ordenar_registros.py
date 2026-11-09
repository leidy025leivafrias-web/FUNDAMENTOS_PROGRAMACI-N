# ordenar_registros.py

from datos import (
    total_registros,
    codigos_exp,
    dnis,
    apellidos,
    nombres,
    bimestre1,
    bimestre2,
    bimestre3,
    promedios_finales,
    estados
)

def ordenar_registros():
    if total_registros < 2:
        print("Se requieren al menos 2 registros para ordenar.")
        return

    # Método burbuja: se mueven juntos todos los datos de cada estudiante.
    listas = [
        codigos_exp,
        dnis,
        apellidos,
        nombres,
        bimestre1,
        bimestre2,
        bimestre3,
        promedios_finales,
        estados,
    ]

    for i in range(total_registros - 1):
        for j in range(total_registros - 1 - i):
            if promedios_finales[j] < promedios_finales[j + 1]:
                for lista in listas:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

    print("Registros ordenados por promedio, de mayor a menor.")