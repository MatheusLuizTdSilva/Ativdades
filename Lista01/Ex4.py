"""
4. Um cliente alugou um carro e rodou alguns quilômetros por um certo número de
dias. O custo diário é de R$90. Se ele rodou mais de 100 km, há uma taxa extra de
R$12 por km adicional. Calcule o valor total a ser pago.
"""

dias = int(input('Dias de aluguel: '))
km = float(input('Quilômetros rodados: '))
custo_total = dias * 90 + max(0, (km - 100) * 12)
print(f'Total a pagar: R${custo_total:.2f}')