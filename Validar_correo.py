def validar_correo():
    while True:
        correo = input("6.CORREO ELECTRÓNICO: ")

        if " " in correo:
            print("ERROR: El correo no debe contener espacios.")
        elif "@" not in correo:
            print("ERROR: El correo debe contener @.")
        elif correo.count("@") != 1:
            print("ERROR: El correo debe tener un solo @.")
        elif correo.split("@")[1] != "gmail.com":
            print("ERROR: El correo debe terminar en gmail.com.")
        else:
            print("*Correo registrado correctamente.*")
            return correo

if __name__ == "__main__":
    correo = validar_correo()
    print("Correo registrado:", correo)