def buscar_expedientes(codigos, apoPat, apoMat, apoNom, apoDni, apoTelf, estPat, estMat, estNom, niveles, estados, asuntos,nota1, nota2, nota3, nota4, promedios, totalExpedientes):
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
                print("--- Registro Academico (4 Bimestres)---")
                print(f"Notas: [Bim 1:{nota1[i]} | Bin 2:{nota2[i]} | Bin 3:{nota3[i]} | Bin 4:{nota4[i]}")
                print(f"Promedio Final: {promedios[i]}")
                if promedios[i]>= 11:
                    print(f"Condicon Academica: Aprobado")
                else:
                    print("Condicion Academica: Desaprobado")
                encontrado = True
                break
        if not encontrado:
            print(f"No se encuentro ningun expediente con el codigo: {codigoBuscar}")
        else:
            print("No hay expedientes registrados en el sistema")    

       