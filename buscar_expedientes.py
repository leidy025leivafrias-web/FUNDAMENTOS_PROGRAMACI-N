def buscar_expedientes(codigos, apoPat, apoMat, apoNom, apoDni, apoTelf, estPat, estMat, estNom, niveles, estados, asuntos, totalExpedientes):
    if totalExpedientes > 0:
        print("\n --- Busqueda de Expedientes ---")
        codigoBuscar = input("Ingrese el Codigo del Expedientes (Ej. EXP-1001)").strip().upper()
        encontrado = False

        for i in range(totalExpedientes):
            if codigos[i] == codigoBuscar:
                print("Expediente Encontrado:")
                print(f"Codigo: {codigos[i]}")
                print(f"Apoderado: {apoPat[i]}, {apoMat[i]}, {apoNom[i]}")
                print(f"DNI: {apoDni[i]} | Telefono: {apoTelf[i]}")
                print(f"Estudiante: {estPat[i]}, {estMat[i]}, {estNom[i]}")
                print(f"Nivel Educativo: {niveles[i]}")
                print(f"Asunto: {asuntos[i]}")
                print(f"Estado Actual: {estados[i]}")
                encontrado = True
                break
        if not encontrado:
            print(f"No se encuentro ningun expediente con el codigo: {codigoBuscar}")
        else:
            print("No hay expedientes registrados en el sistema")    



