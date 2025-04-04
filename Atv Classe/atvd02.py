'''
Conversor de Unidades
○ Crie funções para converter quilômetros em milhas, metros em
centímetros e litros em mililitros.
'''
def km_para_milhas(km):
    return km * 0.621371

def metros_para_centimetros(metros):
    return metros * 100

def litros_para_mililitros(litros):
    return litros * 1000

print(km_para_milhas(10))
print(metros_para_centimetros(5))
print(litros_para_mililitros(3))