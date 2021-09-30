# 3. Comparação com Ano Anterior
# Digamos que você está analisando as vendas de produtos de um ecommerce e quer
# identificar quais produtos tiveram no ano de 2020 mais vendas do que no ano de
# 2019 para reportar isso para a diretoria.
#
# Sua resposta pode ser um print de cada produto, qual foi a venda de 2019, a venda
# de 2020 e o % de crescimento de 2020 para 2019.
#
# Lembrando, para calcular o % de crescimento de um produto de um ano para o outro,
# podemos fazer: (vendas_produto2020/vendas_produto2019 - 1)
#
# Dica: lembre do enumerate, ele pode facilitar seu "for"

# --------------- Variavel ---------------
products = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
sales_2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
sales_2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]
# ----------------------------------------

for index, product in enumerate(products):
    sold_in_2019 = sales_2019[index] # Flag
    sold_in_2020 = sales_2020[index] # Flag
    if sold_in_2020 > sold_in_2019:
        print(f"O produto '{product}' vendeu R$ {sold_in_2019:,.2f} unidades em 2019 e R$ {sold_in_2020:,.2f} unidades em 2020.")
        print(f"As vendas foram {sold_in_2020 / sold_in_2019 - 1:.1%} maiores em 2020.")
        print(f"----------------------------------------------------")