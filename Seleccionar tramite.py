# VALIDAR Y SELECCIONAR TRÁMITE

def seleccionar_tramite():
    while True:
        tramite = input(
            "Ingrese el trámite que desea realizar: "
        ).strip()

        if not tramite:
            print("ERROR: No puede dejar el trámite en blanco.")

        elif not tramite.replace(" ", "").isalpha():
            print("ERROR: El trámite solo debe contener letras y espacios.")

        else:
            print("Trámite registrado correctamente.\n")
            break

    print("=" * 30)
    print(f"TRÁMITE SELECCIONADO: {tramite}")
    print("=" * 30)

    return tramite


if __name__ == "__main__":
    seleccionar_tramite()

