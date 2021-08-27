# Exercícios
# 1. Faturamento do Melhor e do Pior Mês do Ano
# Qual foi o valor de vendas do melhor mês do Ano? E valor do pior mês do ano?
# meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
# vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
# vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

# ------------- Functions -------------
def top_3_values(_list):
    top3 = []
    for i in range(3):
        highest_value_auxiliar = max(_list)
        top3.append(highest_value_auxiliar)
        _list.remove(highest_value_auxiliar)
    return top3
# -------------------------------------

# --------------- Lists ---------------
months = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
sales_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
sales_2sem = [19850, 20120, 17540, 15555, 49051, 9650]
sales_year = sales_1sem + sales_2sem
# -------------------------------------

# --------------- Flags ---------------
highest_value = max(sales_year)
lower_value = min(sales_year)
better_month = months[sales_year.index(highest_value)]
worst_month = months[sales_year.index(lower_value)]
total_profit = sum(sales_year)
higher_percentual = highest_value / total_profit
# -------------------------------------

print(f'O melhor valor de vendas do ano foi de R$ {highest_value:,.2f} no mês de {better_month}')
print(f'O pior valor de vendas do ano foi de R$ {lower_value:,.2f} no mês de {worst_month}')

# 2. Continuação
# Agora relacione as duas listas para printar 'O melhor mês do ano foi {} com {} vendas' e o mesmo para o pior mês do ano.
# (OBS: Solicitação acima já executada anteriormente)
# Calcule também o faturamento total do Ano e quanto que o melhor mês representou do faturamento total.

print(f'O faturamento total do ano foi de R$ {total_profit:,.2f}')
print(f'O melhor mês representou {higher_percentual:.1%} das vendas do ano')

# 3. Crie uma lista com o top 3 valores de vendas do ano (sem fazer "no olho")

top_3 = top_3_values(sales_year)
print(top_3)