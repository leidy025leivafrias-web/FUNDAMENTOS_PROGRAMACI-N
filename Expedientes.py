# ============================================================
# SISTEMA DE REGISTRO DE CALIFICACIONES ESCOLARES
# ============================================================
import csv
def Expedientes(expedientes):
    MAX = 100
    ARCHIVO_CSV = "registro_calificaciones.csv"

    # Listas paralelas para los registros de estudiantes
    codigos_exp = [""] * MAX
    dnis = [""] * MAX
    apellidos = [""] * MAX
    nombres = [""] * MAX
    bimestre1 = [0.0] * MAX
    bimestre2 = [0.0] * MAX
    bimestre3 = [0.0] * MAX
    promedios_finales = [0.0] * MAX
    estados = [""] * MAX
    
    total_registros = 0
    for expediente in expedientes:
        if total_registros >= MAX:
            print("Se alcanzó el máximo de 100 estudiantes.")
            break

        i = total_registros

        codigos_exp[i] = expediente["codigo"]
        dnis[i] = expediente["dni_estudiante"]

        apellidos[i] = (
            expediente["paterno_estudiante"] + " " +
            expediente["materno_estudiante"]
        )

        nombres[i] = expediente["nombre_estudiante"]

        if "calificaciones" in expediente:
            notas = expediente["calificaciones"]

            bimestre1[i] = notas["bimestre1"]
            bimestre2[i] = notas["bimestre2"]
            bimestre3[i] = notas["bimestre3"]
            promedios_finales[i] = notas["promedio"]
            estados[i] = notas["estado_academico"]

        total_registros += 1

    def validar_solo_numeros(texto):
        """Comprueba que el texto contenga únicamente dígitos."""
        return bool(texto) and texto.isdigit()


    def validar_solo_letras(texto):
        """Permite letras, tildes, ñ, ü y espacios."""
        texto = texto.strip()
        if not texto:
            return False

        permitidos = "abcdefghijklmnñopqrstuvwxyzáéíóúü "
        return all(caracter.lower() in permitidos for caracter in texto)


    def leer_texto_valido(mensaje):
        while True:
            texto = input(mensaje).strip()
            if validar_solo_letras(texto):
                return texto
            print("Error: Ingrese solo letras y espacios, sin números ni símbolos.")


    def leer_nota_valida(mensaje):
        """Solicita una nota numérica entre 0 y 20."""
        while True:
            try:
                entrada = input(mensaje).strip().replace(",", ".")
                nota = float(entrada)

                if 0.0 <= nota <= 20.0:
                    return nota

                print("Error: La calificación debe estar entre 0 y 20.")
            except ValueError:
                print("Error: Ingrese un valor numérico válido.")


    def calcular_promedio(indice):
        promedios_finales[indice] = round(
            (
                bimestre1[indice]
                + bimestre2[indice]
                + bimestre3[indice]
            ) / 3.0,
            2,
        )
        estados[indice] = (
            "APROBADO"
            if promedios_finales[indice] >= 11.0
            else "DESAPROBADO"
        )


    def guardar_en_archivo(total):
        """Guarda los registros actuales en un archivo CSV."""
        encabezados = [
            "CodigoExpediente",
            "DNI",
            "Apellidos",
            "Nombres",
            "I_Bimestre",
            "II_Bimestre",
            "III_Bimestre",
            "PromedioFinal",
            "Estado",
        ]

        try:
            with open(
                ARCHIVO_CSV, "w", newline="", encoding="utf-8"
            ) as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(encabezados)

                for i in range(total):
                    escritor.writerow([
                        codigos_exp[i],
                        dnis[i],
                        apellidos[i],
                        nombres[i],
                        bimestre1[i],
                        bimestre2[i],
                        bimestre3[i],
                        promedios_finales[i],
                        estados[i],
                    ])

            print(f"\n[Éxito] Registros guardados en '{ARCHIVO_CSV}'.")
        except OSError as error:
            print(f"Error al guardar el archivo: {error}")


    def buscar_registro():
        if total_registros == 0:
            print("No hay registros en el sistema.")
            return

        busqueda = input(
            "Ingrese el código de expediente (EXP-1001) o el DNI: "
        ).strip().upper()

        encontrado = False

        for i in range(total_registros):
            if (
                codigos_exp[i].upper() == busqueda
                or dnis[i] == busqueda
            ):
                mostrar_registro(i)
                encontrado = True

        if not encontrado:
            print(f"No se encontró ningún registro con: {busqueda}")


    def mostrar_registro(indice):
        print("\n----------------------------------------")
        print("REGISTRO ENCONTRADO")
        print(f"Código de expediente: {codigos_exp[indice]}")
        print(f"DNI: {dnis[indice]}")
        print(f"Apellidos y nombres: {apellidos[indice]}, {nombres[indice]}")
        print(f"I Bimestre: {bimestre1[indice]:.2f}")
        print(f"II Bimestre: {bimestre2[indice]:.2f}")
        print(f"III Bimestre: {bimestre3[indice]:.2f}")
        print(f"Promedio final: {promedios_finales[indice]:.2f}")
        print(f"Estado académico: {estados[indice]}")
        print("----------------------------------------")


    def ordenar_registros():
        if total_registros < 2:
            print("Se requieren al menos 2 registros para ordenar.")
            return

        # Método burbuja: se mueven juntos todos los datos de cada estudiante.
        listas = [
            codigos_exp,
            dnis,
            apellidos,
            nombres,
            bimestre1,
            bimestre2,
            bimestre3,
            promedios_finales,
            estados,
        ]

        for i in range(total_registros - 1):
            for j in range(total_registros - 1 - i):
                if promedios_finales[j] < promedios_finales[j + 1]:
                    for lista in listas:
                        lista[j], lista[j + 1] = lista[j + 1], lista[j]

        print("Registros ordenados por promedio, de mayor a menor.")


    def actualizar_calificaciones():
        if total_registros == 0:
            print("No hay registros en el sistema.")
            return

        codigo = input(
            "Ingrese el código de expediente (Ej. EXP-1001): "
        ).strip().upper()

        for i in range(total_registros):
            if codigos_exp[i].upper() == codigo:
                print(f"Estudiante: {apellidos[i]}, {nombres[i]}")
                print(
                    f"Notas actuales: I={bimestre1[i]:.2f}, "
                    f"II={bimestre2[i]:.2f}, "
                    f"III={bimestre3[i]:.2f}"
                )

                print("\nIngrese las nuevas calificaciones:")
                bimestre1[i] = leer_nota_valida("Nuevo I Bimestre: ")
                bimestre2[i] = leer_nota_valida("Nuevo II Bimestre: ")
                bimestre3[i] = leer_nota_valida("Nuevo III Bimestre: ")

                calcular_promedio(i)
                for expediente in expedientes:
                    if expediente["codigo"] == codigos_exp[i]:
                        expediente["calificaciones"] = {
                            "bimestre1": bimestre1[i],
                            "bimestre2": bimestre2[i],
                            "bimestre3": bimestre3[i],
                            "promedio": promedios_finales[i],
                            "estado_academico": estados[i]
                            }
                        break 

                print(
                    f"Actualización exitosa. Promedio final: "
                    f"{promedios_finales[i]:.2f} | Estado: {estados[i]}"
                )
                return

        print(f"Error: No existe un expediente con el código {codigo}.")


    def listar_registros():
        if total_registros == 0:
            print("No hay registros para mostrar.")
            return

        print("\n================ LISTADO GENERAL DE CALIFICACIONES ================")

        for i in range(total_registros):
            print(
                f"{i + 1}. [{codigos_exp[i]}] DNI: {dnis[i]} | "
                f"{apellidos[i]}, {nombres[i]} | "
                f"Notas [I: {bimestre1[i]:.2f}, "
                f"II: {bimestre2[i]:.2f}, "
                f"III: {bimestre3[i]:.2f}] | "
                f"Promedio: {promedios_finales[i]:.2f} | "
                f"Estado: {estados[i]}"
            )

        print("==================================================================")

    def registrar_calificaciones():
        if total_registros == 0:
            print("No hay estudiantes registrados.")
            return

        print("\n===== REGISTRAR CALIFICACIONES =====")

        codigo = input(
            "Ingrese el código del expediente: "
        ).strip().upper()

        for i in range(total_registros):
            if codigos_exp[i].upper() == codigo:

                print("\nEstudiante encontrado:")
                print("DNI:", dnis[i])
                print("Apellidos:", apellidos[i])
                print("Nombres:", nombres[i])

                # Comprobar si ya tiene calificaciones
                if "calificaciones" in expedientes[i]:
                    print("El estudiante ya tiene calificaciones.")
                    print("Use la opción Actualizar calificaciones.")
                    return

                bimestre1[i] = leer_nota_valida(
                    "Ingrese nota del I Bimestre: "
                )
                bimestre2[i] = leer_nota_valida(
                    "Ingrese nota del II Bimestre: "
                )
                bimestre3[i] = leer_nota_valida(
                    "Ingrese nota del III Bimestre: "
                )

                calcular_promedio(i)

                # Guardar también en el expediente original
                expedientes[i]["calificaciones"] = {
                    "bimestre1": bimestre1[i],
                    "bimestre2": bimestre2[i],
                    "bimestre3": bimestre3[i],
                    "promedio": promedios_finales[i],
                    "estado_academico": estados[i]
                }

                print("\n¡Calificaciones registradas correctamente!")
                print("Promedio final:", promedios_finales[i])
                print("Estado académico:", estados[i])
                return

        print("No existe un estudiante con ese código.")

    def main():
        # No se incluye la opción de registrar nuevos estudiantes.
        # Los registros deben cargarse desde un archivo o añadirse por otro medio.

        opcion = 0

        while opcion != 6:
            print("\n============================================================")
            print("          SISTEMA DE REGISTRO DE CALIFICACIONES")
            print("============================================================")
            print("1. Registrar calificaciones")
            print("2. Buscar registro por código o DNI")
            print("3. Ordenar registros por promedio final (mayor a menor)")
            print("4. Actualizar calificaciones de los bimestres")
            print("5. Listar todos los registros")
            print("6. Guardar y volver al menú principal")

            try:
                opcion = int(input("\nSeleccione una opción (1-6): "))
            except ValueError:
                print("Opción no válida. Ingrese un número del 1 al 6.")
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
                print("Para guardar todos los datos, selecciona la opción 7.")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
    main()
if __name__ == "__main__":
    Expedientes()
