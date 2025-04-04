'''
Gerador de Tabuada
○ Crie uma função que receba um número e imprima a tabuada desse
número.
'''

def gerar_tabuada(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Digite um número para gerar a tabuada: "))
gerar_tabuada(numero)