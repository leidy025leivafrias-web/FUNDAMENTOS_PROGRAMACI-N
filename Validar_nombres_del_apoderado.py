# VALIDAR NOMBRES Y APELLIDOS DEL APODERADO

def Validar__nombres_del_apoderado():

    # VALIDAR APELLIDO PATERNO
    while True:
        paterno = input("2. APELLIDO PATERNO: ").strip()

        if not paterno:
            print("ERROR: No puede dejar el apellido paterno en blanco.")
        elif not paterno.replace(" ", "").isalpha():
            print("ERROR: El apellido solo debe contener letras y espacios.")
        else:
            print("Apellido paterno registrado correctamente.\n")
            break

    # VALIDAR APELLIDO MATERNO
    while True:
        materno = input("3. APELLIDO MATERNO: ").strip()

        if not materno:
            print("ERROR: No puede dejar el apellido materno en blanco.")
        elif not materno.replace(" ", "").isalpha():
            print("ERROR: El apellido solo debe contener letras y espacios.")
        else:
            print("Apellido materno registrado correctamente.\n")
            break

    # VALIDAR NOMBRES
    while True:
        nombre = input("4. NOMBRES: ").strip()

        if not nombre:
            print("ERROR: No puede dejar el nombre en blanco.")
        elif not nombre.replace(" ", "").isalpha():
            print("ERROR: El nombre solo debe contener letras y espacios.")
        else:
            print("Nombre registrado correctamente.\n")
            break

    # MOSTRAR RESULTADO FINAL
    print("=" * 30)
    print(f"DATOS REGISTRADOS: {nombre} {paterno} {materno}")
    print("=" * 30)

    return nombre, paterno, materno


if __name__ == "__main__":
    Validar__nombres_del_apoderado()
