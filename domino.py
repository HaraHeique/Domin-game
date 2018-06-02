#BIBLIOTECA QUE POSSUI AS FUNÇÕES DO DOMINÓ

import random  #Biblioteca de funções randômicas(aleatórias)
import os      

#Inicio
#Funcao que gera as 28 pecas de domino
def gerar_pecas() :
	
	pecas_domino = [] #Lista que serve para armazenar todas as pecas do domino
	inicio_peca = -1  #Variavel que serve indicar o inicio das pecas do lado2 de uma peca de domino
	
	#lado1 e lado2 serao os valores que as pecas armazenará
	
	#Loop para gerar os valores do lado1 das peças do dominó
	for lado1 in range(7) :
		inicio_peca += 1
		
		#Loop para gerar os valores do lado2 das peças do dominó
		for lado2 in range(inicio_peca, 7, 1) :
			
			#Adicionando a peca criada para dentro da lista pecas_domino
			#Usando uma lista de tuplas para armazenar as pecas geradas
			pecas_domino.append((lado1,lado2)) 
	
	#Retorna as peças geradas
	return pecas_domino
#Fim


#Inicio
#Função para gerar uma trava ao usuário quando pergunta se deseja jogar ou não
def trava1_usuario(resposta_user) :
	
	#resposta_user.lower() fará com que toda string fique minuscula
	#Se a resposta não estiver em nenhuma das strings da lista é porque o usuário digitou errado
	while (resposta_user.lower() not in ["sim", "nao", "s", "n"]) :
		
		#Faz a pergunta para o usuário novamente
		resposta_user = input("Digitou errado. Insira novamente: ")
	
	#Se saiu do loop o usuário digitou certo então retorna o que ele respondeu
	return resposta_user
#Fim


#Inicio
#Função para gerar um trava quanto ao número de jogadores que o usuário digitar
def trava2_usuario(resposta_user) :
	
	#Se a resposta não estiver em nenhuma das strings da lista é porque o usuário digitou errado
	while (resposta_user not in ["2", "4"]) :
		
		#Faz a pergunta para o usuário novamente
		resposta_user = input("Digitou errado. Insira novamente: ")
	
	#Se saiu do loop o usuário digitou certo então retorna o que ele respondeu
	return resposta_user
#Fim


#Inicio
#Função que trava o lado que o usuário escolhe para jogar a peça
def trava4_usuario(lado_escolhido) :
	
	while (lado_escolhido.lower() not in ["esquerdo", "direito"]) :
		
		lado_escolhido = input("Digitado errado. Insira novamente: ")
	
	return lado_escolhido
#Fim


#Inicio
#Função para distribuição de peças do dominó de acordo com a quantidade de jogadores
#Lembrando que o n_jogadores é uma string de entrada e não um inteiro
def distribuir_pecas(pecas_domino, n_jogadores) :
	
	#Antes de distribuir as peças é necessário embaralhar(misturar)
	random.shuffle(pecas_domino)
	
	#Depois de embaralhar é necessário descobrir quantas pecas serão dadas para cada jogador
	#Para isso depende do número de jogadores
	#// é divisão inteira
	#Pega o número de pecas do dominó = 28 e divide pela quantidade de jogadores (2 ou 4)
	qnt_jogadores = int(n_jogadores)
	pecas_cada_jogador = len(pecas_domino)//qnt_jogadores
	
	#Lista de jogadores que armazena todos os jogadores e as peças que cada um terá
	lst_jogadores = []
	
	#Representa o número de peças já pegadas do dominó
	n_pecas_retiradas = 0
	
	#Implementar um loop para distribuir a mesma quantidade de peças para todos os jogadores
	for n in range(qnt_jogadores) :
		
		#Criando o jogador para colocar suas peças dentro da lista
		jogador_n = []
		
		#Loop que pegará as peças já embaralhadas e dará para cada jogador
		#No caso como já estão embaralhadas cada jogador pegará as n primeiras peças
		for peca in range(n_pecas_retiradas, n_pecas_retiradas + pecas_cada_jogador, 1) :
			
			#Inserindo as peças do jogador dentro da lista jogador_n
			jogador_n.append(pecas_domino[peca])
		
		
		#Depois de pegar todas as peças para o jogador n é preciso colocar dentro da lst_jogadores
		lst_jogadores.append(jogador_n)
		
		#Depois do jogador_n pegar todas as suas n peças então é necessário n_pecas_retiradas ser contada
		#pelo número de peças de cada jogador, ou seja, pecas_cada_jogador
		n_pecas_retiradas += pecas_cada_jogador
		
	
	#Retorna todos os jogadores com suas respectivas peças do dominó para iniciar o jogo
	return lst_jogadores


