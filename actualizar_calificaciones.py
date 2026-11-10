#actualizar_calificaciones.py

import datos
from calcular_promedio import calcular_promedio
from leer_nota_valida import leer_nota_valida

def actualizar_calificaciones():
    if datos.total_registros == 0:
        print("No hay registros en el sistema.")
        return

    codigo = input("Ingrese el código de expediente (Ej. EXP-1001): ").strip().upper()
    encontrado = False

    for i in range(datos.total_registros):
        if datos.codigos_exp[i].upper() == codigo:
            encontrado = True
            print(f"Estudiante: {datos.apellidos[i]}, {datos.nombres[i]}")
            print(
                f"Notas actuales: I={datos.bimestre1[i]:.2f}, "
                f"II={datos.bimestre2[i]:.2f}, "
                f"III={datos.bimestre3[i]:.2f}"
            )
            
            print("\nIngrese las nuevas calificaciones:")
            datos.bimestre1[i] = leer_nota_valida("Nuevo I Bimestre: ")
            datos.bimestre2[i] = leer_nota_valida("Nuevo II Bimestre: ")
            datos.bimestre3[i] = leer_nota_valida("Nuevo III Bimestre: ")
            
            calcular_promedio(i)
            
            print(
                f"Actualización exitosa. Promedio final: "
                f"{datos.promedios_finales[i]:.2f} | Estado: {datos.estados[i]}"
            )
            return

    if not encontrado:
         print(f"Error: No existe un expediente con el código {codigo}.")