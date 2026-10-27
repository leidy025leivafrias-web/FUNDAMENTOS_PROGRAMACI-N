
def validar_telefono():
    while True:
        telefono = input("Ingrese el número de teléfono (9 dígitos): ")
        if " " in telefono:
            print("ERROR: El teléfono no debe contener espacios en blanco.")
        elif not telefono.isdigit():
            print("ERROR: El teléfono solo debe contener números.")
        elif len(telefono) != 9:
            print("ERROR: El número de teléfono debe tener exactamente 9 dígitos.")
        else:
            print("Número de teléfono registrado correctamente.")
            return telefono

telefono_usuario = validar_telefono()
print("Teléfono registrado:", telefono_usuario)
