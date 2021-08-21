# Exercícios
# 1. Cadastro de CPF
# Crie um programa para cadastro de CPF de clientes que
# recebe o CPF em um input box apenas com números.
#
# Ex: 'Insira seu CPF (digite apenas números)'
#
# Caso o usuário digite algo diferente de números ou digite
# menos de 11 caracteres (tamanho do CPF brasileiro), o
# programa deve exibir uma mensagem de "Digite seu CPF
# corretamente e digite apenas números"

CPF = input("Digite seu CPF (insira apenas números): ")
CPF_is_numeric = CPF.isnumeric()
CPF_length_equals_to_11 = True if len(CPF) == 11 else False

if CPF_is_numeric:
    if CPF_length_equals_to_11:
        print("CPF cadastrado com sucesso!")
    else:
        print("Um CPF válido contém 11 caracteres!")
else:
    print("Digite apenas números!")
