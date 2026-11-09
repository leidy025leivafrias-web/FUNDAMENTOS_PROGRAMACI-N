def Validar_Nivel_Educativo_del_estudiante():
# PASO 4: NIVEL EDUCATIVO Y TRÁMITE
    while True:
        print("\n PASO 10: NIVEL EDUCATIVO Y TRÁMITE")
        print("Seleccione el Nivel Educativo:")
        print("1. Inicial")
        print("2. Primaria")
        print("3. Secundaria")
        print("4. EBE (Educación Básica Especial)")

        opcion = input("Ingrese la opción (1-4): ")

        # Validar que no esté en blanco
        if not opcion.strip():
            print("ERROR: No puede dejar la opción en blanco.\n")

        elif opcion.strip() == "1":
            nivel = "Inicial"
            break
        elif opcion.strip() == "2":
            nivel = "Primaria"
            break
        elif opcion.strip() == "3":
            nivel = "Secundaria"
            break
        elif opcion.strip() == "4":
            nivel = "EBE (Educación Básica Especial)"
            break
        else:
            print("ERROR: Opción no válida. Ingrese un número entre 1 y 4.\n")

    print(f"\nNivel educativo seleccionado: {nivel}")

    return nivel

if __name__ == "__main__":
    Validar_Nivel_Educativo_del_estudiante()