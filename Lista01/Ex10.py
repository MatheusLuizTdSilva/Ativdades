"""
10. Solicite um número inteiro maior que 1 e verifique se ele é primo.
"""

num = int(input('Digite um número maior que 1: '))
é_primo = num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))
print(f'É primo: {é_primo}')