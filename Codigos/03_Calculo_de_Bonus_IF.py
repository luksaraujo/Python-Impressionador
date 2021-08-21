# Cálculo de Bonus
# Crie um programa que calcule e dê um print no bônus
# que os funcionários devem receber segundo a regra:
# A meta é 1000 vendas.
# Se o valor de vendas for maior ou igual a meta, o
# valor do bônus do funcionário é 10% do valor de vendas.
# Caso contrário o valor de bônus do funcionário é 0.
# Print o bônus dos 3 funcionários

meta = 1000
vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700

if vendas_funcionario1 >= meta:
    print(f'O 1º funcionário receberá R$ {vendas_funcionario1 * 0.10} de bônus.')
else:
    print(f'O 1º funcionário receberá R$ 0 de bônus.')
if vendas_funcionario2 >= meta:
    print(f'O 2º funcionário receberá R$ {vendas_funcionario2 * 0.10} de bônus.')
else:
    print(f'O 2º funcionário receberá R$ 0 de bônus.')
if vendas_funcionario3 >= meta:
    print(f'O 3º funcionário receberá R$ {vendas_funcionario3 * 0.10} de bônus.')
else:
    print(f'O 3º funcionário receberá R$ 0 de bônus.')
