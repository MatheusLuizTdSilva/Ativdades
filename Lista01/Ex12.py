"""
12. Peça ao usuário a quantidade de turmas e a quantidade total de alunos. Informe a
média de alunos por turma, mas avise se alguma turma tiver mais de 40 alunos.
"""

turmas = int(input('Quantidade de turmas: '))
alunos = int(input('Quantidade total de alunos: '))
media = alunos / turmas
if media > 40:
    print('Alerta: alguma turma tem mais de 40 alunos!')
print(f'Média de alunos por turma: {media:.2f}')