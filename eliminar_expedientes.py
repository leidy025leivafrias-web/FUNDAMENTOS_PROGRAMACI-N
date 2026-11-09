def eliminar_expedientes(expedientes):
    if len(expedientes) > 0:
        print("\n--- Eliminar Expediente ---")
        codigoBuscar = input("Ingresar el codigo del Expediente a elimiar (Ej  EXP-1001): ").strip().upper()
        encontrado = False

        for i in range(len(expedientes)):
            if expedientes[i]["codigo"].upper() == codigoBuscar:
                encontrado = True
                expedientes.pop(i)
                print(f"\n ¡Expediente {codigoBuscar} eliminado con exito!")
                break

        if not encontrado:
            print(f"No se encontro ningun expediente con el codigo: {codigoBuscar}")
    else:
        print("No hay expedientes registrados en el sistema.")
