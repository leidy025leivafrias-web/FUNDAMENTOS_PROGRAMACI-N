# ============================================================
# SISTEMA DE REGISTRO DE CALIFICACIONES - ADAPTADO DE PROYECTO ESCOLAR
# ============================================================

MAX = 100

# Declaración de arreglos paralelos para almacenar los datos
codigos = [""] * MAX
dnis = [""] * MAX
apellidos = [""] * MAX
nombres = [""] * MAX
nota1 = [0.0] * MAX
nota2 = [0.0] * MAX
nota3 = [0.0] * MAX
promedios = [0.0] * MAX
estados = [""] * MAX

total_estudiantes = 0


# 1. Valida que un texto contenga exclusivamente números
def validar_solo_numeros(texto):
  if len(texto) == 0:
    return False
  for char in texto:
    if not char.isdigit():
      return False
  return True


# 2. Solicita y valida el DNI (exactamente 8 dígitos numéricos)
def leer_dni_valido(mensaje):
  while True:
    dni = input(mensaje)
    if len(dni) == 8 and validar_solo_numeros(dni):
      return dni
    print("Error: El DNI debe tener exactamente 8 dígitos numéricos.")


# 3. Valida que el texto contenga solo letras y espacios
def validar_solo_letras(texto):
  if len(texto) == 0:
    return False
  permitidos = "abcdefghijklmnñopqrstuvwxyzáéíóúÁÉÍÓÚ "
  for char in texto:
    if char.lower() not in permitidos:
      return False
  return True


# 4. Solicita texto y repite hasta ingresar solo letras válidas
def leer_texto_valido(mensaje):
  while True:
    texto = input(mensaje)
    if validar_solo_letras(texto):
      return texto
    print(
        "Error: Este campo solo debe contener letras (sin números ni símbolos)."
    )


# 5. Valida que la nota esté en la escala permitida (0 a 20)
def leer_nota_valida(mensaje):
  while True:
    try:
      nota = float(input(mensaje))
      if 0.0 <= nota <= 20.0:
        return nota
      print("Error: La calificación debe estar en el rango de 0.0 a 20.0.")
    except ValueError:
      print("Error: Ingrese un valor numérico válido.")


# 6. Subproceso de Persistencia: Guardar registros en un archivo CSV
def guardar_en_archivo(total):
  with open("registro_calificaciones.csv", "w", encoding="utf-8") as archivo:
    archivo.write(
        "Codigo,DNI,Apellidos,Nombres,Nota1,Nota2,Nota3,Promedio,Estado\n"
    )
    for i in range(total):
      linea = (
          f"{codigos[i]},{dnis[i]},{apellidos[i]},{nombres[i]},"
          f"{nota1[i]},{nota2[i]},{nota3[i]},{promedios[i]},{estados[i]}\n"
      )
      archivo.write(linea)
  print(
      "Datos respaldados correctamente en el archivo 'registro_calificaciones.csv'."
  )


