
# VALIDAR TRÁMITE A REALIZAR
while True:
    tramite = input("Ingrese el trámite que desea realizar: ")

    # Validar que no esté vacío ni contenga solo espacios
    if not tramite.strip():
        print("ERROR: No puede dejar el trámite en blanco.")
    
    # Validar que solo contenga letras y espacios
    elif not tramite.replace(" ", "").isalpha():
        print("ERROR: El trámite solo debe contener letras y espacios.")
    
    else:
        print("Trámite registrado correctamente.\n")
        break

# MOSTRAR RESULTADO FINAL
print("=" * 30)
print(f"TRÁMITE SELECCIONADO: {tramite}")
print("=" * 30)
