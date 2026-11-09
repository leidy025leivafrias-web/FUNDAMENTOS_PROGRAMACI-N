
padres = []
estudiantes = []

def generar_codigo(prefijo, lista):
    numero = len(lista) + 1
    return f"{prefijo}{numero:03d}"

def registrar_padre():
    print("\n--- REGISTRO DE PADRE / APODERADO ---")
    dni = input("Ingrese DNI del padre: ").strip()
    
    for padre in padres:
        if padre["dni"] == dni:
            print(f"El padre ya se encuentra registrado con el código: {padre['codigo']}")
            return padre["codigo"]
            
    nombres = input("Nombres del padre: ").strip()
    paterno = input("Apellido paterno: ").strip()
    materno = input("Apellido materno: ").strip()
    telefono = input("Teléfono: ").strip()
    correo = input("Correo electrónico: ").strip()
    
    codigo = generar_codigo("P", padres)
    
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

def registrar_estudiante():
    print("\n--- REGISTRO DE ESTUDIANTE ---")
    dni = input("Ingrese DNI del estudiante: ").strip()
    
    for est in estudiantes:
        if est["dni"] == dni:
            print(f"El estudiante ya se encuentra registrado con el código: {est['codigo']}")
            return est["codigo"]
            
    nombres = input("Nombres del estudiante: ").strip()
    paterno = input("Apellido paterno: ").strip()
    materno = input("Apellido materno: ").strip()
    nivel = input("Nivel educativo (Inicial/Primaria/Secundaria): ").strip()
    
    codigo = generar_codigo("E", estudiantes)
    
    nuevo_estudiante = {
        "codigo": codigo,
        "dni": dni,
        "nombres": nombres,
        "paterno": paterno,
        "materno": materno,
        "nivel": nivel,
        "calificaciones": {
            "bimestre1": 0,
            "bimestre2": 0,
            "bimestre3": 0,
            "promedio": 0,
            "estado_academico": "Pendiente"
        }
    }
    
    estudiantes.append(nuevo_estudiante)
    print(f"¡Estudiante registrado con éxito! Código asignado: {codigo}")
    return codigo
