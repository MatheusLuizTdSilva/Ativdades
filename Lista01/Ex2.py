"""
2. Solicite um valor em segundos e converta para dias, horas e minutos.
"""

segundos = int(input('Digite um valor em segundos: '))
dias = segundos // 86400
horas = (segundos % 86400) // 3600
minutos = (segundos % 3600) // 60
print(f'{dias} dias, {horas} horas, {minutos} minutos')