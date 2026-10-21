#VALIDAR INGRESO CORRECTO DEL TELEFONO

def validar_telefono():
    while True:
        telefono = input("Ingrese el número de teléfono (9 dígitos): ")
        
        if not telefono.isdigit():
            print("ERROR: El teléfono solo debe contener números.")
        elif len(telefono) != 9:
            print("ERROR: El número de teléfono debe tener exactamente 9 dígitos.")
        else:
            print("Número de teléfono registrado correctamente.")
            return telefono

#Llamar a la función
telefono_usuario = validar_telefono()
print("Teléfono registrado:", telefono_usuario)