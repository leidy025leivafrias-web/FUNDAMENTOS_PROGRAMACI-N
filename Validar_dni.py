#VALIDAR INGRESO CORRECTO DE DATOS DEL APODERADO (DNI)

def validar_dni_apoderado():
    while True:
        dni = input("Ingrese el DNI del apoderado (8 dígitos): ")

        if not dni.isdigit():
            print("ERROR: El DNI solo debe contener números.")
        elif len(dni) != 8:
            print("ERROR: El DNI debe tener exactamente 8 dígitos.")
        else:
            print("DNI del apoderado registrado correctamente.")
            return dni


# Llamar a la función
dni_apoderado = validar_dni_apoderado()

print("DNI registrado:", dni_apoderado)
