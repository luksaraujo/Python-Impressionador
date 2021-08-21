# Cálculo de bônus com uma nova regra
# Agora, crie um novo código que calcule e dê
# um print no bônus dos funcionários novamente.
# Porém há uma nova regra nesse 2º caso:
# A meta é 1000 vendas
# Agora, os funcionários que venderem muito acima
# da meta ganham mais bônus do que os outros. Então
# o bônus é definido da seguinte forma:
# Se vendas funcionário for maior ou igual a 2000,
# então o bônus é de 15% sobre o valor de vendas;
# Se vendas funcionário for menor do que 2000 e maior
# ou igual a 1000, então o bônus é de 10% sobre o valor
# de vendas;
# Se vendas funcionário for menos do que 1000 então o
# bônus do funcionário é de 0.

vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700
bonus = 0

if vendas_funcionario1 >= 2000:
    bonus = vendas_funcionario1 * 0.15
elif vendas_funcionario1 >= 1000:
    bonus = vendas_funcionario1 * 0.10
else:
    bonus = 0
print(f'O funcionário 1 ganhou R$ {bonus} de bônus.')

if vendas_funcionario2 >= 2000:
    bonus = vendas_funcionario2 * 0.15
elif vendas_funcionario2 >= 1000:
    bonus = vendas_funcionario2 * 0.10
else:
    bonus = 0
print(f'O funcionário 2 ganhou R$ {bonus} de bônus.')

if vendas_funcionario3 >= 2000:
    bonus = vendas_funcionario3 * 0.15
elif vendas_funcionario3 >= 1000:
    bonus = vendas_funcionario3 * 0.10
else:
    bonus = 0
print(f'O funcionário 3 ganhou R$ {bonus} de bônus.')
