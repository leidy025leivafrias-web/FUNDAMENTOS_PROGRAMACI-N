
# CONTADOR PARA GENERAR CODIGOS UNICOS
contador = 1

# REGISTRO DE DATOS DE LA MADRE

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

# GENERAR CODIGO DE LA MADRE
codigo_madre = "MAD" + str(contador).zfill(3)
contador += 1


# REGISTRO DE DATOS DEL ESTUDIANTE

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

# GENERAR CODIGO DEL ESTUDIANTE
codigo_estudiante = "EST" + str(contador).zfill(3)
contador += 1


# REGISTRO DE DATOS DEL PADRE

# VALIDAR APELLIDO PATERNO DEL PADRE
while True:
    paterno_padre = input("Ingrese el apellido paterno del padre: ")

    if not paterno_padre.strip():
        print("ERROR: No puede dejar el apellido paterno en blanco.")
    elif not paterno_padre.replace(" ", "").isalpha():
        print("ERROR: El apellido solo debe contener letras.")
    else:
        paterno_padre = paterno_padre.strip()
        print("Apellido paterno del padre registrado correctamente.\n")
        break

# VALIDAR APELLIDO MATERNO DEL PADRE
while True:
    materno_padre = input("Ingrese el apellido materno del padre: ")

    if not materno_padre.strip():
        print("ERROR: No puede dejar el apellido materno en blanco.")
    elif not materno_padre.replace(" ", "").isalpha():
        print("ERROR: El apellido solo debe contener letras.")
    else:
        materno_padre = materno_padre.strip()
        print("Apellido materno del padre registrado correctamente.\n")
        break

# VALIDAR NOMBRE COMPLETO DEL PADRE
while True:
    nombre_padre = input("Ingrese el nombre completo del padre: ")

    if not nombre_padre.strip():
        print("ERROR: No puede dejar el nombre en blanco.")
    elif not nombre_padre.replace(" ", "").isalpha():
        print("ERROR: El nombre solo debe contener letras y espacios.")
    else:
        nombre_padre = nombre_padre.strip()
        print("Nombre del padre registrado correctamente.\n")
        break

# GENERAR CODIGO DEL PADRE
codigo_padre = "PAD" + str(contador).zfill(3)
contador += 1


# MOSTRAR RESULTADOS FINALES

print("=" * 45)
print("       DATOS REGISTRADOS CORRECTAMENTE")
print("=" * 45)

print("\nDATOS DE LA MADRE:")
print(f"Codigo: {codigo_madre}")
print(f"Nombre completo: {nombre_madre} {paterno_madre} {materno_madre}")

print("\nDATOS DEL ESTUDIANTE:")
print(f"Codigo: {codigo_estudiante}")
print(f"Nombre completo: {nombre_estudiante} {paterno_estudiante} {materno_estudiante}")

print("\nDATOS DEL PADRE:")
print(f"Codigo: {codigo_padre}")
print(f"Nombre completo: {nombre_padre} {paterno_padre} {materno_padre}")

print("=" * 45)
