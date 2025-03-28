"""
3. Peça ao usuário o valor total das mercadorias compradas. Se for menor que R$500,
não há imposto. Caso contrário, aplique uma taxa de 50% sobre o valor que ultrapassar
os R$500.
"""

valor = float(input('Digite o valor das mercadorias: '))
imposto = max(0, (valor - 500) * 0.5)
print(f'Imposto: R${imposto:.2f}')