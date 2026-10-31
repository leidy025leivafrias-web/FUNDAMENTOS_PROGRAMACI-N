
def validar_dni_apoderado():
    print("\n---- PASO 1: IDENTIFICACIÓN DEL APODERADO----")
    while True:
        dni = input("\n1. INGRESE EL DNI DEL APODERADO (8 dígitos): ")
        if " " in dni:
            print("ERROR: El DNI no debe contener espacios en blanco.")
        elif not dni.isdigit():
            print("ERROR: El DNI solo debe contener números.")
        elif len(dni) != 8:
            print("ERROR: El DNI debe tener exactamente 8 dígitos.")
        else:
            print("*DNI del apoderado registrado correctamente.*")
            return dni
if __name__ == "__main__":
  dni_apoderado = validar_dni_apoderado()
  
  print("DNI registrado:", dni_apoderado)

def validar_dni_estudiante():
    print("\nPASO 3: ---- IDENTIFICACIÓN DEL ESTUDIANTE ---")
    while True:
        dni = input("7. INGRESE EL DNI DEL ESTUDIANTE (8 dígitos): ")

        if " " in dni:
            print("ERROR: El DNI no debe contener espacios en blanco.")
        elif not dni.isdigit():
            print("ERROR: El DNI solo debe contener números.")
        elif len(dni) != 8:
            print("ERROR: El DNI debe tener exactamente 8 dígitos.")
        else:
            print("*DNI del estudiante registrado correctamente.*")
            return dni