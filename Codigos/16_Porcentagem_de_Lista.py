# 1. Calculando % de uma lista
# Faremos algo parecido com "filtrar" uma lista. Mais pra frente no curso aprenderemos outras formas de fazer isso, mas com o
# nosso conhecimentoa atual já conseguimos resolver o desafio.

# Digamos que a gente tenha uma lista de vendedores e ao invés de saber todos os vendedores que bateram a meta, eu quero
# conseguir calcular a % de vendedores que bateram a meta. Ou seja, se temos 10 vendedores e 3 bateram a meta, temos 30% dos
# vendedores que bateram a meta.

meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

# RESOLUÇÃO 01 - Criando uma lista auxiliar apenas com os vendedores que bateram a meta
acima_da_meta = []
for venda in vendas:
    if venda[1] >= meta:
        acima_da_meta.append(venda)
percentual = len(acima_da_meta) / len(vendas)
print(f'{percentual:.1%} dos vendedores bateram a meta')

# Resolução 02 - Fazendo o cálculo diretamente na lista que já temos
qtde_vendedores_acima_da_meta = 0
for venda in vendas:
    if venda[1] >= meta:
        qtde_vendedores_acima_da_meta += 1
print(f'{qtde_vendedores_acima_da_meta / len(vendas):.1%} dos vendedores bateram a meta')

# Para treinar uma estrutura parecida, crie um novo código para responder: quem foi o vendedor que mais vendeu?
maior_vendedor = ''
maior_valor_venda = 0
for venda in vendas:
    if venda[1] > maior_valor_venda:
        maior_valor_venda = venda[1]
        maior_vendedor = venda[0]
print(f'O melhor vendedor foi {maior_vendedor} com {maior_valor_venda} vendas')