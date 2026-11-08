def Validar__nombres_del_apoderado():
    # VALIDAR APELLIDO PATERNO
    print("PASO 1:")

    while True:
        paterno = input("Ingrese el apellido paterno: ")

        if not paterno.strip():
            print("ERROR: No puede dejar el apellido paterno en blanco.")
        elif not paterno.replace(" ", "").isalpha():
            print("ERROR: El apellido solo debe contener letras.")
        else:
            paterno = paterno.strip()
            print("Apellido paterno registrado correctamente.\n")
        break

    # VALIDAR APELLIDO MATERNO
    while True:
        materno = input("Ingrese el apellido materno: ")

        if not materno.strip():
            print("ERROR: No puede dejar el apellido materno en blanco.")
        elif not materno.replace(" ", "").isalpha():
            print("ERROR: El apellido solo debe contener letras.")
        else:
            materno = materno.strip()
            print("Apellido materno registrado correctamente.\n")
            break

    # VALIDAR NOMBRE COMPLETO
    while True:
        nombre = input("Ingrese el nombre completo: ")

        if not nombre.strip():
            print("ERROR: No puede dejar el nombre en blanco.")
        elif not nombre.replace(" ", "").isalpha():
            print("ERROR: El nombre solo debe contener letras y espacios.")
        else:
            nombre = nombre.strip()
            print("Nombre registrado correctamente.\n")
            break

    # MOSTRAR RESULTADO FINAL
    print("=" * 30)
    print(f"DATOS REGISTRADOS: {nombre} {paterno} {materno}")
    print("=" * 30)

    return nombre, paterno, materno
if __name__ == "__main__":
    Validar__nombres_del_apoderado()