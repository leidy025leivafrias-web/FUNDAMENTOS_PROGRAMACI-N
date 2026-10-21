# VALIDAR APELLIDO PATERNO DEL ESTUDIANTE
while True:
    paterno_estudiante = input("Ingrese el apellido paterno del estudiante: ")
    if not paterno_estudiante.isalpha():
        print("ERROR: El apellido solo debe contener letras.")
    else:
        print("Apellido paterno del estudiante registrado correctamente.\n")
        break

# VALIDAR APELLIDO MATERNO DEL ESTUDIANTE
while True:
    materno_estudiante = input("Ingrese el apellido materno del estudiante: ")
    if not materno_estudiante.isalpha():
        print("ERROR: El apellido solo debe contener letras.")
    else:
        print("Apellido materno del estudiante registrado correctamente.\n")
        break

# VALIDAR NOMBRE COMPLETO DEL ESTUDIANTE
while True:
    nombre_estudiante = input("Ingrese el nombre completo del estudiante: ")
    # Reemplazamos los espacios para verificar si todo lo demás son letras
    if not nombre_estudiante.replace(" ", "").isalpha():
        print("ERROR: El nombre solo debe contener letras y espacios.")
    else:
        print("Nombre del estudiante registrado correctamente.\n")
        break

# MOSTRAR RESULTADO FINAL
print("=" * 30)
print(f"DATOS DEL ESTUDIANTE REGISTRADOS: {nombre_estudiante} {paterno_estudiante} {materno_estudiante}")
print("=" * 30)