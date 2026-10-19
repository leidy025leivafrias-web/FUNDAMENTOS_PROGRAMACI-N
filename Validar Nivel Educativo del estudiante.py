# PASO 4: NIVEL EDUCATIVO Y TRÁMITE
while True:
    print("PASO 4: NIVEL EDUCATIVO Y TRÁMITE")
    print("Seleccione el Nivel Educativo:")
    print("1. Inicial")
    print("2. Primaria")
    print("3. Secundaria")
    print("4. EBE (Educación Básica Especial)")
    
    opcion = input("Ingrese la opción (1-4): ")

    if opcion == "1":
        nivel = "Inicial"
        break
    elif opcion == "2":
        nivel = "Primaria"
        break
    elif opcion == "3":
        nivel = "Secundaria"
        break
    elif opcion == "4":
        nivel = "EBE (Educación Básica Especial)"
        break
    else:
        print("ERROR: Opción no válida. Ingrese un número entre 1 y 4.\n")

print(f"\nNivel educativo seleccionado: {nivel}")