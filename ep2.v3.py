#versao3

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

##def definicao (bixo):
	#um for pra passar por toda a lista com os inspermons, 
	#comparar quando o nome for igual ao nome bixo 
	#pegar os dados desse bixo
"""	for a in range (numerodeinspermons-1):
		if ipmon["nome"] == bixo:
			teste = "AAAAAAAAA"
			return teste

"""


with open('inspermons.json') as arquivo:
 	inspermons = json.load(arquivo)


numerodeinspermons = 3  #QUANDO ADICIONAR INSPERMONS, MUDAR AQUI

while True:
	oponente=[]
	lista=[]
	contador=1
	vida = -1
	pergunta = input ("Você deseja: \n 1 - escolher seu inspermon \n 2 - passear \n 3 - dormir \n ")
	
	if pergunta ==  "1":

		for ipmon in inspermons:
			print (contador) #numero para a pessoa escolher 
			mostra_ipmon(ipmon) #exibe todos os ipmons
			contador+=1
			lista.append(ipmon["nome"])
			oponente.append(ipmon)


			 
		resposta = int(input ("Escolha um Inspermon para você jogar: \n"))
#		print (lista)
		print ("\n")
#		print (oponente)
		bixo = lista[resposta-1]
		print ("Você escolheu o Inspermon {0} \n".format(bixo)) #exibe qual inspermon a pessoa escolheu


	if pergunta == "2":
		print ("\n")
		print ("aqui vai ser a batalha \n")

#escolhe inimigo aleatorio e mostra
		print ("O seu adversário é: ")
		print (escolheinimigo (inspermons))
		print ("\n")
		
		
#faz a batalha e recebe o resultado
		for a in range (len(inspermons)):

			if ipmon["nome"] == bixo:
				print ("AAAAAAAAA KCT")


		if vida < 0:  #vamos ter que mudar tudo aqui 
			print ("você morreu") 
			break


	elif pergunta == "3":
		print ("você vai dormir. até a próxima!")
		break
	#escrever algo para se a pessoa nao escolher nenhum dos dois