import csv

def guardar_expedientes(expedientes):

    if len(expedientes) == 0:
        print("No hay expedientes registrados para guardar.")
        return

    with open("expedientes.csv", "w", newline="", encoding="utf-8-sig") as archivo:

        escritor = csv.writer(archivo)

        escritor.writerow([
            "Codigo",
            "DNI Apoderado",
            "Nombre Apoderado",
            "Apellido Paterno Apoderado",
            "Apellido Materno Apoderado",
            "Telefono Apoderado",
            "Correo Apoderado",
            "DNI Estudiante",
            "Nombre Estudiante",
            "Apellido Paterno Estudiante",
            "Apellido Materno Estudiante",
            "Nivel Educativo",
            "Estado Tramite",
            "I Bimestre",
            "II Bimestre",
            "III Bimestre",
            "Promedio Final",
            "Estado Academico"
        ])

        for expediente in expedientes:

            notas = expediente.get("calificaciones", {})

            escritor.writerow([
                expediente.get("codigo", ""),
                expediente.get("dni_apoderado", ""),
                expediente.get("nombre_apoderado", ""),
                expediente.get("paterno_apoderado", ""),
                expediente.get("materno_apoderado", ""),
                expediente.get("telefono_apoderado", ""),
                expediente.get("correo_apoderado", ""),
                expediente.get("dni_estudiante", ""),
                expediente.get("nombre_estudiante", ""),
                expediente.get("paterno_estudiante", ""),
                expediente.get("materno_estudiante", ""),
                expediente.get("nivel", ""),
                expediente.get("estado", ""),
                notas.get("bimestre1", ""),
                notas.get("bimestre2", ""),
                notas.get("bimestre3", ""),
                notas.get("promedio", ""),
                notas.get("estado_academico", "")
            ])

    print("\n¡Expedientes guardados correctamente!")
    print("Archivo generado: expedientes.csv")