#Inicio
#Função que cria tipo um "vetor" em python que inicia a mesma vazia. 
#Essa função terá retorno no momento de colocar as peças na mesas, o qual ajudará muito
def criar_mesa() :
	
	#Mesa terá um vetor de tamanho máximo = 55 posições
	lst_mesa_domino = []
	#Percorrer o vetor e colocar as tuplas com -1 nele, como se fosse um valor default
	for i in range(55) :
		lst_mesa_domino.append((-1,-1))
	
	return lst_mesa_domino
#Fim


#Inicio
#Função que verifica a pessoa que está com a bucha de sena caso sejam 2 ou 4 jogadores
#Função retorna o jogador que está com a bucha de sena
def check_peca_inicial(jogadores_pecas, n_jogadores) :
	
	#Loop para percorrer todos os jogadores (2 ou 4)
	for jogador in range(int(n_jogadores)) :
		
		#Loop para verificar quem está com a bucha de sena (6,6) e retornar a (jogador, posicao)
		#Roda até a posição do número de peças que o primeiro jogador tem que é o mesmo que todos tem no inicio do jogo
		for peca in range(len(jogadores_pecas[0])) :
				
			#Procurando a bucha de sena (6,6)
			if (jogadores_pecas[jogador][peca] == (6,6)) :
				#Já mata a execução do programa indicando a jogador
				return jogador
#Fim


#Inicio
#Função que tira as repetições na lista de possíveis jogadas para evitar problemas
#Essa função só serve para o usuário
def retirar_repeticao(lst_possiveis_jogadas) :
	
	#Se houver repetições essa lista conterá mais de um elemento
	#Se ambos os elementos são iguais então deleta o que está na primeira posição
	for pos in range(1, len(lst_possiveis_jogadas), 1) :
		
		#Se achar uma peça diferente dentro da lista então não haverão mais repetidas
		if (lst_possiveis_jogadas[0] != lst_possiveis_jogadas[pos]) :
			return lst_possiveis_jogadas
	
	#Se percorrer tudo e só achar repetida então retorna somente uma única peça sem haver nenhuma repetição 
	return [lst_possiveis_jogadas[0]]
#Fim
		

#Inicio
#Função que atualiza as peças das mãos dos jogadores após ser jogada na mesa
def atualiza_pecas_jogadores(jogadores_pecas, jogador_elem) :
	
	#Atualiza as peças dos jogadores deletando a respectiva peça na lista jogadores_pecas 
	#jogador_elem é uma tupla que contém (jogador, elemento a ser retirado)
	#Vai até a posição do jogador e remove a peça já jogada
	peca = jogador_elem[1]
	
	#peça da tupla = (-1,-1) quer dizer que não é para atualizar as peças dos jogadores
	if (peca != (-1,-1)) :
		jogadores_pecas[jogador_elem[0]].remove(peca) 
	
	return jogadores_pecas
#Fim


