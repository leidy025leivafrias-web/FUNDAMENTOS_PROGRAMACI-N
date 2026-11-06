def leer_nota_valida(mensaje):
    while True:
        try:
            nota = float(input(mensaje))
            if 0 <= nota <= 20:
                return nota
            print("Error: la nota debe estar entre 0 y 20.")
        except ValueError:
            print("Error: ingrese un número válido.")