# REGISTRO DE PADRES O APODERADOS

padres = []


def generar_codigo_padre(lista):
    numero = len(lista) + 1
    return f"P{numero:03d}"


def solicitar_no_vacio(mensaje):
    while True:
        valor = input(mensaje).strip()

        if valor:
            return valor

        print("ERROR: Este campo no puede estar vacío. Intente nuevamente.")


def validar_dni():
    while True:
        dni = input("Ingrese DNI del padre: ").strip()

        if dni.isdigit() and len(dni) == 8:
            return dni

        print("ERROR: El DNI debe contener exactamente 8 dígitos.")


def validar_nombre(mensaje):
    while True:
        valor = input(mensaje).strip()

        if valor and valor.replace(" ", "").isalpha():
            return valor

        print("ERROR: Ingrese solamente letras y espacios.")


def validar_telefono():
    while True:
        telefono = input("Teléfono: ").strip()

        if telefono.isdigit() and len(telefono) == 9:
            return telefono

        print("ERROR: El teléfono debe contener exactamente 9 dígitos.")


def validar_correo():
    while True:
        correo = input("Correo electrónico: ").strip()

        if (
            correo.count("@") == 1
            and " " not in correo
            and "." in correo.split("@")[1]
            and correo.split("@")[1].split(".")[0]
            and correo.split("@")[1].split(".")[-1]
        ):
            return correo

        print("ERROR: Ingrese un correo electrónico válido.")


def registrar_padre():
    print("\n--- REGISTRO DE PADRE ---")

    dni = validar_dni()

    for padre in padres:
        if padre["dni"] == dni:
            print(
                f"El padre ya se encuentra registrado "
                f"con el código: {padre['codigo']}"
            )
            return padre["codigo"]

    nombres = validar_nombre("Nombres del padre: ")
    paterno = validar_nombre("Apellido paterno: ")
    materno = validar_nombre("Apellido materno: ")
    telefono = validar_telefono()
    correo = validar_correo()

    codigo = generar_codigo_padre(padres)

    nuevo_padre = {
        "codigo": codigo,
        "dni": dni,
        "nombres": nombres,
        "paterno": paterno,
        "materno": materno,
        "telefono": telefono,
        "correo": correo
    }

    padres.append(nuevo_padre)

    print("\n¡PADRE REGISTRADO CON ÉXITO!")
    print("Código asignado:", codigo)

    return codigo


if __name__ == "__main__":
    registrar_padre()
