"""
8. Solicite uma temperatura em Celsius e converta para Fahrenheit.
"""

temp_celsius = float(input('Temperatura em Celsius: '))
temp_fahrenheit = (temp_celsius * 9/5) + 32
print(f'Temperatura em Fahrenheit: {temp_fahrenheit:.2f}')