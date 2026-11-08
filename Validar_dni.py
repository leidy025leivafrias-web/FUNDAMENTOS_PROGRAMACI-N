
def validar_dni_apoderado():
    print("PASO 2:")
    while True:
        dni = input("Ingrese el DNI del apoderado (8 dígitos): ")
        if " " in dni:
            print("ERROR: El DNI no debe contener espacios en blanco.")
        elif not dni.isdigit():
            print("ERROR: El DNI solo debe contener números.")
        elif len(dni) != 8:
            print("ERROR: El DNI debe tener exactamente 8 dígitos.")
        else:
            print("DNI del apoderado registrado correctamente.")
            return dni
if __name__ == "__main__":
  dni_apoderado = validar_dni_apoderado()
  
  print("DNI registrado:", dni_apoderado)

def validar_dni_estudiante():
    while True:
        dni = input("Ingrese el DNI del estudiante (8 dígitos): ")

        if " " in dni:
            print("ERROR: El DNI no debe contener espacios en blanco.")
        elif not dni.isdigit():
            print("ERROR: El DNI solo debe contener números.")
        elif len(dni) != 8:
            print("ERROR: El DNI debe tener exactamente 8 dígitos.")
        else:
            print("DNI del estudiante registrado correctamente.")
            return dni