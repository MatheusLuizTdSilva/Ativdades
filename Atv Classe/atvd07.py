'''
Simulador de Dados
○ Crie uma função que gere um número aleatório entre 1 e 6, simulando o
lançamento de um dado.
'''

import random

def rolar_dado():
    return random.randint(1, 6)

print(f"Resultado do dado: {rolar_dado()}")