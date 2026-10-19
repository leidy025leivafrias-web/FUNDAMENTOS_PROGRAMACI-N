#FUNCIÓN 5: lista de expedientes.
def listado_expedientes(codigos, estudiantes_pat, estudiantes_mat, estados, total):
      if total == 0:
          print("No hay expedientes para mostrar.")
          return
      print("LISTADO GENERAL DE EXPEDIENTES")
      
      for i in range(total):
            print(f"{i + 1}. [{codigos[i]}] Estudiante: {estudiantes_pat[i]} {estudiantes_mat[i]} | Estado: {estados[i]}")