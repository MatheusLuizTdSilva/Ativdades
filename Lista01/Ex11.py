"""
11. Crie um sistema de login que não permite que o nome de usuário e a senha sejam
iguais.
"""

usuario = input('Usuário: ')
senha = input('Senha: ')
if usuario == senha:
    print('Usuário e senha não podem ser iguais.')
else:
    print('Cadastro realizado com sucesso!')