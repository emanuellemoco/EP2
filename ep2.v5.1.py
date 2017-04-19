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
		resOponente = VidaOponente - (PoderJogador - DefesaOponente)
		resJogador = VidaJogador - (PoderOponente - DefesaJogador)
		
		if resJogador > resOponente:
			return "você ganhou"
		elif resOponente > resJogador:
			return "voce perdeu"
		elif resJogador == resOponente:
			return "empate"


		# if VidaOponente <= 0:
		# 	return "Você ganhou"
		# elif VidaJogador <= 0:
		# 	return "Você perdeu"
		# elif VidaJogador == VidaOponente:
		# 	return "Deu empate"
	

with open('inspermons.json') as arquivo:
 	inspermons = json.load(arquivo)


numerodeinspermons = 3  #QUANDO ADICIONAR INSPERMONS, MUDAR AQUI

#primeira coisa a fazer é pedir pra escolher um inspermon
bixo = escolhe_jogador(inspermons)
#print(bixo)


PoderJogador = (bixo["poder"])
VidaJogador = (bixo["vida"])
DefesaJogador = (bixo["defesa"])



while True:
	pergunta = input ("Você deseja: \n 1 - escolher seu inspermon \n 2 - passear \n 3 - dormir \n ")
	
	if pergunta ==  "1":
		bixo = escolhe_jogador(inspermons)

		PoderJogador = (bixo["poder"])
		VidaJogador = (bixo["vida"])
		DefesaJogador = (bixo["defesa"])

	if pergunta == "2":
		print ("aqui vai ser a batalha \n")

		#escolhe inimigo aleatorio e mostra
		x = (randint(0,2))
		adversario = inspermons[x]
		print ("O seu adversário é: ")
		print (adversario)

		PoderOponente = (inspermons[x]["poder"])
		VidaOponente = (inspermons[x]["vida"])
		DefesaOponente = (inspermons[x]["poder"])




		resultado = batalha(VidaJogador, VidaOponente, DefesaJogador, DefesaOponente, PoderJogador, PoderOponente)
		print (resultado)

		# if resultado == "ganhou":
		# 	print("Voce venceu!")
		# elif resultado == "perdeu":
		# 	print("Voce perdeu!")
		# elif resultado == "empate":
		# 	print ("Empate")

		



		# if vida < 0:  #vamos ter que mudar tudo aqui 
		# 	print ("você morreu") 
		# 	break


	elif pergunta == "3":
		print ("você vai dormir. até a próxima!")
		break
	#escrever algo para se a pessoa nao escolher nenhum dos dois