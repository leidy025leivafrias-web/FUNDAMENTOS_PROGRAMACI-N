# VALIDAR TRÁMITE A REALIZAR
while True:
    tramite = input("Ingrese el trámite que desea realizar: ")
    
    # Reemplazamos los espacios para verificar si todo lo demás son letras
    if not tramite.replace(" ", "").isalpha():
        print("ERROR: El trámite solo debe contener letras y espacios.")
    else:
        print("Trámite registrado correctamente.\n")
        break

# MOSTRAR RESULTADO FINAL
print("=" * 30)
print(f"TRÁMITE SELECCIONADO: {tramite}")
print("=" * 30)