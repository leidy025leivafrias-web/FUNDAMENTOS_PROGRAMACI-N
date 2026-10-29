
from actualizar_tramite import actualizar_estado_tramite

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
    MAX = 100
    codigos = [""] * MAX
    estados = [""] * MAX
    totalExpedientes = 0

    while True:
        mostrar_menu()
        opcion = input(" >")
        
        if opcion == '1':
            print("\n--- Registrar Nuevo Expediente ---")
    
        elif opcion == '2':
            print("\n--- Listar Todos ---")
         
        elif opcion == '3':
            print("\n--- Buscar por Código ---")
        
        elif opcion == '4':
            print("\n--- Ordenar por Código ---")
        
        elif opcion == '5':
            #Actualizar Estado 
            if totalExpedientes > 0:
                actualizar_estado_tramite(codigos, estados, totalExpedientes)
            else:
                print("\n  No hay expedientes registrados en el sistema.")

        
        elif opcion == '6':
            print("\n--- Registrar Calificaciones ---")
        
        elif opcion == '7':
            print("\n--- Guardar en Archivo ---")
        
        elif opcion == '8':
            print("\nSaliendo del sistema...")
            break
        else:
            print("\nOpción inválida. Intente de nuevo.")
        

if __name__ == "__main__":
    main()