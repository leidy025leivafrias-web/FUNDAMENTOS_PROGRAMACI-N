# MODIFICAR DATOS DEL EXPEDIENTE

def modificar_expediente(expedientes):

    if not expedientes:
        print("No hay expedientes registrados.")
        return

    print("\n--- MODIFICAR DATOS DEL EXPEDIENTE ---")

    codigo_buscar = input(
        "Ingrese el código del expediente (EXP001): "
    ).strip().upper()

    encontrado = next(
        (
            exp for exp in expedientes
            if exp["codigo"].strip().upper() == codigo_buscar
        ),
        None
    )

    if encontrado is None:
        print("No se encontró ningún expediente.")
        return

    print("\nExpediente encontrado.")
    print("Código:", encontrado["codigo"])
    print("Ingrese los nuevos datos.\n")

    # VALIDAR DNI DEL APODERADO
    while True:
        dni = input("Nuevo DNI del apoderado: ").strip()

        if dni.isdigit() and len(dni) == 8:
            break

        print("ERROR: El DNI debe contener exactamente 8 dígitos.")

    # VALIDAR TELÉFONO
    while True:
        telefono = input("Nuevo teléfono del apoderado: ").strip()

        if telefono.isdigit() and len(telefono) == 9:
            break

        print("ERROR: El teléfono debe contener exactamente 9 dígitos.")

    # VALIDAR NOMBRES DEL APODERADO
    nuevos_datos = {}

    campos_apoderado = [
        ("nombre_apoderado", "Nuevo nombre del apoderado: "),
        ("paterno_apoderado", "Nuevo apellido paterno del apoderado: "),
        ("materno_apoderado", "Nuevo apellido materno del apoderado: ")
    ]

    for clave, mensaje in campos_apoderado:
        while True:
            dato = input(mensaje).strip()

            if dato and dato.replace(" ", "").isalpha():
                nuevos_datos[clave] = dato
                break

            print("ERROR: Ingrese solamente letras y espacios.")

    # VALIDAR CORREO ELECTRÓNICO
    while True:
        correo = input("Nuevo correo del apoderado: ").strip()

        if (
            correo.count("@") == 1
            and " " not in correo
            and correo.split("@")[0]
            and correo.split("@")[1] == "gmail.com"
            and "." not in correo.split("@")[0]
                or False
        ):
            # Esta condición se sustituye por la validación inferior.
            pass

        partes = correo.split("@")

        if (
            len(partes) == 2
            and partes[0]
            and partes[1].lower() == "gmail.com"
            and "." not in partes[0]
            and correo.count("@") == 1
            and " " not in correo
        ):
            break

        print("ERROR: Ingrese un correo válido terminado en @gmail.com.")

    # VALIDAR NOMBRES DEL ESTUDIANTE
    campos_estudiante = [
        ("nombre_estudiante", "Nuevo nombre del estudiante: "),
        ("paterno_estudiante", "Nuevo apellido paterno del estudiante: "),
        ("materno_estudiante", "Nuevo apellido materno del estudiante: ")
    ]

    for clave, mensaje in campos_estudiante:
        while True:
            dato = input(mensaje).strip()

            if dato and dato.replace(" ", "").isalpha():
                nuevos_datos[clave] = dato
                break

            print("ERROR: Ingrese solamente letras y espacios.")

    # VALIDAR DNI DEL ESTUDIANTE
    dni_anterior = encontrado["dni_estudiante"]

    while True:
        dni_estudiante = input("Nuevo DNI del estudiante: ").strip()

        if not dni_estudiante.isdigit() or len(dni_estudiante) != 8:
            print("ERROR: El DNI debe contener exactamente 8 dígitos.")
            continue

        duplicado = any(
            exp is not encontrado
            and exp["dni_estudiante"] == dni_estudiante
            for exp in expedientes
        )

        if duplicado:
            print("ERROR: Ese DNI ya pertenece a otro estudiante.")
            continue

        break

    # VALIDAR NIVEL EDUCATIVO
    niveles = {
        "1": "Inicial",
        "2": "Primaria",
        "3": "Secundaria",
        "4": "EBE (Educación Básica Especial)"
    }

    while True:
        print("\nSeleccione el nuevo nivel educativo:")
        print("1. Inicial")
        print("2. Primaria")
        print("3. Secundaria")
        print("4. EBE (Educación Básica Especial)")

        opcion = input("Seleccione una opción: ").strip()

        if opcion in niveles:
            nivel = niveles[opcion]
            break

        print("ERROR: Seleccione una opción del 1 al 4.")

    # VALIDAR ESTADO DEL TRÁMITE
    estados = {
        "1": "PENDIENTE",
        "2": "EN PROCESO",
        "3": "ATENDIDO",
        "4": "RECHAZADO"
    }

    while True:
        print("\nSeleccione el nuevo estado del trámite:")
        print("1. Pendiente")
        print("2. En proceso")
        print("3. Atendido")
        print("4. Rechazado")

        opcion = input("Seleccione una opción: ").strip()

        if opcion in estados:
            estado = estados[opcion]
            break

        print("ERROR: Seleccione una opción del 1 al 4.")

    # ACTUALIZAR LOS DATOS
    encontrado["dni_apoderado"] = dni
    encontrado["telefono_apoderado"] = telefono
    encontrado["correo_apoderado"] = correo

    encontrado.update(nuevos_datos)

    encontrado["dni_estudiante"] = dni_estudiante
    encontrado["nivel"] = nivel
    encontrado["estado"] = estado

    # ELIMINAR CALIFICACIONES SI CAMBIÓ EL DNI
    if dni_anterior != dni_estudiante:
        encontrado.pop("calificaciones", None)
        print("\nLas calificaciones anteriores fueron eliminadas.")

    print("\n¡DATOS DEL EXPEDIENTE ACTUALIZADOS CON ÉXITO!")
    print("Código:", encontrado["codigo"])
