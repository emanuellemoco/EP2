import json
from random import randint 


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
		#Gera um numero aleatório que que somado na vida 
		elemento_sorteJogador = randint(-200,200)
		elemento_sorteOponente = randint(-200,200)

		VidaOponente = VidaOponente - (PoderJogador - DefesaOponente) + elemento_sorteOponente
		VidaJogador = VidaJogador - (PoderOponente - DefesaJogador) + elemento_sorteJogador

		print ("Sua vida é: {0}, a vida do seu oponente é: {1}".format(VidaJogador, VidaOponente))
		resposta = input ("Você quer fugir? 1- sim , 2-  nao")
		if resposta == "1":
#FAZER A CONDIÇÃO DA FUGA AQUI TAMBÉM 
			###
			print ("Arregão!!!!!!! \n") 

			if VidaJogador > VidaOponente:
				print ("Fuga mal sucedida, você vai ter que batalhar\n ")
				#chamar outra funcao tipo resultado_fuga que nao vai ter o round de ataque 
				resultado = batalha(VidaJogador, VidaOponente, DefesaJogador, DefesaOponente, PoderJogador, PoderOponente)
				print (resultado)
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


numerodeinspermons = 3  #QUANDO ADICIONAR INSPERMONS, MUDAR AQUI
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
		x = (randint(0,2))
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
				#chamar outra funcao tipo resultado_fuga que nao vai ter o round de ataque 
				resultado = batalha(VidaJogador, VidaOponente, DefesaJogador, DefesaOponente, PoderJogador, PoderOponente)
				print (resultado)
				print ("\n")

			else:

				print ("Fuga bem sucedida! \n Deu empate")



	if pergunta == "4":
		
		#PRECISAMOS ARRUMAR AQUI PRA FICAR BONITINHO
		print ("O seu insperdex é: \n")
		print(listainsperdex)




	elif pergunta == "3":
		print ("você vai dormir. até a próxima!")
		break
	#escrever algo para se a pessoa nao escolher nenhum dos dois