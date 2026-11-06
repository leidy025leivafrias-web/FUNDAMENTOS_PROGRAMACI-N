def modificar_expediente(expedientes):
    if len(expedientes) > 0:
        print("\n--- Modificar datos del expedientes ---")
        codigoBuscar= input("Ingresar el codigo de expedientes a modificar (EXP-1001)")
        encontrado= False

        for exp in expedientes:
            if exp["codigo"]. upper() == codigoBuscar:
                encontrado = True
                print(f"Expediente {exp["codigo"]} encontrado. Ingrese los nuevos datos")

                exp["dni_apoderado"] = input("Nuevo DNI del apoderado")
                exp["telefono_apoderado"] = input("Nuevo telefono del apoderado")
                exp["nombre_apoderado"] = input("Nuevo nombre del apoderado")
                exp["paterno_apoderado"] = input("Nuevo Apellido Paterno del apoderado")
                exp["materno_apoderado"] = input("Nuevo Apellido Matterno del apoderado")
                exp["correo_estudiante"] = input("Nuevo correo electronico del estudiante")


                exp["nombre_estudiante"] = input("Nuevo nombre del estudiante")
                exp["paterno_estudiante"] = input("Nuevo Apellido Paterno del estudiante")
                exp["materno_estudiante"] = input("Nuevo Apellido Matterno del estudiante")
                exp["dni_estudiante"] = input("Nuevo DNI del estudiante")

                exp["nivel_educativo"] = input("Nuevo Nivel Educativo del estudiante")
                exp["estado_actual"] = input("Nuevo Estado Actual")

                print("\n¡Datos del expediente actualizado con exito!")
                break
        if not encontrado:
            print(f"No encontro ningun expediente con el codigo{codigoBuscar}")
    else:
        print("No hay expedientes registrados")







