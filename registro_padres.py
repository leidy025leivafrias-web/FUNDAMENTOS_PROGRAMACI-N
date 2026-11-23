padres = []

def generar_codigo_padre(lista):
    numero = len(lista) + 1
    return f"P{numero:03d}"

def solicitar_no_vacio(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Este campo no puede estar vacío. Intente nuevamente.")

def registrar_padre():
    print("\n--- REGISTRO DE PADRE ---")
    dni = solicitar_no_vacio("Ingrese DNI del padre: ")

    for padre in padres:
        if padre["dni"] == dni:
            print(f"El padre ya se encuentra registrado con el código: {padre['codigo']}")
            return padre["codigo"]

    nombres = solicitar_no_vacio("Nombres del padre: ")
    paterno = solicitar_no_vacio("Apellido paterno: ")
    materno = solicitar_no_vacio("Apellido materno: ")
    telefono = solicitar_no_vacio("Teléfono: ")
    correo = solicitar_no_vacio("Correo electrónico: ")

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
    print(f"¡Padre registrado con éxito! Código asignado: {codigo}")
    return codigo
