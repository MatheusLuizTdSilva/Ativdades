"""1. Peça ao usuário três notas e calcule:
a. A média aritmética simples
b. A média ponderada considerando os pesos 2, 2 e 3
c. A média ponderada considerando os pesos 1, 2 e 2
"""

notas = [float(input(f'Digite a nota {i+1}: ')) for i in range(3)]
media_simples = sum(notas) / 3
media_ponderada_1 = (notas[0]*2 + notas[1]*2 + notas[2]*3) / 7
media_ponderada_2 = (notas[0]*1 + notas[1]*2 + notas[2]*2) / 5
print(f'Média Simples: {media_simples:.2f}')
print(f'Média Ponderada (2,2,3): {media_ponderada_1:.2f}')
print(f'Média Ponderada (1,2,2): {media_ponderada_2:.2f}')