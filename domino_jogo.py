#Biblioteca terá todas as funções para jogar dominó
import domino

#Biblioteca que possui funções para dar delay e limpar a tela
import time, os


#Executando o jogo
def jogar() :
	
	#1)Gerar as peças do dominó
	#Função invocada abaixo retorna um lista de tuplas com todas as peças do dominó
	pecas_domino = domino.gerar_pecas()
	
	#2)Perguntar o usuário se ele deseja jogar e a quantidade de players que vai de 2 ou 4
	
	#Pergunta ao usuario e chama uma trava para checar se ele digitou corretamente
	pergunta = domino.trava1_usuario(str(input("Deseja jogar? Digite S/N: ")))
	
	os.system("cls") #Limpar tela do terminal
	
	#Enquanto a pergunta for sempre sim ou s então o jogo ficará rodando
	while (pergunta.lower() in ["sim", "s"]) :
		
		#Perguntar quantos jogadores jogarão
		#Perguntar como string, pois como o usuário que digita se ele colocar um caracter em vez
		#de um inteiro o programa dará erro
		print("Possiveis jogadores 2 ou 4")
		qnt_jogadores = domino.trava2_usuario(input("Quantidade de jogadores: "))
		os.system("cls")
		
		"""
		#Distribuir as peças de acordo com a quantidade de jogadores
		#Os jogadores ficam dentro de uma lista de listas, onde cada uma dela representa um jogador
		#Dentro dessas lista de listas possui as peças dos n jogadores
		#jogadores_peças tem os jogadores e as peças de cada um deles
		"""
		jogadores_pecas = domino.distribuir_pecas(pecas_domino, qnt_jogadores)
		
		#Criar a "mesa" onde serão colocadas as peças nela
		mesa_domino = domino.criar_mesa()
		
		#Checar a peça inicial do jogo, o qual depende do número de jogadores
		#Bucha de sena inicia
		#Posição do jogador
		jogador_x = domino.check_peca_inicial(jogadores_pecas, qnt_jogadores)
		
		#Atualiza a mesa_domino com a peça inicial o qual não precisa chamar uma função nenhuma pois é a primeira peça
		#Colocando a (6,6) na mesa na posição central da mesa (55//2) que será posição 27
		mesa_domino[len(mesa_domino)//2] = (6,6)
		
		#Depois de colocar a peça na mesa tem que deletar ela de jogadores_pecas
		#Tem que deletar da mão do jogador, pois ele já jogou ela. A peça está na mesa
		jogadores_pecas = domino.atualiza_pecas_jogadores(jogadores_pecas, (jogador_x,(6,6)))
		
		print("Jogador %d esta com a bucha de sena.\n\n" %(jogador_x+1))
		time.sleep(3)
		
		#O jogador que inicia o game é aquele que já jogou a primeira peça
		#O loop só para quando o número de peças do jogador n for igual zero
		#Após isso é necessário saber qual é o próximo jogador o que é chamado uma função
		#num_pecas_jogador começa com -1 só para entrar no loop
		num_pecas_jogadorX = -1
		#Para indicar qual é a posição da peça inicial e final que está na mesa do dominó
		#Inicio fica do lado esquerdo e final do lado direito
		inicio = fim = len(mesa_domino)//2
		
		#Esse contador serve para contar quantos jogadores passaram sequencialmente
		cont_passam = 0
		
		while (num_pecas_jogadorX != 0) and (cont_passam < int(qnt_jogadores)) :
			
			os.system("cls")
			#Função que imprimi a mesa do dominó
			domino.imprimi_mesa_domino(mesa_domino, inicio, fim)
			
			#Função que informa a quantidade de peças que cada jogador possui em suas mãos
			domino.quantidade_pecas_jogadores(jogadores_pecas)
			
			#Função para imprimir a mão do jogador usuário (jogador 1)
			print("Suas pecas (Jogador 1):")
			domino.imprimi_pecas_usuario(jogadores_pecas[0])
			
			#Pega a posição do próximo jogador a jogar
			#Manda como parâmetro somente o jogador
			jogador_x = domino.proximo_jogar(jogador_x, qnt_jogadores)
			print("\n\nProximo jogador: %d" %(jogador_x+1))
			
			#Pega a peça jogada pelo jogador_x da rodada
			#Parâmetro são (jogador atual, peças na mão do jogador atual, valor da peça lado esquerdo, valor da peça lado direito)
			peca_rodada = domino.jogada_peca(jogador_x, jogadores_pecas[jogador_x], mesa_domino[inicio][0], mesa_domino[fim][1])
			print("Peca escolhida: ", peca_rodada)
			
			#Contar quantos jogadores passam sequencialmente, pois se o jogo fechar ele será super importante...
			#para conter loop infinito ou parada do jogo
			cont_passam = domino.x_jogadores_passa(cont_passam, peca_rodada, qnt_jogadores)
				
			#Depois de jogar a peça a mesa tem que ser atualizada
			mesa_domino = domino.atualiza_mesa_domino(mesa_domino, peca_rodada, inicio, fim, jogador_x)	
				
			#Depois atualiza o inicio e fim da mesa
			atualizar_inicio_fim = domino.atualiza_inicio_fim(mesa_domino, inicio, fim)
			inicio = atualizar_inicio_fim[0]
			fim = atualizar_inicio_fim[1]
			
			#Atualizar a mão do jogador
			jogadores_pecas = domino.atualiza_pecas_jogadores(jogadores_pecas, (jogador_x, peca_rodada))
			
			#Armazena o número de peças que o jogador atual que fez a jogada tem
			#Se esse número armazenado é zero então o jogador atual ganhou
			num_pecas_jogadorX = len(jogadores_pecas[jogador_x])
			
			input("\nPressione qualquer tecla para continuar...")
		
		
		#Função que imprimi a mesa do dominó
		os.system("cls")
		domino.imprimi_mesa_domino(mesa_domino, inicio, fim)
		
		#Função que checa quem ou quais jogador(es) ganhou(ram) a partida
		#Pode ser por batida (1 vencedor) ou por pontos (pelo menos 1 vencedor)
		domino.vencedor_partida(jogador_x, num_pecas_jogadorX, jogadores_pecas)
		os.system("cls")
			
		
		#Pergunta ao usuario e chama uma trava para checar se ele digitou corretamente
		pergunta = domino.trava1_usuario((input("Deseja jogar novamente? Digite S/N: ")))
		

def main():
	
	jogar()
	
	return 0

if __name__ == '__main__':
	main()

