"""
7. Solicite um número ímpar ao usuário e calcule a diferença entre o quadrado do
número anterior e do próximo número ímpar.
"""

num = int(input('Digite um número ímpar: '))
anterior = (num - 2) ** 2
proximo = (num + 2) ** 2
diferenca = proximo - anterior
print(f'Diferença: {diferenca}')