'''
Calculadora Simples
○ Crie funções para soma, subtração, multiplicação e divisão.
○ Faça um programa que peça dois números e mostre o resultado da
operação escolhida.
'''

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Não é possível dividir por zero!"
    
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (+, -, *, /): ")

if operacao == "+":
    print(f"Resultado: {soma(a, b)}")
elif operacao == "-":
    print(f"Resultado: {subtracao(a, b)}")
elif operacao == "*":
    print(f"Resultado: {multiplicacao(a, b)}")
elif operacao == "/":
    print(f"Resultado: {divisao(a, b)}")