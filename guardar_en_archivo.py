import csv
from datos import ARCHIVO_CSV, codigos_exp, dnis, apellidos, nombres, bimestre1, bimestre2, bimestre3, promedios_finales, estados

def guardar_en_archivo(total):
    
    """Guarda los registros actuales en un archivo CSV."""
    encabezados = [
        "CodigoExpediente",
        "DNI",
        "Apellidos",
        "Nombres",
        "I_Bimestre",
        "II_Bimestre",
        "III_Bimestre",
        "PromedioFinal",
        "Estado",
    ]

    try:
        with open(
            ARCHIVO_CSV, "w", newline="", encoding="utf-8"
        ) as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(encabezados)

            for i in range(total):
                escritor.writerow([
                    codigos_exp[i],
                    dnis[i],
                    apellidos[i],
                    nombres[i],
                    bimestre1[i],
                    bimestre2[i],
                    bimestre3[i],
                    promedios_finales[i],
                    estados[i],
                ])

        print(f"\n[Éxito] Registros guardados en '{ARCHIVO_CSV}'.")
    except OSError as error:
        print(f"Error al guardar el archivo: {error}")
