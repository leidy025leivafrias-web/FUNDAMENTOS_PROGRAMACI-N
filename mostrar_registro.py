# mostrar_registro.py

from datos import (
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
def mostrar_registro(indice):
    print("\n----------------------------------------")
    print("REGISTRO ENCONTRADO")
    print(f"Código de expediente: {codigos_exp[indice]}")
    print(f"DNI: {dnis[indice]}")
    print(f"Apellidos y nombres: {apellidos[indice]}, {nombres[indice]}")
    print(f"I Bimestre: {bimestre1[indice]:.2f}")
    print(f"II Bimestre: {bimestre2[indice]:.2f}")
    print(f"III Bimestre: {bimestre3[indice]:.2f}")
    print(f"Promedio final: {promedios_finales[indice]:.2f}")
    print(f"Estado académico: {estados[indice]}")
    print("----------------------------------------")
