
import csv

def cargar_expedientes():
    expedientes = []

    try:
        with open("expedientes.csv", "r", encoding="utf-8-sig", newline="") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                expediente = {
                    "codigo": fila["Codigo"],
                    "dni_apoderado": fila["DNI Apoderado"],
                    "nombre_apoderado": fila["Nombre Apoderado"],
                    "paterno_apoderado": fila["Apellido Paterno Apoderado"],
                    "materno_apoderado": fila["Apellido Materno Apoderado"],
                    "telefono_apoderado": fila["Telefono Apoderado"],
                    "correo_apoderado": fila["Correo Apoderado"],
                    "dni_estudiante": fila["DNI Estudiante"],
                    "nombre_estudiante": fila["Nombre Estudiante"],
                    "paterno_estudiante": fila["Apellido Paterno Estudiante"],
                    "materno_estudiante": fila["Apellido Materno Estudiante"],
                    "nivel": fila["Nivel Educativo"],
                    "estado": fila["Estado Tramite"]
                }

                if all([
                    fila["I Bimestre"],
                    fila["II Bimestre"],
                    fila["III Bimestre"],
                    fila["Promedio Final"]
                ]):
                    expediente["calificaciones"] = {
                        "bimestre1": float(fila["I Bimestre"]),
                        "bimestre2": float(fila["II Bimestre"]),
                        "bimestre3": float(fila["III Bimestre"]),
                        "promedio": float(fila["Promedio Final"]),
                        "estado_academico": fila["Estado Academico"]
                    }

                expedientes.append(expediente)

        print(f"Se cargaron {len(expedientes)} expedientes correctamente.")

    except FileNotFoundError:
        print("No existe un archivo de expedientes anterior.")

    except (OSError, KeyError, ValueError, csv.Error) as error:
        print("Error al cargar expedientes:", error)
        raise

    return expedientes
