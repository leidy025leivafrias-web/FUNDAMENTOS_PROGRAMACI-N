def buscar_expedientes(expedientes):
    if len(expedientes) > 0:
        print("\n --- BUSQUEDA DE EXPEDIENTES ---")
        codigoBuscar = input("Ingrese el Codigo del Expedientes (Ej. EXP001): ").strip().upper()
        encontrado = False
        
        for expediente in expedientes:
            if expediente["codigo"].upper() == codigoBuscar:
                print("\nEXPEDIENTE ENCONTRADO:")
                print(f"CÓDIGO: ", expediente["codigo"])
                print(f"\nAPODERADO: ", expediente ["nombre_apoderado"], expediente["paterno_apoderado"], expediente["materno_apoderado"])
                print(f"DNI: ",expediente["dni_apoderado"])
                print(f"TELÉFONO: ",expediente["telefono_apoderado"])
                print(f"CORREO: ",expediente["correo_apoderado"])
                print(f"\nESTUDIANTE: ", expediente["nombre_estudiante"], expediente ["paterno_estudiante"],expediente ["materno_estudiante"])
                print(f"DNI: ", expediente["dni_estudiante"])
                print(f"NIVEL EDUCATIVO: ",expediente ["nivel"])
                print(f"\nESTADO ACTUAL: ",expediente ["estado"])
                
                if "calificaciones" in expediente:
                     notas = expediente["calificaciones"]
                     print("\n--- REGISTRO ACADÉMICO (4 Bimestres)---")
                     print("I Bimestre: ", notas ["bimestre1"])
                     print("II Bimestre: ",notas ["bimestre2"])
                     print("III Bimestre: ",notas ["bimestre3"])
                     print("Promedio final: ",notas ["promedio"])
                     print("Condición académica: ",notas ["estado_académico"])
                else:
                   print("\nEl estudiante todavía no tiene calificaciones registradas.")
                   encontrado = True
                   break
        if not encontrado:
            print(f"No se encuentro ningun expediente con el codigo: {codigoBuscar}")
    else:
            print("No hay expedientes registrados en el sistema")    

       