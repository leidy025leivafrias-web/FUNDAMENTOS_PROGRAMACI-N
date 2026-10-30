
def validar_numero():
    print("\nPASO 2: ----CONTACTO DEL APODERADO----")
    while True:
        telefono = input("\n 5. NÚMERO DE CELULAR (9 dígitos): ")
        if " " in telefono:
            print("ERROR: El teléfono no debe contener espacios en blanco.")
        elif not telefono.isdigit():
            print("ERROR: El teléfono solo debe contener números.")
        elif len(telefono) != 9:
            print("ERROR: El número de teléfono debe tener exactamente 9 dígitos.")
        else:
            print("*Número de teléfono registrado correctamente.*")
            return telefono

if __name__ == "__main__":
    telefono_usuario = validar_numero()
    print("Teléfono registrado:", telefono_usuario)