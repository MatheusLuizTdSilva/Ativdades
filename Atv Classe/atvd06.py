'''
Contador de Vogais
○ Crie uma função que conte quantas vogais existem em uma palavra ou
frase.
'''

def contar_vogais(texto):
    return sum(c in "aeiou" for c in texto.lower())

palavra = input("Digite uma palavra ou frase: ")
print(contar_vogais(palavra))