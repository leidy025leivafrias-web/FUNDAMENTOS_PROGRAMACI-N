def eliminar_expedientes(expedientes):
    if not expedientes:
        print("\nNo hay expedientes registrados en el sistema.")
        return

    print("\n--- ELIMINAR EXPEDIENTE ---")

    while True:
        codigo_buscar = input(
            "Ingrese el código del expediente (Ej. EXP-1001): "
        ).strip().upper()

        if codigo_buscar:
            break

        print("ERROR: El código no puede estar vacío. Intente nuevamente.")

    for i, expediente in enumerate(expedientes):
        codigo = str(expediente.get("codigo", "")).strip().upper()

        if codigo == codigo_buscar:
            confirmacion = input(
                f"¿Está seguro de eliminar el expediente {codigo_buscar}? (S/N): "
            ).strip().upper()

            if confirmacion == "S":
                expedientes.pop(i)
                print(f"\n¡Expediente {codigo_buscar} eliminado con éxito!")
            elif confirmacion == "N":
                print("\nEliminación cancelada.")
            else:
                print("\nOpción no válida. No se eliminó el expediente.")

            return

    print(f"\nNo se encontró ningún expediente con el código: {codigo_buscar}")
