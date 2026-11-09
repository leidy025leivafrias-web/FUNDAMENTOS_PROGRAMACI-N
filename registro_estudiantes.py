estudiantes = []

def generar_codigo_estudiante(lista):
    numero = len(lista) + 1
    return f"E{numero:03d}"

def registrar_estudiante():
    print ("\n--- REGISTRO DE ESTUDIANTES ---")
    dni = input("Ingrese DNI del estudiante: ").strip()
    
    for est in estudiantes:
        if est["dni"] == dni:
            print(f"El estudiante ya se encuentra registrado con el código: {est['codigo']}")
            return est["codigo"]
            
    nombres = input("Nombres del estudiante: ").strip()
    paterno = input("Apellido paterno: ").strip()
    materno = input("Apellido materno: ").strip()
    nivel = input("Nivel educativo (Inicial/Primaria/Secundaria): ").strip()
    
    codigo = generar_codigo_estudiante(estudiantes)
    
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