"""
6. Crie um programa que gere e exiba os 100 primeiros números primos.
"""

primos = []
for num in range(2, 550):
    if len(primos) == 100:
        break
    if all(num % p != 0 for p in primos):
        primos.append(num)
print(primos)