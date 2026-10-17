def buscar_expedientes(codigos, apoPat, apoMat, apoNom, apoDni, apoTelf, estPat, estMat, estNom, niveles, estados, asuntos, totalExpedientes):
    if totalExpedientes > 0:
        print("\n --- Busqueda de Expedientes ---")
        codigoBuscar = input("Ingrese el Codigo del Expedientes (Ej. EXP-1001)").strip().upper()
        encontrar = False