from Validar_dni import validar_dni_apoderado, validar_dni_estudiante
from Validar_nombres_del_apoderado import Validar__nombres_del_apoderado
from Validar_nombre_estudiante import validar_nombres_estudiante
from Validar_numero import validar_numero
from Validar_Nivel_Educativo_del_estudiante import Validar_Nivel_Educativo_del_estudiante
from Validar_correo import validar_correo
from Codigo_expediente import Codigo_expediente
from listado_expedientes import listado_expedientes
from buscar_expedientes import buscar_expedientes
from OrdenarExpedientes import ordenar_expedientes_por_codigo
from actualizar_tramite import actualizar_estado_tramite
from Expedientes import Expedientes
from guardado import guardar_expedientes
from Cargar_expedientes import cargar_expedientes
from eliminar_expedientes import eliminar_expedientes
from modificar_expedientes import modificar_expedientes


def mostrar_menu():
    print("\n===============================================")
    print("  MESA DE PARTES DIGITAL - FE Y ALEGRÍA Nº 37")
    print("===============================================")
    print("1. Registrar Nuevo Expediente")
    print("2. Listar Expedientes")
    print("3. Buscar por Código")
    print("4. Ordenar por Código")
    print("5. Actualizar Estado")
    print("6. Registrar Calificaciones")
    print("7. Guardar en Archivo")
    print("8. Eliminar Expediente")
    print("9. Modificar Expediente")
    print("10. Salir")
    print("===============================================")


def main():
    expedientes = cargar_expedientes()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            print("\n<<<<< REGISTRAR NUEVO EXPEDIENTE >>>>>")

            dni_apoderado = validar_dni_apoderado()
            nombre, paterno, materno = Validar__nombres_del_apoderado()
            telefono_apoderado = validar_numero()
            correo_apoderado = validar_correo()
            dni_estudiante = validar_dni_estudiante()
            nombre_estudiante, paterno_estudiante, materno_estudiante = validar_nombres_estudiante()
            nivel = Validar_Nivel_Educativo_del_estudiante()

            codigo = Codigo_expediente(expedientes)

            expediente = {
                "codigo": codigo,
                "dni_apoderado": dni_apoderado,
                "nombre_apoderado": nombre,
                "paterno_apoderado": paterno,
                "materno_apoderado": materno,
                "telefono_apoderado": telefono_apoderado,
                "correo_apoderado": correo_apoderado,
                "dni_estudiante": dni_estudiante,
                "nombre_estudiante": nombre_estudiante,
                "paterno_estudiante": paterno_estudiante,
                "materno_estudiante": materno_estudiante,
                "nivel": nivel,
                "estado": "Pendiente"
            }

            expedientes.append(expediente)

            print("\nExpediente registrado correctamente.")
            print("Código asignado:", codigo)

            guardar_expedientes(expedientes)

        elif opcion == '2':
            print("\n<<<<< LISTADO GENERAL DE EXPEDIENTES >>>>>")
            listado_expedientes(expedientes)

        elif opcion == '3':
            print("\n<<<<< BÚSQUEDA POR CÓDIGO >>>>>")
            buscar_expedientes(expedientes)

        elif opcion == '4':
            print("\n<<<<< ORDENAR POR CÓDIGO >>>>>")
            ordenar_expedientes_por_codigo(expedientes)

        elif opcion == '5':
            print("\n<<<<< ACTUALIZAR ESTADO >>>>>")
            if expedientes:
                actualizar_estado_tramite(expedientes)
                guardar_expedientes(expedientes)
            else:
                print("\nNo hay expedientes registrados.")

        elif opcion == '6':
            print("\n<<<<< REGISTRAR CALIFICACIONES >>>>>")
            if expedientes:
                Expedientes(expedientes)
                guardar_expedientes(expedientes)
            else:
                print("\nNo hay expedientes registrados.")

        elif opcion == '7':
            print("\n<<<<< GUARDAR EXPEDIENTES >>>>>")
            guardar_expedientes(expedientes)

        elif opcion == '8':
            print("\n<<<<< ELIMINAR EXPEDIENTE >>>>>")

            cantidad_anterior = len(expedientes)
            eliminar_expedientes(expedientes)

            if len(expedientes) < cantidad_anterior:
                guardar_expedientes(expedientes)

        elif opcion == '9':
            print("\n<<<<< MODIFICAR EXPEDIENTE >>>>>")

            if expedientes:
                modificar_expedientes(expedientes)
                guardar_expedientes(expedientes)
            else:
                print("\nNo hay expedientes registrados.")

        elif opcion == '10':
            guardar_expedientes(expedientes)
            print("\nSaliendo del sistema...")
            break

        else:
            print("\nOpción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
