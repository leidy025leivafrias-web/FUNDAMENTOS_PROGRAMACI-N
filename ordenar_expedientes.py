
# Funcion para ordenar expedientes por codigo
def ordenar_expedientes_por_codigo(codigos, apo_pat, apo_mat, apo_nom, apo_dni, apo_telf, est_pat, est_mat, 
                                   est_nom, niveles, asuntos, estados):

    cantidad = len(codigos)

    for i in range(cantidad - 1):
        for j in range(cantidad - 1 - i):

            if codigos[j] > codigos[j + 1]:

                auxiliar = codigos[j]
                codigos[j] = codigos[j + 1]
                codigos[j + 1] = auxiliar

                auxiliar = apo_pat[j]
                apo_pat[j] = apo_pat[j + 1]
                apo_pat[j + 1] = auxiliar

                auxiliar = apo_mat[j]
                apo_mat[j] = apo_mat[j + 1]
                apo_mat[j + 1] = auxiliar

                auxiliar = apo_nom[j]
                apo_nom[j] = apo_nom[j + 1]
                apo_nom[j + 1] = auxiliar

                auxiliar = apo_dni[j]
                apo_dni[j] = apo_dni[j + 1]
                apo_dni[j + 1] = auxiliar

                auxiliar = apo_telf[j]
                apo_telf[j] = apo_telf[j + 1]
                apo_telf[j + 1] = auxiliar

                auxiliar = est_pat[j]
                est_pat[j] = est_pat[j + 1]
                est_pat[j + 1] = auxiliar

                auxiliar = est_mat[j]
                est_mat[j] = est_mat[j + 1]
                est_mat[j + 1] = auxiliar

                auxiliar = est_nom[j]
                est_nom[j] = est_nom[j + 1]
                est_nom[j + 1] = auxiliar

                auxiliar = niveles[j]
                niveles[j] = niveles[j + 1]
                niveles[j + 1] = auxiliar

                auxiliar = asuntos[j]
                asuntos[j] = asuntos[j + 1]
                asuntos[j + 1] = auxiliar

                auxiliar = estados[j]
                estados[j] = estados[j + 1]
                estados[j + 1] = auxiliar

    print("Expedientes ordenados correctamente.")


# Funcion para buscar un expediente por codigo
def buscar_expediente_por_codigo(codigos, apo_pat, apo_mat, apo_nom,
                                 apo_dni, apo_telf, est_pat, est_mat,
                                 est_nom, niveles, asuntos, estados,
                                 codigo_buscar):

    encontrado = False

    for i in range(len(codigos)):
        if codigos[i] == codigo_buscar:

            print("EXPEDIENTE ENCONTRADO")
            print("Codigo:", codigos[i])
            print("Apoderado:", apo_pat[i], apo_mat[i], apo_nom[i])
            print("DNI:", apo_dni[i])
            print("Telefono:", apo_telf[i])
            print("Estudiante:", est_pat[i], est_mat[i], est_nom[i])
            print("Nivel:", niveles[i])
            print("Asunto:", asuntos[i])
            print("Estado:", estados[i])

            encontrado = True

    if encontrado == False:
        print("No se encontro el expediente.")

# Funcion para buscar un expediente por codigo
def buscar_expediente_por_codigo(codigos, apo_pat, apo_mat, apo_nom,
                                 apo_dni, apo_telf, est_pat, est_mat,
                                 est_nom, niveles, asuntos, estados,
                                 codigo_buscar):

    encontrado = False

    for i in range(len(codigos)):

        if codigos[i] == codigo_buscar:

            print("EXPEDIENTE ENCONTRADO")
            print("Codigo:", codigos[i])
            print("Apoderado:", apo_pat[i], apo_mat[i], apo_nom[i])
            print("DNI:", apo_dni[i])
            print("Telefono:", apo_telf[i])
            print("Estudiante:", est_pat[i], est_mat[i], est_nom[i])
            print("Nivel:", niveles[i])
            print("Asunto:", asuntos[i])
            print("Estado:", estados[i])

            encontrado = True

    if encontrado == False:
        print("No se encontro el expediente.")

# Datos de prueba
codigos = ["EXP-1003", "EXP-1001", "EXP-1002"]

apo_pat = ["Perez", "Torres", "Lopez"]
apo_mat = ["Rojas", "Vega", "Diaz"]
apo_nom = ["Carlos", "Ana", "Luis"]
apo_dni = ["12345678", "23456789", "34567890"]
apo_telf = ["987654321", "976543210", "965432109"]

est_pat = ["Perez", "Torres", "Lopez"]
est_mat = ["Rojas", "Vega", "Diaz"]
est_nom = ["Carlos", "Ana", "Luis"]

niveles = ["Primaria", "Secundaria", "Inicial"]
asuntos = ["Constancia", "Certificado", "Matricula"]
estados = ["Pendiente", "Atendido", "En revision"]


# Llamar a la funcion
ordenar_expedientes_por_codigo(
    codigos, apo_pat, apo_mat, apo_nom, apo_dni, apo_telf,
    est_pat, est_mat, est_nom, niveles, asuntos, estados
)


# Mostrar los expedientes ordenados
for i in range(len(codigos)):
    print("------------------------------")
    print("Codigo:", codigos[i])
    print("Apoderado:", apo_pat[i], apo_mat[i], apo_nom[i])
    print("DNI:", apo_dni[i])
    print("Telefono:", apo_telf[i])
    print("Estudiante:", est_pat[i], est_mat[i], est_nom[i])
    print("Nivel:", niveles[i])
    print("Asunto:", asuntos[i])
    print("Estado:", estados[i])



print()
codigo_buscar = input("Ingrese el codigo que desea buscar: ").upper()

buscar_expediente_por_codigo(
    codigos, apo_pat, apo_mat, apo_nom, apo_dni, apo_telf,
    est_pat, est_mat, est_nom, niveles, asuntos, estados,
    codigo_buscar
)

# Buscar un expediente
print()
codigo_buscar = input("Ingrese el codigo que desea buscar: ").upper()

buscar_expediente_por_codigo(
    codigos, apo_pat, apo_mat, apo_nom, apo_dni, apo_telf,
    est_pat, est_mat, est_nom, niveles, asuntos, estados,
    codigo_buscar
)