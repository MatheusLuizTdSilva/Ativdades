'''
Verificador de Palíndromos
○ Crie uma função que receba uma palavra e diga se ela é um palíndromo
(lê igual de frente para trás).
'''

def verificar_palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()
    if palavra == palavra[::-1]:
        return "É um palíndromo!"
    else:
        return "Não é um palíndromo!"

palavra = input("Digite uma palavra: ")
print(verificar_palindromo(palavra))