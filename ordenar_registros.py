
# ORDENAR POR PROMEDIO
def ordenar_registros():

    if len(expedientes) < 2:
        print("Se necesitan al menos 2 expedientes para ordenar.")
        return

    expedientes_ordenados = sorted(
        expedientes,
        key=lambda exp: exp.get("calificaciones", {}).get("promedio", -1),
        reverse=True
    )

    print("\nEXPEDIENTES ORDENADOS POR PROMEDIO")
    print("----------------------------------------")

    for i, expediente in enumerate(expedientes_ordenados, start=1):

        notas = expediente.get("calificaciones")

        print(f"\n{i}. Código: {expediente['codigo']}")
        print(
            "Estudiante:",
            expediente["nombre_estudiante"],
            expediente["paterno_estudiante"],
            expediente["materno_estudiante"]
        )

        if notas:
            print("Promedio:", notas["promedio"])
            print("Estado:", notas["estado_academico"])
        else:
            print("Sin calificaciones registradas.")

    print("----------------------------------------")
