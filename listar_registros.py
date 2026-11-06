# listar_registros.py

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

def listar_registros():
    if total_registros == 0:
        print("No hay registros para mostrar.")
        return

    print("\n================ LISTADO GENERAL DE CALIFICACIONES ================")

    for i in range(total_registros):
        print(
            f"{i + 1}. [{codigos_exp[i]}] DNI: {dnis[i]} | "
            f"{apellidos[i]}, {nombres[i]} | "
            f"Notas [I: {bimestre1[i]:.2f}, "
            f"II: {bimestre2[i]:.2f}, "
            f"III: {bimestre3[i]:.2f}] | "
            f"Promedio: {promedios_finales[i]:.2f} | "
            f"Estado: {estados[i]}"
        )

    print("==================================================================")