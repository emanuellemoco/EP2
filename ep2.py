#EP2
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


#escolhevoce
def escolhevoce (escolheinimigo(inspermons)):
	inimigonome  = ipmon["nome"]


with open('inspermons.json') as arquivo:
 	inspermons = json.load(arquivo)



vida = -1
numerodeinspermons = 3


while True:
	pergunta = input ("Você deseja: \n 1 - escolher seu inspermon \n 2 - passear \n 3 - dormir \n ?")
	
	if pergunta ==  "1":
			print ("escolher Inspermon")
			#mostrar os nomes dos poks e deixar a pessoa escolher
			#for i in range (numerodeinspermons-1)    

			#pensar um jeito de fazer mostrando a lista 



	if pergunta == "2":
		print ("aqui vai ser a batalha \n")

		#escolhe inimigo aleatorio e mostra
		print ("O seu adversário é: ")
		print (escolheinimigo (inspermons))
		print ("\n")
		
		
		#faz a batalha e recebe o resultado
		

		if vida < 0:  #vamos ter que mudar tudo aqui 
			print ("você morreu") 
			break



	elif pergunta == "3":
		print ("você vai dormir. até a próxima!")
		break
	#escrever algo para se a pessoa nao escolher nenhum dos dois