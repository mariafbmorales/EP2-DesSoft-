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
    for i in range(1,4):
        if i in sequencia and i+1 in sequencia and i+2 in sequencia and i+3 in sequencia:
            return 15
    return 0

def calcula_pontos_sequencia_alta(numero):
    sequencia = []
    for i in range(len(numero)):
        if numero[i] not in sequencia:
            sequencia.append(numero[i])
    for i in range(1,5):
        if i in sequencia and i+1 in sequencia and i+2 in sequencia and i+3 in sequencia and i+4 in sequencia:
            return 30
    return 0

def calcula_pontos_full_house(numeros):
    repeticoes = {}
    for i in range(len(numeros)):
        if numeros[i] in repeticoes:
            repeticoes[numeros[i]] += 1
        if numeros[i] not in repeticoes:
            repeticoes[numeros[i]] = 1

    dupla = 0
    trio = 0
    for valor in repeticoes.values():
        if valor == 3:
            trio += 1
        if valor == 2:
            dupla += 1
    
    if dupla == 1 and trio == 1:
        soma = 0
        for i in range(len(numeros)):
            soma += numeros[i]
        return soma
    return 0

def calcula_pontos_quadra(numeros):
    repeticoes = {}
    for i in range(len(numeros)):
        if numeros[i] in repeticoes:
            repeticoes[numeros[i]] += 1
        if numeros[i] not in repeticoes:
            repeticoes[numeros[i]] = 1

    quarteto = 0
    for valor in repeticoes.values():
        if valor >= 4:
            quarteto += 1
    
    if quarteto >= 1:
        soma = 0
        for i in range(len(numeros)):
            soma += numeros[i]
        return soma
    return 0

def calcula_pontos_quina(numeros):
    repeticoes = {}
    for i in range(len(numeros)):
        if numeros[i] in repeticoes:
            repeticoes[numeros[i]] += 1
        if numeros[i] not in repeticoes:
            repeticoes[numeros[i]] = 1

    quinteto = 0
    for valor in repeticoes.values():
        if valor >= 5:
            quinteto += 1
    
    if quinteto >= 1:
        return 50
    return 0