#Inicio
#Função que atualiza a mesa_domino que é um vetor de tuplas
#Parâmetros (mesa do dominó, peça que o jogador jogou na rodada, a posição da pesa da esquerda e fim é da direita)
def atualiza_mesa_domino(mesa_domino, peca_jogada, inicio, fim, jogador_x) :
	
	#Se ele passou eu não faço nada para atualizar a mesa
	if (peca_jogada != (-1,-1)) :
	
		#Checar em qual dos dois lados a peça jogada se encaixa na mesa dominó
		#Lista para armazenar as possíveis jogadas que o jogador pode fazer com a mesma peça
		#Essa lista conterá tuplas onde (peça da ordem correta = (x, y), posição onde será colocada na mesa)
		lst_possiveis_jogadas = []
	
		#Loop para percorrer os lados peça jogada (lado0, lado1)
		for lado_pj in range(2) : #range de 2 porque a peça tem dois lados
		
			#Primeiro checar o lado 1 (esquerdo) depois o outro (direito)
			#Percorrer o inicio e final das peças que está na mesa (lado0, lado1)
			for lado_md in range(2) :
				
				#É necessário saber se é para comparar com a peça do lado esquerdo ou direito
				if (lado_md == 0) :
					direcao = inicio
				else :
					direcao = fim
				
				#Quando achar os lados que são iguais guarda dentro da lista de possíveis jogadas que o jogador...
				#pode fazer
				if (peca_jogada[lado_pj] == mesa_domino[direcao][lado_md]) :
				
					#Se os lados forem diferentes então não é preciso inverter a peça para colocar na mesa
					if (lado_pj != lado_md) :
					
						#Armazena depois do final corrente que é o lado direito da mesa
						if (lado_pj == 0) :
							lst_possiveis_jogadas.append((peca_jogada, fim+1))
					
						#Armazena antes do inicio corrente que é o lado esquerda da mesa
						else :
							lst_possiveis_jogadas.append((peca_jogada, inicio-1))
				
					#Senão é porque os lados são iguais então é necessário inverter a peça porque senão ficará errado na mesa
					else :
					
						#Primeiro inverter a peça porque nesse condicional sempre é invertida
						#Como tuplas são imutáveis não é possível fazer a troca nas tuplas então é preciso fazer um cópia e inverter
						a, b = peca_jogada[1], peca_jogada[0]
					
						#Coloca antes do inicio lado esquerdo da mesa
						if (lado_pj == 0) :
							lst_possiveis_jogadas.append(((a, b), inicio-1))
					
						#Coloca depois do fim lado direito da mesa
						else :
							lst_possiveis_jogadas.append(((a, b), fim+1))
		
		#print(peca_jogada)
		#print(lst_possiveis_jogadas)
		
		#Após pegar as possíveis jogadas é necessário checar se é o usuário ou a máquina que vai jogar
	
		#Diferente de 0 é a máquina
		if (jogador_x != 0) :
		
			#Escolhe aleatoriamente qualquer uma das peças
		
			#Atualizar a peça escolhida na mesa
			#peca_escolhida[1] = posição que a peça será colocada
			#peca_escolhida[0] = a peça em si já posicionada de maneira correta
			peca_escolhida = random.choice(lst_possiveis_jogadas)
			mesa_domino[peca_escolhida[1]] = peca_escolhida[0]
			
			#Retorna a mesa dominó modificada e seu começo e final
			return mesa_domino
		
		#Senão é o usuário e aí tem que interagir com o puto
		else :
			
			#Retirar as repetições que podem haver na lista de possíveis jogadas
			lst_possiveis_jogadas = retirar_repeticao(lst_possiveis_jogadas)
			
			#Se o número de peças possíveis para fazer a jogada é somente uma então só coloca na mesa 
			if (len(lst_possiveis_jogadas) == 1) :
				mesa_domino[lst_possiveis_jogadas[0][1]] = lst_possiveis_jogadas[0][0]
				return mesa_domino
			
			#Senão é porque tem uma peça a mais que pode ser jogada
			else :
				print(peca_jogada,"possui mais de uma jogada que pode fazer.")
				print("Deseja colocar a peça no lado esquerdo ou direito da mesa?")
				
				#Chama a trava enquanto o usuário não digitar corretamente
				lado_escolhido = trava4_usuario(input())
				
				#Lado esquerdo implica em posição_inicio < metade da mesa
				if (lado_escolhido == "esquerdo") :
					
					for i in range(len(lst_possiveis_jogadas)) :
						if (lst_possiveis_jogadas[i][1] < 27) :
							mesa_domino[lst_possiveis_jogadas[i][1]] = lst_possiveis_jogadas[i][0]
							return mesa_domino
				
				#Senão é o lado direito
				else :		
					for i in range(len(lst_possiveis_jogadas)) :
						if (lst_possiveis_jogadas[i][1] > 27) :
							mesa_domino[lst_possiveis_jogadas[i][1]] = lst_possiveis_jogadas[i][0]
							return mesa_domino
	
	#Senão é porque (-1,-1) não é para atualizar nada
	else :
		return mesa_domino
