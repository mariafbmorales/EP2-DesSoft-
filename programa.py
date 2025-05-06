from funcoes import rolar_dados
from funcoes import guardar_dado
from funcoes import remover_dado
from funcoes import calcula_pontos_regra_simples
from funcoes import calcula_pontos_soma 
from funcoes import calcula_pontos_sequencia_baixa
from funcoes import calcula_pontos_sequencia_alta 
from funcoes import calcula_pontos_full_house
from funcoes import calcula_pontos_quadra 
from funcoes import calcula_pontos_quina
from funcoes import calcula_pontos_regra_avancada 
from funcoes import faz_jogada
from funcoes import imprime_cartela

cartela_de_pontuação = {'regra_simples': {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},'regra_avancada': {'sem_combinacao': -1,'quadra': -1,'full_house': -1,'sequencia_baixa': -1,'sequencia_alta': -1,'cinco_iguais':-1}}
imprime_cartela(cartela_de_pontuação)
reg_simp = ["1", "2", "3", "4", "5", "6"]
reg_av = ["sem_combinacao","quadra","full_house","sequencia_baixa","sequencia_alta","cinco_iguais"]

for i in range (12):
    roladas = 0
    dados_rolados = rolar_dados(5)
    dados_guardados = []

    continua = True
    while continua:
        print(f"Dados rolados:{dados_rolados}")
        print(f"Dados guardados:{dados_guardados}")

        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        escolha_jogador = input()
        while escolha_jogador not in ["0", "1", "2", "3", "4"]: