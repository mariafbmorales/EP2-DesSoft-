import random
def rolar_dados(qnt_dados):
    dados_rolados = []
    for i in range(qnt_dados):
        sorteado = random.randint(1, 6)
        dados_rolados.append(sorteado)
    return dados_rolados

def guardar_dado(lista_rolados, lista_guardados, indice):
    lista_guardados.append(lista_rolados[indice])
    nova_lista_rolados = []
    for i in range(len(lista_rolados)):
        if i != indice:
            nova_lista_rolados.append(lista_rolados[i])
    return [nova_lista_rolados, lista_guardados]

def remover_dado(dados_rolados, dados_estoque, indice):
    dados_rolados.append(dados_estoque[indice])
    nova_lista_estoque = []
    for i in range(len(dados_estoque)):
        if i != indice:
            nova_lista_estoque.append(dados_estoque[i])
    return [dados_rolados, nova_lista_estoque]

def calcula_pontos_regra_simples(numeros_inteiros):
    dicio = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for num in numeros_inteiros:
        if num in dicio:
            dicio[num] += num
    return dicio

def calcula_pontos_soma(numeros):
    soma = 0
    for i in range(len(numeros)):
        soma += numeros[i]
    return soma

def calcula_pontos_sequencia_baixa(numero):
    sequencia = []
    for i in range(len(numero)):
        if numero[i] not in sequencia:
            sequencia.append(numero[i])
        soma = 0
        for num in sequencia:
            soma += num
        if soma == 10 or soma == 14 or soma == 18:
            return 15
        else:
            return 0
