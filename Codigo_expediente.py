# CONTADOR DE EXPEDIENTES
contador = 1

# VALIDAR TRÁMITE A REALIZAR
while True:
    tramite = input("Ingrese el trámite que desea realizar: ")

    # Validar que no esté vacío ni contenga solo espacios
    if not tramite.strip():
        print("ERROR: No puede dejar el trámite en blanco.")

    # Validar que solo contenga letras y espacios
    elif not tramite.replace(" ", "").isalpha():
        print("ERROR: El trámite solo debe contener letras y espacios.")

    else:
        print("Trámite registrado correctamente.\n")
        break


# GENERAR CÓDIGO DEL EXPEDIENTE
if contador < 10:
    codigo = "EXP-0" + str(contador)
else:
    codigo = "EXP-" + str(contador)

contador = contador + 1


# MOSTRAR RESULTADO FINAL
print("=" * 30)
print("EXPEDIENTE REGISTRADO")
print("=" * 30)
print(f"TRÁMITE: {tramite}")
print(f"CÓDIGO DEL EXPEDIENTE: {codigo}")
print("=" * 30)