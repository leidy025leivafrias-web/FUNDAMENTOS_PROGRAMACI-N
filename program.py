#ESTRUCTURA DE EXPEDIENTES
def estructura_expedientes(Codigo, Estudiante, Apoderado, Nivel, Estado, Calificaciones):
        return{
               "Codigo": Codigo,
               "Estudiante": Estudiante,
               "Apoderado": Apoderado,
               "Nivel": Nivel,
               "Estado": Estado,
               "Calificaciones": Calificaciones
        }
   
#LISTA DE EXPEDIENTES
def lista_expedientes(expedientes):
        if len(expedientes) == 0:
           print("ERROR: Expediente no encontrado")
           return
        for expediente in expedientes:
              print(expediente)

 