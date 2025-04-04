'''
Calculadora de Média
○ Crie uma função que receba três notas e retorne a média do aluno.
○ Mostre se o aluno está aprovado ou reprovado (média mínima 7).
'''

def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        return f"Média: {media}. Aluno Aprovado!"
    else:
        return f"Média: {media}. Aluno Reprovado!"

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
print(calcular_media(nota1, nota2, nota3))