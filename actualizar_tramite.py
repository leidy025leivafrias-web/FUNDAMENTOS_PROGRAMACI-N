#Función 4: Actualizar estado del trámite
def actualizar_estado_tramite(codigos, estados, total):
    print("\n--- ACTUALIZAR ESTADO DEL TRÁMITE ---")
    codigo_buscar = input("Ingrese el código del expediente:").strip().upper()

    posicion = -1
    for i in range(total):
        if codigos[i] == codigo_buscar:
            posicion = i
            break

    if posicion != -1:
        print(f"Expediente encontrado. Estado actual: {estados[posicion]}")
    else:
        print("Error: El código ingresado no existe.")