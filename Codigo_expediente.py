def Codigo_expediente(expedientes):

    numeros = []

    for expediente in expedientes:
        codigo = expediente.get("codigo", "")

        if codigo.startswith("EXP"):
            try:
                numeros.append(int(codigo[3:]))
            except ValueError:
                continue

    siguiente = max(numeros, default=0) + 1

    return f"EXP{siguiente:03d}"


if __name__ == "__main__":
    print(Codigo_expediente([]))
