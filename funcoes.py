import random
def rolar_dados(qnt_dados):
    dados_rolados = []
    for i in range(qnt_dados):
        sorteado = random.radint(1, 6)
        dados_rolados.append(sorteado)
    return dados_rolados