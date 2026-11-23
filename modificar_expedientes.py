# MODIFICAR DATOS DEL EXPEDIENTE
def modificar_expediente(expedientes):

    if not expedientes:
        print("No hay expedientes registrados.")
        return

    print("\n--- MODIFICAR DATOS DEL EXPEDIENTE ---")

    codigo_buscar = input(
        "Ingrese el código del expediente (EXP-1001): "
    ).strip().upper()

    encontrado = None

    for exp in expedientes:
        if exp["codigo"].strip().upper() == codigo_buscar:
            encontrado = exp
            break

    if encontrado is None:
        print("No se encontró ningún expediente con ese código.")
        return

    print("\nExpediente encontrado.")
    print("Código:", encontrado["codigo"])
    print("Ingrese los nuevos datos.\n")

    # VALIDAR DNI DEL APODERADO
    while True:
        dni = input("Nuevo DNI del apoderado: ").strip()

        if dni.isdigit() and len(dni) == 8:
            encontrado["dni_apoderado"] = dni
            break

        print("ERROR: El DNI debe contener exactamente 8 dígitos.")

    # VALIDAR TELÉFONO
    while True:
        telefono = input("Nuevo teléfono del apoderado: ").strip()

        if telefono.isdigit() and len(telefono) == 9:
            encontrado["telefono_apoderado"] = telefono
            break

        print("ERROR: El teléfono debe contener exactamente 9 dígitos.")

    # VALIDAR DATOS DEL APODERADO
    campos_apoderado = [
        ("nombre_apoderado", "Nuevo nombre del apoderado: "),
        ("paterno_apoderado", "Nuevo apellido paterno del apoderado: "),
        ("materno_apoderado", "Nuevo apellido materno del apoderado: ")
    ]

    for clave, mensaje in campos_apoderado:
        while True:
            dato = input(mensaje).strip()

            if dato and dato.replace(" ", "").isalpha():
                encontrado[clave] = dato
                break

            print("ERROR: Ingrese solamente letras y espacios.")

    # VALIDAR CORREO DEL APODERADO
    while True:
        correo = input("Nuevo correo del apoderado: ").strip()

        if (
            correo.count("@") == 1
            and " " not in correo
            and "." in correo.split("@")[1]
            and correo.split("@")[1].split(".")[0]
            and correo.split("@")[1].split(".")[-1]
        ):
            encontrado["correo_apoderado"] = correo
            break

        print("ERROR: Ingrese un correo electrónico válido.")

    # VALIDAR DATOS DEL ESTUDIANTE
    campos_estudiante = [
        ("nombre_estudiante", "Nuevo nombre del estudiante: "),
        ("paterno_estudiante", "Nuevo apellido paterno del estudiante: "),
        ("materno_estudiante", "Nuevo apellido materno del estudiante: ")
    ]

    for clave, mensaje in campos_estudiante:
        while True:
            dato = input(mensaje).strip()

            if dato and dato.replace(" ", "").isalpha():
                encontrado[clave] = dato
                break

            print("ERROR: Ingrese solamente letras y espacios.")

    # VALIDAR DNI DEL ESTUDIANTE
    while True:
        dni_estudiante = input("Nuevo DNI del estudiante: ").strip()

        if dni_estudiante.isdigit() and len(dni_estudiante) == 8:
            encontrado["dni_estudiante"] = dni_estudiante
            break

        print("ERROR: El DNI debe contener exactamente 8 dígitos.")

    # VALIDAR NIVEL EDUCATIVO
    while True:
        nivel = input("Nuevo nivel educativo: ").strip()

        if nivel:
            encontrado["nivel"] = nivel
            break

        print("ERROR: El nivel educativo no puede estar vacío.")

    # VALIDAR ESTADO DEL TRÁMITE
    while True:
        estado = input("Nuevo estado del trámite: ").strip()

        if estado:
            encontrado["estado"] = estado
            break

        print("ERROR: El estado no puede estar vacío.")

    print("\n¡DATOS DEL EXPEDIENTE ACTUALIZADOS CON ÉXITO!")
    print("Código:", encontrado["codigo"])


if __name__ == "__main__":
    modificar_expediente([])






