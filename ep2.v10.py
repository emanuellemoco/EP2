import json
from random import randint 

numerodeinspermons = 12  #QUANDO ADICIONAR INSPERMONS, MUDAR AQUI

# mostra todas as informações de todos os inspermons 
def mostra_ipmon(inspermons):
	print("Inspermon : {0}".format(ipmon["nome"]))
	print("poder = {0}".format(ipmon["poder"]))
	print("vida = {0}".format(ipmon["vida"]))
	print("defesa = {0}\n".format(ipmon["defesa"]))


def escolhe_jogador(inspermons):
	print("Escolha um Inspermon para você jogar: \n")
	for i in range(len(inspermons)):
		ipmon = inspermons[i]
		print("{0} : {1} (vida: {2}, poder: {3}, defesa: {4})".format(i + 1, 
			ipmon["nome"], ipmon["vida"], ipmon["poder"], ipmon["defesa"]))
	print ("\n")
	resposta = int(input ("Qual a sua escolha: \n"))
	#print (oponente)
	bixo = inspermons[resposta-1]
	print ("Você escolheu o Inspermon {0} \n".format(bixo["nome"]))
#	print ("Você escolheu o Inspermon {0} \n".format(bixo))
	return bixo

def batalha(VidaJogador, VidaOponente, DefesaJogador, DefesaOponente, PoderJogador, PoderOponente):
	while VidaJogador > 0 and VidaOponente > 0:
		#Funcionalidade 3: A sorte está lançada!
		#Gera um numero aleatório que que é somado na vida 
		elemento_sorteJogador = randint(-100,100)
		elemento_sorteOponente = randint(-100,100)

		VidaOponente = VidaOponente - (PoderJogador - DefesaOponente) + elemento_sorteOponente

		if VidaOponente<=0:
			if VidaOponente < 0:
				VidaOponente = 0
			print("Você ganhou!!")
			print("A sua vida é: {0}\n".format(VidaJogador))

			#Funcionalidade 4: Vamos evoluir Inspèrmons!
			#quando o jogador ganha uma batalha, é acrescido 30 pontos na sua vida.
			VidaJogador = VidaJogador + 30
			print ("O seu Inspèrmon evoluiu! Sua vida agora é: {0}".format(VidaJogador))
			return""

		VidaJogador = VidaJogador - (PoderOponente - DefesaJogador) + elemento_sorteJogador
		if VidaJogador<=0:
			if VidaJogador <0:
				VidaJogador = 0
			print("vc perdeu\n")
			print ("a vida do seu oponente é: {0}".format(VidaOponente))
			return""

		print ("Sua vida é: {0}, a vida do seu oponente é: {1}".format(VidaJogador, VidaOponente))
		
		#Funcionalidade 2: Vamos fugir da batalha!
		resposta = input ("Você quer fugir? 1- sim , 2-  nao")
		if resposta == "1":

			print ("Arregão!!!!!!! \n") 
			#condições para ocorrer a fuga:
			#Só é possível fugir da batalha se a Vida do Jogador foi MENOR do que a Vida do Oponente
			if VidaJogador > VidaOponente:
				print ("Fuga mal sucedida, você vai ter que batalhar\n ")
				print ("Você perdeu seu round de ataque!")
				VidaOponente = VidaOponente - (PoderJogador - DefesaOponente) + elemento_sorteOponente
				print ("Sua vida é: {0}, a vida do seu oponente é: {1}".format(VidaJogador, VidaOponente))
				#resultado = batalha(VidaJogador, VidaOponente, DefesaJogador, DefesaOponente, PoderJogador, PoderOponente)
				#print (resultado)
				print ("\n")
				return ""

			else:

				print ("Fuga bem sucedida! \n Deu empate")
				return ""

				break
		
		elif resposta == "2":
			print ("nao quero fugir")
			if VidaOponente <= 0:  
				return "você ganhou"

			elif VidaJogador <= 0:
				return "voce perdeu"


with open('inspermons.json') as arquivo:
 	inspermons = json.load(arquivo)

#Funcionalidade 5: Salve o jogo!
try:
	with open ('insperdex.json') as arquivo:
		insperdex = json.load(arquivo)
#		print ("TESTEEEEEEEEE")
except Exception as inst:
#	print ("Você ainda não batalhou, não tem adversários no insperdex")
	listainsperdex = [] #cria a lista para o insperdéx

#primeira coisa a fazer é pedir pra escolher um inspermon
bixo = escolhe_jogador(inspermons)
print ("\n")
#print(bixo)

PoderJogador = (bixo["poder"])
VidaJogador = (bixo["vida"])
DefesaJogador = (bixo["defesa"])

while True:
	pergunta = input ("Você deseja: \n 1 - escolher seu inspermon \n 2 - passear \n 3 - dormir \n 4 - Exibir Insperdex \n ")
	print ("\n")

	if pergunta ==  "1":
		bixo = escolhe_jogador(inspermons)

		PoderJogador = (bixo["poder"])
		VidaJogador = (bixo["vida"])
		DefesaJogador = (bixo["defesa"])

	if pergunta == "2":
		print ("Você entrou em uma batalha \n")

		#escolhe inimigo aleatorio e mostra
		x = (randint(0,numerodeinspermons-1))
		adversario = inspermons[x]
		listainsperdex.append(adversario)  #adiciona os adversários no insperdéx
		print ("O seu adversário é: ")
		print (adversario)
		print ("\n")

		PoderOponente = (inspermons[x]["poder"])
		VidaOponente = (inspermons[x]["vida"])
		DefesaOponente = (inspermons[x]["poder"])

		print ("Ainda da tempo de fugir dessa batalha! O que você deseja?\n")
		pergunta_fuga = input("1 - Eu quero batalhar! \n2 - Estou com medo, quero fugir\n")

		if pergunta_fuga == "1":

			print ("aqui vai ser a batalha \n") 

			resultado = batalha(VidaJogador, VidaOponente, DefesaJogador, DefesaOponente, PoderJogador, PoderOponente)
			print (resultado)
			print ("\n")

		elif pergunta_fuga == "2":  #opcao de fugir

			print ("Arregão!!!!!!! \n") 

			if VidaJogador > VidaOponente:
				print ("Fuga mal sucedida, você vai ter que batalhar\n ")
				resultado = batalha(VidaJogador, VidaOponente, DefesaJogador, DefesaOponente, PoderJogador, PoderOponente)
				print (resultado)
				print ("\n")

			else:

				print ("Fuga bem sucedida! \n Deu empate")


	if pergunta == "4":
		print ("O seu insperdex é: \n")
		print(listainsperdex)
		print ("\n")


	elif pergunta == "3":
		print ("Você vai dormir. até a próxima!\n")
		print ("ZZZZZZzzzzzzZZzzz")
		break
		
#Funcionalidade 5: Salve o jogo!
	#criar arquivo
	with open ('inspermons.json', 'w') as arquivo:
		json.dump (inspermons, arquivo)

	with open ('inperdex.json', 'w') as arquivo:
		json.dump (listainsperdex, arquivo)


