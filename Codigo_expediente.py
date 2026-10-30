def Codigo_expediente(expedientes):
    numero = len(expedientes) + 1
    while True:
       codigo = f"EXP{numero:03d}"
       existe = False
       
       for expediente in expedientes:
          if expediente["codigo"] == codigo:
              existe = True
              break
        
       if existe:
           numero += 1
       else:
           return codigo
if __name__ == "__main__":
    expedientes = []
    codigo = Codigo_expediente(expedientes)
    print("Código generado:", codigo)       
       