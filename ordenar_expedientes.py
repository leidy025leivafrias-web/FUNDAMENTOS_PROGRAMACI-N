
# Funcion para ordenar expedientes por codigo
def ordenar_expedientes_por_codigo(codigos, apo_pat, apo_mat, apo_nom,
                                   apo_dni, apo_telf, est_pat, est_mat,
                                   est_nom, niveles, asuntos, estados):

    cantidad = len(codigos)

    for a in range(cantidad - 1):
        for m in range(cantidad - 1 - a):

            if codigos[m] > codigos[m + 1]:

                auxiliar = codigos[m]
                codigos[m] = codigos[m + 1]
                codigos[m + 1] = auxiliar

                auxiliar = apo_pat[m]
                apo_pat[m] = apo_pat[m + 1]
                apo_pat[m + 1] = auxiliar

                auxiliar = apo_mat[m]
                apo_mat[m] = apo_mat[m + 1]
                apo_mat[m + 1] = auxiliar

                auxiliar = apo_nom[m]
                apo_nom[m] = apo_nom[m + 1]
                apo_nom[m + 1] = auxiliar

                auxiliar = apo_dni[m]
                apo_dni[m] = apo_dni[m + 1]
                apo_dni[m + 1] = auxiliar

                auxiliar = apo_telf[m]
                apo_telf[m] = apo_telf[m + 1]
                apo_telf[m + 1] = auxiliar

                auxiliar = est_pat[m]
                est_pat[m] = est_pat[m + 1]
                est_pat[m + 1] = auxiliar

                auxiliar = est_mat[m]
                est_mat[m] = est_mat[m + 1]
                est_mat[m + 1] = auxiliar

                auxiliar = est_nom[m]
                est_nom[m] = est_nom[m + 1]
                est_nom[m + 1] = auxiliar

                auxiliar = niveles[m]
                niveles[m] = niveles[m + 1]
                niveles[m + 1] = auxiliar

                auxiliar = asuntos[m]
                asuntos[m] = asuntos[m + 1]
                asuntos[m + 1] = auxiliar

                auxiliar = estados[m]
                estados[m] = estados[m + 1]
                estados[m + 1] = auxiliar

    print("Expedientes ordenados correctamente.")


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
for a in range(len(codigos)):
    print("------------------------------")
    print("Codigo:", codigos[a])
    print("Apoderado:", apo_pat[a], apo_mat[a], apo_nom[a])
    print("DNI:", apo_dni[a])
    print("Telefono:", apo_telf[a])
    print("Estudiante:", est_pat[a], est_mat[a], est_nom[a])
    print("Nivel:", niveles[a])
    print("Asunto:", asuntos[a])
    print("Estado:", estados[a])
