# Exercícios - Módulo 1.ipynb
#
# Exercícios do Módulo 1 - Operações, Variáveis e Input
#
# Parte 1 - Operações e Variáveis
# Crie um programa que imprima (print) os principais
# indicadores da loja Hashtag&Drink no último ano.
# Obs: faça tudo usando variáveis.
#
# Valores do último ano:
#
# Quantidade de Vendas de Coca = 150
# Quantidade de Vendas de Pepsi = 130
# Preço Unitário da Coca = 1,50
# Preço Unitário da Pepsi = 1,50
# Custo da Loja: 2.500,00"""

qtde_coca = 150
qtde_pepsi = 130
preco_coca = 1.50
preco_pepsi = 1.50
despesas_loja = 2500

# 1. Qual foi o faturamento de Pepsi da Loja?
print(f'O faturamento de Pepsi foi de R$ {qtde_pepsi * preco_pepsi}')

# 2. Qual foi o faturamento de Coca da Loja?
print(f'O faturamento de Coca foi de R$ {qtde_coca * preco_coca}')

# 3. Qual foi o Lucro da loja?
faturamento = qtde_pepsi * preco_pepsi + qtde_coca * preco_coca
lucro = faturamento - despesas_loja
print(f'O lucro da loja foi de R$ {lucro}')

# 4. Qual foi a Margem da Loja? (Lembre-se, margem = Lucro / Faturamento). Não precisa formatar em percentual
margem = lucro / faturamento
print(f'A margem da loja foi de R$ {margem:.02f}')
