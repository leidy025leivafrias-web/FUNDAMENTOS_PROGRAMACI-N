# calcular_promedio.py

from datos import bimestre1, bimestre2, bimestre3, promedios_finales, estados

def calcular_promedio(indice):
    promedios_finales[indice] = round(
        (
            bimestre1[indice]
            + bimestre2[indice]
            + bimestre3[indice]
        ) / 3.0,
        2,
    )
    estados[indice] = (
        "APROBADO"
        if promedios_finales[indice] >= 11.0
        else "DESAPROBADO"
    )
