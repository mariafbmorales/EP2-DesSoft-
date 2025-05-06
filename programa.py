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
    