# ============================================================
# ALGORITMO PRINCIPAL
# ============================================================
def main():
  global total_estudiantes
  opcion = 0

  while opcion != 6:
    print("\n============================================================")
    print("      SISTEMA DE REGISTRO DE CALIFICACIONES ESCOLARES       ")
    print("============================================================")
    print("1. Registrar Nuevo Estudiante y Calificaciones")
    print("2. Buscar Estudiante por Código o DNI")
    print("3. Ordenar Estudiantes por Promedio (Mayor a Menor)")
    print("4. Actualizar Calificaciones")
    print("5. Listar Todos los Estudiantes")
    print("6. Guardar y Salir")

    try:
      opcion = int(input("Seleccione una opción: "))
    except ValueError:
      print("Opción no válida. Ingrese un número del 1 al 6.")
      continue

    if opcion == 1:
      if total_estudiantes < MAX:
        total_estudiantes += 1
        print("\n--- PASO 1: DATOS DE IDENTIFICACIÓN ---")
        dnis[total_estudiantes - 1] = leer_dni_valido(
            "DNI del Estudiante (exactamente 8 dígitos): "
        )
        apellidos[total_estudiantes - 1] = leer_texto_valido(
            "Apellidos del Estudiante: "
        )
        nombres[total_estudiantes - 1] = leer_texto_valido(
            "Nombres del Estudiante: "
        )

        print("\n--- PASO 2: REGISTRO DE CALIFICACIONES (0 - 20) ---")
        nota1[total_estudiantes - 1] = leer_nota_valida(
            "Ingrese Nota de Evaluacion 1: "
        )
        nota2[total_estudiantes - 1] = leer_nota_valida(
            "Ingrese Nota de Evaluacion 2: "
        )
        nota3[total_estudiantes - 1] = leer_nota_valida(
            "Ingrese Nota de Evaluacion 3: "
        )

        # Cálculo automático del promedio
        suma = (
            nota1[total_estudiantes - 1]
            + nota2[total_estudiantes - 1]
            + nota3[total_estudiantes - 1]
        )
        promedios[total_estudiantes - 1] = round(suma / 3.0, 2)

        # Determinación automática del estado (Nota mínima aprobatoria: 11.0)
        if promedios[total_estudiantes - 1] >= 11.0:
          estados[total_estudiantes - 1] = "APROBADO"
        else:
          estados[total_estudiantes - 1] = "DESAPROBADO"

        # Generación automática del código correlativo
        codigos[total_estudiantes - 1] = f"EST-{1000 + total_estudiantes}"

        print(
            f"\n¡Estudiante registrado con éxito! Código asignado:"
            f" {codigos[total_estudiantes - 1]}"
        )
      else:
        print("Capacidad máxima de estudiantes alcanzada.")

    elif opcion == 2:
      if total_estudiantes > 0:
        print("\n--- BÚSQUEDA DE ESTUDIANTE ---")
        busqueda = input("Ingrese el Código o DNI del Estudiante: ")
        encontrado = False

        for i in range(total_estudiantes):
          if codigos[i] == busqueda or dnis[i] == busqueda:
            print("\n----------------------------------------")
            print("REGISTRO ENCONTRADO:")
            print(f"Código: {codigos[i]}")
            print(f"DNI: {dnis[i]}")
            print(f"Estudiante: {apellidos[i]}, {nombres[i]}")
            print(
                f"Calificaciones: [{nota1[i]} | {nota2[i]} | {nota3[i]}]"
            )
            print(f"Promedio Final: {promedios[i]}")
            print(f"Estado: {estados[i]}")
            print("----------------------------------------")
            encontrado = True

        if not encontrado:
          print(f"No se encontró ningún registro con: {busqueda}")
      else:
        print("No hay estudiantes registrados en el sistema.")

    elif opcion == 3:
      if total_estudiantes > 1:
        # Método burbuja sincronizando arreglos paralelos para ordenar promedios
        for i in range(total_estudiantes - 1):
          for j in range(total_estudiantes - 1 - i):
            if promedios[j] < promedios[j + 1]:  # Orden descendente
              (
                  codigos[j],
                  codigos[j + 1],
              ) = (codigos[j + 1], codigos[j])
              (
                  dnis[j],
                  dnis[j + 1],
              ) = (dnis[j + 1], dnis[j])
              (
                  apellidos[j],
                  apellidos[j + 1],
              ) = (apellidos[j + 1], apellidos[j])
              (
                  nombres[j],
                  nombres[j + 1],
              ) = (nombres[j + 1], nombres[j])
              (
                  nota1[j],
                  nota1[j + 1],
              ) = (nota1[j + 1], nota1[j])
              (
                  nota2[j],
                  nota2[j + 1],
              ) = (nota2[j + 1], nota2[j])
              (
                  nota3[j],
                  nota3[j + 1],
              ) = (nota3[j + 1], nota3[j])
              (
                  promedios[j],
                  promedios[j + 1],
              ) = (promedios[j + 1], promedios[j])
              (
                  estados[j],
                  estados[j + 1],
              ) = (estados[j + 1], estados[j])

        print(
            "¡Estudiantes ordenados correctamente por promedio de mayor a"
            " menor!"
        )
      else:
        print("Se requieren al menos 2 estudiantes para ordenar.")

    elif opcion == 4:
      if total_estudiantes > 0:
        print("\n--- ACTUALIZAR CALIFICACIONES ---")
        codigo_buscar = input("Ingrese el Código del Estudiante (Ej. EST-1001): ")
        encontrado = False

        for i in range(total_estudiantes):
          if codigos[i] == codigo_buscar:
            encontrado = True
            print(f"Estudiante: {apellidos[i]}, {nombres[i]}")
            print(
                f"Notas actuales: [{nota1[i]}, {nota2[i]}, {nota3[i]}]"
            )

            print("Ingrese las nuevas notas:")
            nota1[i] = leer_nota_valida("Nueva Nota 1: ")
            nota2[i] = leer_nota_valida("Nueva Nota 2: ")
            nota3[i] = leer_nota_valida("Nueva Nota 3: ")

            suma = nota1[i] + nota2[i] + nota3[i]
            promedios[i] = round(suma / 3.0, 2)

            if promedios[i] >= 11.0:
              estados[i] = "APROBADO"
            else:
              estados[i] = "DESAPROBADO"

            print(
                f"¡Actualización exitosa! Nuevo promedio: {promedios[i]} |"
                f" Estado: {estados[i]}"
            )

        if not encontrado:
          print(f"Error: El estudiante con código {codigo_buscar} no existe.")
      else:
        print("No hay estudiantes registrados en el sistema.")

    elif opcion == 5:
      if total_estudiantes > 0:
        print(
            "\n================ LISTADO GENERAL DE CALIFICACIONES"
            " ================"
        )
        for i in range(total_estudiantes):
          print(
              f"{i+1}. [{codigos[i]}] DNI: {dnis[i]} | Estudiante:"
              f" {apellidos[i]}, {nombres[i]} | Promedio: {promedios[i]} |"
              f" Estado: {estados[i]}"
          )
        print("============================================================")
      else:
        print("No hay estudiantes para mostrar.")

    elif opcion == 6:
      if total_estudiantes > 0:
        guardar_en_archivo(total_estudiantes)
      print("Saliendo del sistema de calificaciones. ¡Hasta luego!")

    else:
      print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
  main()