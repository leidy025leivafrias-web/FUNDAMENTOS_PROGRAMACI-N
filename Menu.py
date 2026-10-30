from Validar_dni import validar_dni_apoderado, validar_dni_estudiante
from Validar_nombres_del_apoderado import Validar__nombres_del_apoderado
from Validar_nombre_estudiante import validar_nombres_estudiante
from Validar_numero import validar_numero
from Validar_Nivel_Educativo_del_estudiante import Validar_Nivel_Educativo_del_estudiante
from Validar_correo import validar_correo

from listado_expedientes import listado_expedientes
def mostrar_menu():
    print("*** Ejecución Iniciada. ***")
    print("===============================================")
    print("  MESA DE PARTES DIGITAL - FE Y ALEGRÍA Nº 37")
    print("===============================================")
    print("1. Registrar Nuevo Expediente")
    print("2. Listar Todos")
    print("3. Buscar por Código")
    print("4. Ordenar por Código")
    print("5. Actualizar Estado")
    print("6. Registrar Calificaciones")
    print("7. Guardar en Archivo")
    print("8. Salir")
    print("Seleccione una opción:")

def main():
    expedientes = []
    while True:
        mostrar_menu()
        opcion = input("> ")
        
        if opcion == '1':
            print("\n <<<<<REGISTRAR NUEVO EXPEDIENTE>>>>> ")
            dni_apoderado = validar_dni_apoderado()
            nombre, paterno, materno = Validar__nombres_del_apoderado()
            telefono_apoderado = validar_numero()
            correo_apoderado = validar_correo()
            dni_estudiante = validar_dni_estudiante()
            nombre_estudiante, paterno_estudiante, materno_estudiante = validar_nombres_estudiante()
            nivel = Validar_Nivel_Educativo_del_estudiante()
        elif opcion == '2':
            print("\n--- Listar Todos ---")
            
        elif opcion == '3':
            print("\n--- Buscar por Código ---")
            
        elif opcion == '4':
            print("\n--- Ordenar por Código ---")
            
        elif opcion == '5':
            print("\n--- Actualizar Estado ---")
            # Agrega aquí tu lógica
        elif opcion == '6':
            print("\n--- Registrar Calificaciones ---")
            # Agrega aquí tu lógica
        elif opcion == '7':
            print("\n--- Guardar en Archivo ---")
            # Agrega aquí tu lógica
        elif opcion == '8':
            print("\nSaliendo del sistema...")
            break
        else:
            print("\nOpción inválida. Intente de nuevo.")
        

if __name__ == "__main__":
    main()