#Fim


#Inicio
#Função para atualizar o inicio e o começo da mesa (muito importante)
def atualiza_inicio_fim(mesa_domino, inicio_atual, fim_atual) :
	
	#Percorrer para trás para achar o inicio renovado
	while (mesa_domino[inicio_atual-1] != (-1,-1)) :
		inicio_atual -= 1
	
	#Percorrer para frente para achar o fim renovado
	while (mesa_domino[fim_atual+1] != (-1,-1)) :
		fim_atual += 1
	
	return (inicio_atual, fim_atual)
#Fim
			

#Inicio
#Função que serve para checar qual será o próximo jogador a jogar
#Onde é necessário saber o n_jogadores, pois pode ser de 2 a 4
def proximo_jogar(jogador_atual, n_jogadores) :
	
	#Se o jogador atual é o último jogador então o próximo será o primeiro que está na posição 0
	if (jogador_atual == (int(n_jogadores)-1)) :
		jogador_atual = 0
	
	#Senão entrar na condição acima é porque o próximo jogador é só somar +1 que a próximo posição
	else :
		jogador_atual += 1
	
	return jogador_atual
#Fim


#Inicio
#Função que faz uma trava para o usuário caso digite errado as peças que deseja
def trava3_usuario(lado_peca) :
	
	while (lado_peca not in ["0", "1", "2", "3", "4", "5", "6"]) :
		print("Digitou errado. Insira novamente")
		lado_peca = input()
	
	return lado_peca
#Fim


#Inicio
#Função que imprimi as peças que o usuário tem (jogador 1)
def imprimi_pecas_usuario(pecas_usuario) :
	
	for pos in range(len(pecas_usuario)) :
		print(pecas_usuario[pos], " ", end="")
		
	
	return None
#Fim


#Inicio
#Função que serve para determinar a peça que será escolhida pelo usuário ou computador a partir das regras
#Recebe como parâmetros o jogador, as peças que o determinado jogador tem (lista de tuplas) e...
#Os valores que a primeira e a última peças da mesa possui para ser jogada seguindo as regras
def jogada_peca(jogadorX, pecas_jogadorX, valor_primeira_peca, valor_ultima_peca) :
	
	#É uma lista que possui as possíveis peças que qualquer um dos jogadores podem jogar
	#Ela é inserida pelo próprio software para evitar erros
	lst_possiveis_pecas = []
	
	#Checar se com a mão dele é possível jogar alguma peça
	#Loop para percorrer pegar todas as peças possíveis
	
	for pos_peca in range(len(pecas_jogadorX)) :
		
		#Se o lado esquerdo ou direito da peça se encaixar com qualquer um dos valores da última e primeira peça da mesa então armazena
		#E lembrando que se a lista continuar vazia é porque o jogador passa a vez
		for lado in range(2) :
			
			if (pecas_jogadorX[pos_peca][lado] in [valor_primeira_peca, valor_ultima_peca]) :
				lst_possiveis_pecas.append(pecas_jogadorX[pos_peca])
			
			
	#Se tiver peças que o jogador pode jogar então usar elas
	if (len(lst_possiveis_pecas) != 0) :
		
		#Checar se quem jogará o usuário ou o computador
		
		#jogadorX = 0 então é o usuário, logo tem que interagir com ele
		if (jogadorX == 0) :
			
			lado_peca1 = trava3_usuario(input("Insira o lado 1 da peca: "))
			lado_peca2 = trava3_usuario(input("Insira o lado 2 da peca: "))
		
			while ((int(lado_peca1), int(lado_peca2)) not in lst_possiveis_pecas) :  
			
				print("A peca inserida nao existe na sua mao ou nao se pode jogar na mesa segunda as regras do domino.")
				print("Insira novamente.")
			
				lado_peca1 = trava3_usuario(input("Insira o lado 1 da peca: "))
				lado_peca2 = trava3_usuario(input("Insira o lado 2 da peca: "))
		
			#Retorna a peça da mão do usuário válida segundo as regras
			return ((int(lado_peca1), int(lado_peca2)))
		
		#JogadorX é a máquina(computador)
		else :
			
			#Pegar a lst_possiveis_pecas e escolher uma aleatoriamente da lista como se a máquina estivesse escolhendo
			#Usar a biblioteca random e o método randint que escolhe um valor dentre os colocador no parâmetro
			peca_escolhida_maquina = random.choice(lst_possiveis_pecas)
			
			return peca_escolhida_maquina
	
			
	#Senão é porque a lista de peças possíveis não existe elementos dentro, logo é porque o jogador não tem
	#Então ele passa a vez dele para o próximo jogador
	else :
		print("Passou a vez.")
		
		#Retorna o negativo que representa que não é para alterar as peças na mão do jogadorX porque ele passou 
		return (-1,-1)
		

