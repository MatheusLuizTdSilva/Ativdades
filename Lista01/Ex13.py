"""
13. Dado um salário inicial e um aumento percentual que dobra a cada ano, calcule o
salário atual após vários anos.
"""

salario = float(input('Salário inicial: '))
aumento = float(input('Aumento percentual: ')) / 100
anos = int(input('Quantidade de anos: '))
salario_final = salario * (1 + aumento) ** anos
print(f'Salário após {anos} anos: R${salario_final:.2f}')
