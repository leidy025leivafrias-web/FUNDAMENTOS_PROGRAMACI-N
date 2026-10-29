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
    while True:
        mostrar_menu()
        opcion = input("> ")
        
        if opcion == '1':
            print("\n--- Registrar Nuevo Expediente ---")
            # Agrega aquí tu lógica
        elif opcion == '2':
            print("\n--- Listar Todos ---")
            # Agrega aquí tu lógica
        elif opcion == '3':
            print("\n--- Buscar por Código ---")
            # Agrega aquí tu lógica
        elif opcion == '4':
            print("\n--- Ordenar por Código ---")
            # Agrega aquí tu lógica
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
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()