import json
from random import randint 

# escolher um inspermon aleatório
def escolheinimigo (ipmon):
	x = (randint(0,2))
	return (ipmon[x])

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
	return bixo

#função feita para teste, ainda não está com o código da batalha
def batalha(jogador, inimigo):
	return "vitoria"



with open('inspermons.json') as arquivo:
 	inspermons = json.load(arquivo)

vida = -1
numerodeinspermons = 3  #QUANDO ADICIONAR INSPERMONS, MUDAR AQUI

bixo = escolhe_jogador(inspermons)

while True:
	pergunta = input ("Você deseja: \n 1 - escolher seu inspermon \n 2 - passear \n 3 - dormir \n ")
	
	if pergunta ==  "1":
		bixo = escolhe_jogador(inspermons)


	if pergunta == "2":
		print ("aqui vai ser a batalha \n")

		#escolhe inimigo aleatorio e mostra
		adversario = escolheinimigo(inspermons)
		print ("O seu adversário é: ")
		print (adversario)
		print ("\n")
		
		resultado = batalha(bixo, adversario)
		if resultado == "vitoria":
			print("Voce venceu!")
		else:
			print("Voce perdeu!")
		
#faz a batalha e recebe o resultado"
#		for a in range (numerodeinspermons-1):
#			for ipmon in inspermons:
#				
#				if ipmon["nome"] == bixo:
#					print ("AAAAAAAAA KCT")


		if vida < 0:  #vamos ter que mudar tudo aqui 
			print ("você morreu") 
			break


	elif pergunta == "3":
		print ("você vai dormir. até a próxima!")
		break
	#escrever algo para se a pessoa nao escolher nenhum dos dois