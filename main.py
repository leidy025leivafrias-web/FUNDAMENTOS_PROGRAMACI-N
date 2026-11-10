# main.py

import datos
from Buscar_Registro import buscar_registro
from ordenar_registros import ordenar_registros
from actualizar_calificaciones import actualizar_calificaciones
from listar_registros import listar_registros
from guardar_en_archivo import guardar_en_archivo

def main():
    # No se incluye la opción de registrar nuevos estudiantes.
    # Los registros deben cargarse desde un archivo o añadirse por otro medio.
    
    opcion = 0

    while opcion != 5:
        print("\n============================================================")
        print("          SISTEMA DE REGISTRO DE CALIFICACIONES")
        print("============================================================")
        print("1. Buscar registro por código o DNI")
        print("2. Ordenar registros por promedio final (mayor a menor)")
        print("3. Actualizar calificaciones de los bimestres")
        print("4. Listar todos los registros")
        print("5. Guardar y salir")

        try:
            opcion = int(input("\nSeleccione una opción (1-5): "))
        except ValueError:
            print("Opción no válida. Ingrese un número del 1 al 5.")
            continue

        if opcion == 1:
            buscar_registro()
        elif opcion == 2:
            ordenar_registros()
        elif opcion == 3:
            actualizar_calificaciones()
        elif opcion == 4:
            listar_registros()
        elif opcion == 5:
            guardar_en_archivo(datos.total_registros)
            print("Saliendo del sistema. ¡Hasta luego!")
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()