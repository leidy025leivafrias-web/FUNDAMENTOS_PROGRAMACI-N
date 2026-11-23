def actualizar_estado_tramite(expedientes):
    print("\n--- ACTUALIZAR ESTADO DEL TRÁMITE ---")

    codigo_buscar = input("Ingrese el código del expediente: ").strip().upper()

    expediente_encontrado = None

    for expediente in expedientes:
        if expediente["codigo"].upper() == codigo_buscar:
            expediente_encontrado = expediente
            break

    if expediente_encontrado is None:
        print("Error: El código ingresado no existe.")
        return

    print("Estado actual:", expediente_encontrado["estado"])

    print("\n1. PENDIENTE")
    print("2. EN PROCESO")
    print("3. ATENDIDO")
    print("4. RECHAZADO")

    opcion = input("Seleccione el nuevo estado (1-4): ").strip()

    estados = {
        "1": "PENDIENTE",
        "2": "EN PROCESO",
        "3": "ATENDIDO",
        "4": "RECHAZADO"
    }

    if opcion not in estados:
        print("Opción no válida. No se realizaron cambios.")
        return

    nuevo_estado = estados[opcion]

    if expediente_encontrado["estado"].upper() == nuevo_estado:
        print("El expediente ya tiene ese estado.")
        return

    expediente_encontrado["estado"] = nuevo_estado

    print("Estado actualizado correctamente:", nuevo_estado)
