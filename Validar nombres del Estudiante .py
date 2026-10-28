
# VALIDAR APELLIDO PATERNO DEL ESTUDIANTE
while True:
    paterno_estudiante = input("Ingrese el apellido paterno del estudiante: ")

    if not paterno_estudiante.strip():
        print("ERROR: No puede dejar el apellido paterno en blanco.")
    elif not paterno_estudiante.replace(" ", "").isalpha():
        print("ERROR: El apellido solo debe contener letras.")
    else:
        paterno_estudiante = paterno_estudiante.strip()
        print("Apellido paterno del estudiante registrado correctamente.\n")
        break

# VALIDAR APELLIDO MATERNO DEL ESTUDIANTE
while True:
    materno_estudiante = input("Ingrese el apellido materno del estudiante: ")

    if not materno_estudiante.strip():
        print("ERROR: No puede dejar el apellido materno en blanco.")
    elif not materno_estudiante.replace(" ", "").isalpha():
        print("ERROR: El apellido solo debe contener letras.")
    else:
        materno_estudiante = materno_estudiante.strip()
        print("Apellido materno del estudiante registrado correctamente.\n")
        break

# VALIDAR NOMBRE COMPLETO DEL ESTUDIANTE
while True:
    nombre_estudiante = input("Ingrese el nombre completo del estudiante: ")

    if not nombre_estudiante.strip():
        print("ERROR: No puede dejar el nombre en blanco.")
    elif not nombre_estudiante.replace(" ", "").isalpha():
        print("ERROR: El nombre solo debe contener letras y espacios.")
    else:
        nombre_estudiante = nombre_estudiante.strip()
        print("Nombre del estudiante registrado correctamente.\n")
        break

# MOSTRAR RESULTADO FINAL
print("=" * 30)
print(f"DATOS DEL ESTUDIANTE REGISTRADOS: {nombre_estudiante} {paterno_estudiante} {materno_estudiante}")
print("=" * 30)
