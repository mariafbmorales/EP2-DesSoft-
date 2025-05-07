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
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    roladas = 0

    continua = True
    while continua:
        print(f"Dados rolados:{dados_rolados}")
        print(f"Dados guardados:{dados_guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        escolha_jogador = input()

        while escolha_jogador not in ["0", "1", "2", "3", "4"]:
            print("Opção inválida. Tente novamente.")
            escolha_jogador = input()
        
        else:
            if escolha_jogador == "1":
                print("Digite o índice do dado a ser guardado (0 a 4):")
                guardado = int(input())
                lista_guardados = guardar_dado(dados_rolados, dados_guardados, guardado)
                dados_rolados = lista_guardados[0]
                dados_guardados = lista_guardados[1]

            elif escolha_jogador == "2":
                print("Digite o índice do dado a ser removido (0 a 4):")
                removido = int(input())
                lista_removidos = remover_dado(dados_rolados, dados_guardados, removido)
                dados_rolados = lista_removidos[0]
                dados_guardados = lista_removidos[1]

            elif escolha_jogador == "3":
                if roladas >=2 :
                    print("Você já usou todas as rerrolagens.")
                else:
                    dados_rolados = rolar_dados(len(dados_rolados))
                    roladas += 1

            elif escolha_jogador == "4":
                imprime_cartela(cartela_de_pontuação)
            
            elif escolha_jogador == "0":
                total = dados_rolados + dados_guardados
                validacao = False
                print ("Digite a combinação desejada:")

                while not validacao:
                    escolha = input()

                    if escolha in reg_simp:
                        n = int(escolha)
                        if cartela_de_pontuação['regra_simples'][n] == -1:
                            cartela_de_pontuação = faz_jogada(total, n, cartela_de_pontuação)
                            validacao = True
                        else:
                            print("Essa combinação já foi utilizada.")

                    elif escolha in reg_av:
                        if cartela_de_pontuação['regra_avancada'][escolha] == -1:
                            cartela_de_pontuação = faz_jogada(total, escolha, cartela_de_pontuação)
                            validacao = True
                        else:
                            print("Essa combinação já foi utilizada.")
                    else:
                        print("Opção inválida. Tente novamente.")

                continua = False
    
n = int(escolha)
total_primeiro = 0
for n in cartela_de_pontuação['regra_simples']:
    valor = cartela_de_pontuação['regra_simples'][n]
    if valor != -1:
        total_primeiro += valor
bonus = 0
if total_primeiro >= 63:
    bonus += 35

total_segundo = 0
for escolha in cartela_de_pontuação['regra_avancada']:
    valor = cartela_de_pontuação['regra_avancada'][escolha]
    if valor != -1:
        total_segundo += valor

total_pontos = total_primeiro + total_segundo + bonus

imprime_cartela(cartela_de_pontuação)
print(f"Pontuação total: {total_pontos}")