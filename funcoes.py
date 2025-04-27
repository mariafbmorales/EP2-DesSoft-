import random
def rolar_dados(qnt_dados):
    dados_rolados = []
    for i in range(qnt_dados):
        sorteado = random.randint(1, 6)
        dados_rolados.append(sorteado)
    return dados_rolados

def guardar_dado(lista_rolados, lista_guardados, indice):
    lista_final = []
    nova_lista_rolados = []
    for i in range(len(lista_rolados)):
        if lista_rolados[i] != lista_rolados[indice]:
            nova_lista_rolados.append(lista_rolados[i])
        lista_final.append(nova_lista_rolados)
    lista_guardados.append(lista_rolados[indice])
    lista_final.append(lista_guardados)
    return lista_final

