# ============================================================
# SISTEMA DE REGISTRO DE CALIFICACIONES ESCOLARES
# ============================================================

def Expedientes(expedientes):

    # VALIDAR NOTAS
    def leer_nota_valida(mensaje):
        while True:
            try:
                entrada = input(mensaje).strip().replace(",", ".")
                nota = float(entrada)

                if 0 <= nota <= 20:
                    return nota

                print("ERROR: La nota debe estar entre 0 y 20.")

            except ValueError:
                print("ERROR: Ingrese un valor numérico válido.")

    # CALCULAR PROMEDIO
    def calcular_promedio(nota1, nota2, nota3):
        promedio = round((nota1 + nota2 + nota3) / 3, 2)

        estado = "APROBADO" if promedio >= 11 else "DESAPROBADO"

        return promedio, estado

    # BUSCAR EXPEDIENTE
    def buscar_por_codigo(codigo):
        for expediente in expedientes:
            if expediente["codigo"].strip().upper() == codigo:
                return expediente

        return None

    # MOSTRAR CALIFICACIONES
    def mostrar_calificaciones(expediente):

        print("\n----------------------------------------")
        print("REGISTRO DE CALIFICACIONES")
        print("----------------------------------------")
        print("Código:", expediente["codigo"])
        print("DNI:", expediente["dni_estudiante"])
        print(
            "Estudiante:",
            expediente["nombre_estudiante"],
            expediente["paterno_estudiante"],
            expediente["materno_estudiante"]
        )

        notas = expediente.get("calificaciones")

        if notas:
            print("I Bimestre:", notas["bimestre1"])
            print("II Bimestre:", notas["bimestre2"])
            print("III Bimestre:", notas["bimestre3"])
            print("Promedio final:", notas["promedio"])
            print("Estado académico:", notas["estado_academico"])
        else:
            print("El estudiante todavía no tiene calificaciones.")

        print("----------------------------------------")

    # REGISTRAR CALIFICACIONES
    def registrar_calificaciones():

        if not expedientes:
            print("No hay estudiantes registrados.")
            return

        print("\n===== REGISTRAR CALIFICACIONES =====")

        codigo = input("Ingrese el código del expediente: ").strip().upper()

        expediente = buscar_por_codigo(codigo)

        if expediente is None:
            print("No existe un expediente con ese código.")
            return

        if expediente.get("calificaciones"):
            print("El estudiante ya tiene calificaciones.")
            print("Utilice la opción de actualizar calificaciones.")
            return

        print("\nEstudiante encontrado:")
        print(
            expediente["nombre_estudiante"],
            expediente["paterno_estudiante"],
            expediente["materno_estudiante"]
        )

        nota1 = leer_nota_valida("Ingrese nota del I Bimestre: ")
        nota2 = leer_nota_valida("Ingrese nota del II Bimestre: ")
        nota3 = leer_nota_valida("Ingrese nota del III Bimestre: ")

        promedio, estado = calcular_promedio(nota1, nota2, nota3)

        expediente["calificaciones"] = {
            "bimestre1": nota1,
            "bimestre2": nota2,
            "bimestre3": nota3,
            "promedio": promedio,
            "estado_academico": estado
        }

        print("\n¡CALIFICACIONES REGISTRADAS CORRECTAMENTE!")
        print("Promedio final:", promedio)
        print("Estado académico:", estado)

    # BUSCAR REGISTRO
    def buscar_registro():

        if not expedientes:
            print("No hay expedientes registrados.")
            return

        busqueda = input(
            "Ingrese el código del expediente o DNI del estudiante: "
        ).strip().upper()

        encontrado = None

        for expediente in expedientes:
            if (
                expediente["codigo"].strip().upper() == busqueda
                or expediente["dni_estudiante"] == busqueda
            ):
                encontrado = expediente
                break

        if encontrado:
            mostrar_calificaciones(encontrado)
        else:
            print("No se encontró ningún registro.")

    # ORDENAR POR PROMEDIO
    def ordenar_registros():

        if len(expedientes) < 2:
            print("Se necesitan al menos 2 expedientes para ordenar.")
            return

        expedientes.sort(
            key=lambda exp: exp.get("calificaciones", {}).get("promedio", -1),
            reverse=True
        )

        print("\nExpedientes ordenados por promedio de mayor a menor.")
        listar_registros()

    # ACTUALIZAR CALIFICACIONES
    def actualizar_calificaciones():

        if not expedientes:
            print("No hay estudiantes registrados.")
            return

        codigo = input(
            "Ingrese el código del expediente: "
        ).strip().upper()

        expediente = buscar_por_codigo(codigo)

        if expediente is None:
            print("No existe un expediente con ese código.")
            return

        if not expediente.get("calificaciones"):
            print("El estudiante todavía no tiene calificaciones.")
            print("Utilice la opción registrar calificaciones.")
            return

        mostrar_calificaciones(expediente)

        print("\nIngrese las nuevas calificaciones:")

        nota1 = leer_nota_valida("Nuevo I Bimestre: ")
        nota2 = leer_nota_valida("Nuevo II Bimestre: ")
        nota3 = leer_nota_valida("Nuevo III Bimestre: ")

        promedio, estado = calcular_promedio(nota1, nota2, nota3)

        expediente["calificaciones"] = {
            "bimestre1": nota1,
            "bimestre2": nota2,
            "bimestre3": nota3,
            "promedio": promedio,
            "estado_academico": estado
        }

        print("\n¡CALIFICACIONES ACTUALIZADAS CORRECTAMENTE!")
        print("Nuevo promedio:", promedio)
        print("Estado académico:", estado)

    # LISTAR REGISTROS
    def listar_registros():

        if not expedientes:
            print("No hay expedientes registrados.")
            return

        print("\n========== LISTADO DE CALIFICACIONES ==========")

        for i, expediente in enumerate(expedientes, start=1):

            print(f"\n{i}. Código: {expediente['codigo']}")
            print("DNI:", expediente["dni_estudiante"])
            print(
                "Estudiante:",
                expediente["nombre_estudiante"],
                expediente["paterno_estudiante"],
                expediente["materno_estudiante"]
            )

            notas = expediente.get("calificaciones")

            if notas:
                print(
                    f"Notas: I={notas['bimestre1']} | "
                    f"II={notas['bimestre2']} | "
                    f"III={notas['bimestre3']}"
                )
                print("Promedio:", notas["promedio"])
                print("Estado:", notas["estado_academico"])
            else:
                print("Sin calificaciones registradas.")

        print("\n===============================================")

    # MENÚ DE CALIFICACIONES
    if not expedientes:
        print("No hay estudiantes registrados en el sistema.")
        return

    while True:

        print("\n================================================")
        print("       SISTEMA DE REGISTRO DE CALIFICACIONES")
        print("================================================")
        print("1. Registrar calificaciones")
        print("2. Buscar registro por código o DNI")
        print("3. Ordenar por promedio final")
        print("4. Actualizar calificaciones")
        print("5. Listar todos los registros")
        print("6. Volver al menú principal")
        print("================================================")

        try:
            opcion = int(input("Seleccione una opción (1-6): "))
        except ValueError:
            print("ERROR: Ingrese una opción numérica.")
            continue

        if opcion == 1:
            registrar_calificaciones()

        elif opcion == 2:
            buscar_registro()

        elif opcion == 3:
            ordenar_registros()

        elif opcion == 4:
            actualizar_calificaciones()

        elif opcion == 5:
            listar_registros()

        elif opcion == 6:
            print("Regresando al menú principal...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")
