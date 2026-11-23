def buscar_expedientes(expedientes):
    if not expedientes:
        print("No hay expedientes registrados en el sistema.")
        return

    codigo_buscar = input(
        "Ingrese el código del expediente: "
    ).strip().upper()

    encontrado = None

    for expediente in expedientes:
        if expediente["codigo"].upper() == codigo_buscar:
            encontrado = expediente
            break

    if encontrado is None:
        print("No se encontró ningún expediente con ese código.")
        return

    print("\n--- EXPEDIENTE ENCONTRADO ---")
    print("Código:", encontrado["codigo"])
    print("DNI del apoderado:", encontrado["dni_apoderado"])
    print("Apoderado:", encontrado["nombre_apoderado"],
          encontrado["paterno_apoderado"],
          encontrado["materno_apoderado"])
    print("Teléfono:", encontrado["telefono_apoderado"])
    print("Correo:", encontrado["correo_apoderado"])

    print("\n--- DATOS DEL ESTUDIANTE ---")
    print("DNI:", encontrado["dni_estudiante"])
    print("Estudiante:", encontrado["nombre_estudiante"],
          encontrado["paterno_estudiante"],
          encontrado["materno_estudiante"])
    print("Nivel educativo:", encontrado["nivel"])
    print("Estado del trámite:", encontrado["estado"])

    notas = encontrado.get("calificaciones")

    if notas:
        print("\n--- CALIFICACIONES ---")
        print("I Bimestre:", notas["bimestre1"])
        print("II Bimestre:", notas["bimestre2"])
        print("III Bimestre:", notas["bimestre3"])
        print("Promedio:", notas["promedio"])
        print("Estado académico:", notas["estado_academico"])
    else:
        print("\nEl expediente todavía no tiene calificaciones.")
