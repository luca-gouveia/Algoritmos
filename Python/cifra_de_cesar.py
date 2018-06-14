'''
Author: Luca Gouveia
Created on 27/05/18
'''

alf = ['A', 'B', 'C', 'D', 'E', 'F', 'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
mod_alf = alf[:]

tamanho = int(input("Digite a quantidade de letras que serão deslocadas: "))
deslocamento = alf[:tamanho]

for i in deslocamento:
    mod_alf.remove(i)
    mod_alf.insert(25,i)

#-----------------------------------------

entrada = str(input("Seu texto: ")).upper()
saida = []

resposta = int(input("Você quer criptografar ou descriptografar? CRIPT(1) - DESCRIPT(2): "))

if(resposta == 1):
    for i in range (len(entrada)):
        if(entrada[i] == ' '):
            saida.append(' ')
        else:
            index_n = alf.index(entrada[i])
            saida.append(mod_alf[index_n])

    print("Saida:","".join(saida))

if(resposta == 2):
    for i in range(len(entrada)):
        if(entrada[i] == ' '):
            saida.append(' ')
        else:
            index_mod = mod_alf.index(entrada[i])
            saida.append(alf[index_mod])

    print("Saida:","".join(saida))

