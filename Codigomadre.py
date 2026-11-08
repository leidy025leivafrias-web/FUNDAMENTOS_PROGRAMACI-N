# VALIDAR APELLIDO PATERNO DE LA MADRE
while True:
    paterno_madre = input("Ingrese el apellido paterno de la madre: ")

    if not paterno_madre.strip():
        print("ERROR: No puede dejar el apellido paterno en blanco.")
    elif not paterno_madre.replace(" ", "").isalpha():
        print("ERROR: El apellido solo debe contener letras.")
    else:
        paterno_madre = paterno_madre.strip()
        print("Apellido paterno de la madre registrado correctamente.\n")
        break

# VALIDAR APELLIDO MATERNO DE LA MADRE
while True:
    materno_madre = input("Ingrese el apellido materno de la madre: ")

    if not materno_madre.strip():
        print("ERROR: No puede dejar el apellido materno en blanco.")
    elif not materno_madre.replace(" ", "").isalpha():
        print("ERROR: El apellido solo debe contener letras.")
    else:
        materno_madre = materno_madre.strip()
        print("Apellido materno de la madre registrado correctamente.\n")
        break

# VALIDAR NOMBRE COMPLETO DE LA MADRE
while True:
    nombre_madre = input("Ingrese el nombre completo de la madre: ")

    if not nombre_madre.strip():
        print("ERROR: No puede dejar el nombre en blanco.")
    elif not nombre_madre.replace(" ", "").isalpha():
        print("ERROR: El nombre solo debe contener letras y espacios.")
    else:
        nombre_madre = nombre_madre.strip()
        print("Nombre de la madre registrado correctamente.\n")
        break

# MOSTRAR RESULTADO FINAL
print("=" * 30)
print(f"DATOS DE LA MADRE REGISTRADOS: {nombre_madre} {paterno_madre} {materno_madre}")
print("=" * 30)