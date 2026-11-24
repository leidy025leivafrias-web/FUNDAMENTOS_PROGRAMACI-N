
# VALIDAR CORREO ELECTRÓNICO

def validar_correo():

    while True:

        correo = input(
            "Nuevo correo del apoderado: "
        ).strip()

        partes = correo.split("@")

        if (
            len(partes) == 2
            and partes[0]
            and partes[1].lower() == "gmail.com"
            and " " not in correo
            and not partes[0].startswith(".")
            and not partes[0].endswith(".")
        ):
            print("Correo electrónico registrado correctamente.")
            return correo

        print(
            "ERROR: Ingrese un correo válido terminado en @gmail.com."
        )


if __name__ == "__main__":
    validar_correo()
