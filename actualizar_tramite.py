#Función 4: Actualizar estado del trámite

def actualizar_estado_tramite(expedientes):
    print("\n--- ACTUALIZAR ESTADO DEL TRÁMITE ---")
    codigo_buscar = input("Ingrese el código del expediente:").strip().upper()

    posicion = -1
    for i in range(len(expedientes)):
        if expedientes[i]["codigo"] == codigo_buscar:
            posicion = i
            break

    if posicion != -1:
        print(f"Expediente encontrado. Estado actual: {expedientes[posicion]["estado"].upper()}")
        estado_original = expedientes[posicion]["estado"]

        print("1. PENDIENTE")
        print("2. EN PROCESO")
        print("3. ATENDIDO")
        print("4. RECHAZADO")

        opcion = input("Seleccione el nuevo estado (1-4): ").strip()
        nuevo_estado = ""

        if opcion == "1":
            nuevo_estado = "PENDIENTE"
        elif opcion == "2":
            nuevo_estado = "EN PROCESO"
        elif opcion == "3":
            nuevo_estado = "ATENDIDO"
        elif opcion == "4":
            nuevo_estado = "RECHAZADO"
        else:
            print("Opción no válida. No se realizaron cambios.")
            return

        if nuevo_estado == estado_original.upper():
            print(f"[!] Alerta: El expediente ya se encuentra en estado {estado_original}.")
        else:
            expedientes[posicion]["estado"] = nuevo_estado
            print(f"¡Éxito! El estado se actualizó a: {expedientes[posicion]["estado"]}")
    else:
        print("Error: El código ingresado no existe.")

        