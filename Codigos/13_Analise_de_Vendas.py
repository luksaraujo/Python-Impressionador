# 2. Análise de Vendas
# Nesse exercício vamos fazer uma "análise simples" de atingimento de Meta.
# Temos uma lista com os vendedores e os valores de vendas e queremos identificar
# (printar) quais os vendedores que bateram a meta e qual foi o valor que eles venderam.

# --------------- Variavel ---------------
goal = 10000
sales = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870]
]
# ----------------------------------------

# --------------- Programa ---------------
for salesperson_register in sales:
    sales_value = salesperson_register[1]
    salesperson = salesperson_register[0]
    if sales_value >= goal:
        print(f"{salesperson} bateu a meta com R$ {sales_value:.2f} de vendas")
# ----------------------------------------