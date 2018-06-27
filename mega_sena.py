'''
Author: Luca Gouveia
Created on 28/05/18
'''

import random

num = 6 # Limite de numeros da aposta (6 = menor aposta da mega-sena)

print("Você pode escolher os números entre 01 e 60")
print("Sua aposta consiste em {} número(s) separados por hífen".format(num))

aposta = []
while (len(aposta) != num*2): #Evita a entrada maior ou menor que o necessario
    aposta = list(map(str,input("Digite sua aposta: ").split("-")))
    aposta_saida = "".join(aposta) # Aposta realizada - fora da lista e na ordem igual a entrada
    aposta = "".join(sorted(aposta))# Aposta realizada - fora da lista e ordenada

numeros = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60']
sorte = [] # Lista que recebe os numeros sorteados
sorteado = ''
contador = 0

#-------------FUNCAO_DE_ORDENACAO-----------------
lista_o = [] #Lista dos sorteados ordenados
def ordenar(lista,lista_o):
	for i in range(len(lista)):
		menor = min(lista)
		lista.remove(menor)
		lista_o.append(menor)
	return(lista_o)
#-------------------------------------------------
 
while(sorteado != aposta):    
	random.shuffle(numeros) #Os numeros da lista(numeros) sao misturados

	for i in range(num):
        	sorte.append(numeros[i])
    
	sorteado = "".join(ordenar(sorte,lista_o))    
	print(sorteado)
	sorte.clear() # Limpa a lista dos numeros sorteados, fazendo com que a probabilidade de ganhar fica a mesma
	lista_o.clear() #Limpa a lista ordenada dos numeros sorteados (essa lista pega os numeros sorteados e ordena, para que nao seja levado em consideracao a ordem)
	contador+=1

print("=============================================================")
print("GANHOU!!!!!!!! Aposta {}".format("({})".format(aposta_saida)))
print("Houve(ram) {} sorteio(s) até você ganhar!".format(contador))
