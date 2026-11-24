# VALIDAR CORREO ELECTRÓNICO
while True:
    correo = input("Nuevo correo del apoderado: ").strip()

    partes = correo.split("@")

    if (
        len(partes) == 2
        and partes[0]
        and partes[1].lower() == "gmail.com"
        and " " not in correo
    ):
        break

    print("ERROR: Ingrese un correo válido terminado en @gmail.com.")
