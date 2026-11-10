def modificar_expediente(expedientes):
    if len(expedientes) > 0:
        print("\n--- Modificar datos del expedientes ---")
        codigoBuscar= input("Ingresar el codigo de expedientes a modificar (EXP-1001)")
        encontrado= False

        for exp in expedientes:
            if exp['codigo']. upper() == codigoBuscar:
                encontrado = True
                print(f"Expediente {exp['codigo']} encontrado. Ingrese los nuevos datos")


                print("\n¿Que quieres modificar?")
                print("1. Datos del Apoderado")
                print("2. Datos del estudiante")
                opcion = input("Elige: ")

                if opcion =="1":
                    print("1. DNI")
                    print("2. Nombre")
                    print("3. Apellido Paterno")
                    print("4. Apellido Materno")
                    print("5 Telefono")
                    print("6. Correo")

                    alt=input("Marca una opcion:")

                    if alt=="1":
                        exp["dni_apoderado"] = validar_entero("Nuevo DNI del apoderado ",8)
                    elif alt=="2":
                        exp["nombre_apoderado"] = validar_Letra("Nuevo nombre del apoderado")
                    elif alt=="3":
                        exp["paterno_apoderado"] = validar_Letra("Nuevo Apellido Paterno del apoderado")
                    elif alt=="4":
                        exp["materno_apoderado"] = validar_Letra("Nuevo Apellido Matterno del apoderado")
                    elif alt=="5":
                        exp["telefono_apoderado"] = validar_entero("Nuevo telefono del apoderado",9)
                    elif alt=="6":
                        exp["correo_apoderado"] = validar_correo("Nuevo correo electronico del apoderado")
                    else:
                        print("Alternativa invalida")

                    print(" \n Dato del apoderado modificado")
                    
                elif opcion =="2":
                    print("1. DNI")
                    print("2. Nombre")
                    print("3. Apellido Paterno")
                    print("4. Apellido Materno")
                    print("5. Nivel Educativo")
                    print("6. Estado Actual")
                    
                    alt=input("Marca una opcion:")
                    if alt=="1":
                        exp["dni_estudiante"] = validar_entero("Nuevo DNI del estudiane ",8)
                    elif alt=="2":
                        exp["nombre_estudiante"] = validar_Letra("Nuevo nombre del estudiante")
                    elif alt=="3":
                        exp["paterno_estudiante"] = validar_Letra("Nuevo Apellido Paterno del estudiante")
                    elif alt=="4":
                        exp["materno_estudiante"] = validar_Letra("Nuevo Apellido Matterno del estudiante")
                    elif alt=="5":
                        exp["nivel_educativo"] = validar_Letra("Nuevo Nivel Educativo del estudiante")
                    elif alt=="6":
                        exp["estado_actual"] = validar_Letra("Nuevo Estado Actual")
                    else:
                        print("Alternativa invalida")
                        
                    print(" \n Dato del estudiante modificado")
                    print("\n¡Datos del expediente actualizado con exito!")
                    break
            
        if not encontrado:
            print(f"No encontro ningun expediente con el codigo{codigoBuscar}")
    else:
        print("No hay expedientes registrados")

def validar_Letra(dato):
    while True:
        Nuevo_dato=input(dato).strip()
        if Nuevo_dato.replace(" ","").isalpha() and len(Nuevo_dato)>0:
            return Nuevo_dato
        print("Solo se acepta letras.")

def validar_entero(dato,maximo):
    while True:
        Nuevo_dato = input(dato).strip()
        if not Nuevo_dato.isdigit():
            print("Solo se permite numeros")
        elif len(Nuevo_dato)!=maximo:

            print(f"Debe tener {maximo} digitos")
        else:
            return Nuevo_dato

def validar_correo(dato):
    while True:
        Nuevo_dato=input(dato).strip()
        if "@" in Nuevo_dato and "." in Nuevo_dato and " " not in Nuevo_dato:
            return Nuevo_dato
        print("Error, ingreso un correo valido ej: juan@dominio.com")