#Inicio		
#Em casos de todos os jogadores passarem e o jogo fechar em completo
def x_jogadores_passa(contador, peca_jogada, n_jogadores) :
	
	#Quer dizer que o jogador passou
	if (peca_jogada == (-1,-1)) :
		contador += 1
		
		if (contador == int(n_jogadores)) :
			os.system("cls")
			print("Todos passaram. Logo o jogo fechou.")
			print("Eh necessario disputar por pontos.")
	
	else :
		contador = 0
	
	return contador
#Fim


#Inicio
#Vencedor(es) da partida
def vencedor_partida(jogador_x, num_pecas_jogadorX, jogadores_pecas) :
	
	#Se num peças do jogador corrente for zero é porque ele venceu por batida
	if (num_pecas_jogadorX == 0) :
		print("Jogador %d venceu a partida!" %(jogador_x+1))
	
	#Senão um ou mais jogadores venceu(ram) por pontos, pois o jogo foi fechado totalmente
	else :
		lst_pontos = []
		menor_ponto = 100
		
		#Loop para percorrer cada jogador
		for i in range(len(jogadores_pecas)) :
			
			#Imprimi a mão de cada jogador primeiro
			print("Pecas do jogador %d:" %(i+1))
			imprimi_pecas_usuario(jogadores_pecas[i])
			
			pontos_jogadorX = 0
			#Loop para percorrer a mão de cada jogador (peças)
			for j in range(len(jogadores_pecas[i])) :
				
				pontos_jogadorX += (jogadores_pecas[i][j][0] + jogadores_pecas[i][j][1])
			
			#Checar qual é o menor ponto de todos
			if (menor_ponto > pontos_jogadorX) :
				menor_ponto = pontos_jogadorX
			
			print("\nPontos: %d.\n" %pontos_jogadorX)
			lst_pontos.append(pontos_jogadorX)
		
		
		#Checar quem possui os menores pontos
		for pos_jogador in range(len(lst_pontos)) :
			
			#Se os pontos desse jogador se assemelhar com os pontos do jogador menor_ponto é porque ele é vencedor
			if (lst_pontos[pos_jogador] == menor_ponto) :
				print("Jogador %d eh vencedor!" %(pos_jogador+1))
	
	
	input("Pressione qualquer tecla para continuar...")
	return None
#Fim


#Inicio
#Função que imprime a quantidade de peças de todos os jogadores
def quantidade_pecas_jogadores(jogadores_pecas) :
	
	#Loop para percorrer os jogadores
	for pos_jogador in range(len(jogadores_pecas)) :
		
		#Imprimir quantas peças cada jogador tem
		print("Jogador %d: %d pecas" %((pos_jogador+1), len(jogadores_pecas[pos_jogador])))
	
	print("\n\n")
	
	#Retorna nada porque é uma função void
	return None
#Fim


#Inicio
#Função que imprimi as peças na mesa
def imprimi_mesa_domino(mesa_domino, inicio, fim) :
	
	print("Mesa domino:")
	#Fazer o loop e percorrer as peças e imprimindo-as de maneira correta
	for pos_peca in range(inicio, fim+1, 1) :
		
		#Imprimindo a peça
		print("|", mesa_domino[pos_peca][0], "|", mesa_domino[pos_peca][1], "|", end="")
	
	print("\n\n")
	
	#Função que retorna void, pois só serve para impressão
	return None
#Fim




def main() :
	
	
	
	return 0

if __name__ == '__main__':
	main()

