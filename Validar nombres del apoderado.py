# VALIDAR APELIDO PATERNO
while True:
    paterno = input("Ingrese el apellido paterno: ")
    if not paterno.isalpha():
        print("ERROR: El apellido solo debe contener letras.")
    else:
        print("Apellido paterno registrado correctamente.\n")
        break

# VALIDAR APELLIDO MATERNO
while True:
    materno = input("Ingrese el apellido materno: ")
    if not materno.isalpha():
        print("ERROR: El apellido solo debe contener letras.")
    else:
        print("Apellido materno registrado correctamente.\n")
        break

# VALIDAR NOMBRE COMPLETO
while True:
    nombre = input("Ingrese el nombre completo: ")
    # Reemplazamos los espacios para verificar si todo lo demás son letras
    if not nombre.replace(" ", "").isalpha():
        print("ERROR: El nombre solo debe contener letras y espacios.")
    else:
        print("Nombre registrado correctamente.\n")
        break

# MOSTRAR RESULTADO FINAL
print("=" * 1)
print(f"DATOS REGISTRADOS: {nombre} {paterno} {materno}")
print("=" * 1)