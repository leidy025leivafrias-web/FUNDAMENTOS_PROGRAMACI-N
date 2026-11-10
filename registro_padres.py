padres = []

def generar_codigo_padre(lista):
    numero = len(lista) + 1
    return f"P{numero:03d}"

def registrar_padre():
    print("\n--- REGISTRO DE PADRE ---")
    dni = input("Ingrese DNI del padre: ").strip

    for padre in padres:
        if padre["dni"] == dni:
            print(f"El padre ya se encuentra registrado con el código: {padre['codigo']}")
            return padre["codigo"]
            
    nombres = input("Nombres del padre: ").strip()
    paterno = input("Apellido平aterno: ").strip()
    materno = input("Apellido materno: ").strip()
    telefono = input("Teléfono: ").strip()
    correo = input("Correo electrónico: ").strip()
    
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