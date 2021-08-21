# Parte 2 - Inputs e Strings
#
# A maioria das empresas trabalham com um Código para cada produto que possuem. A Hashtag&Drink, por exemplo, tem mais de 1.000 produtos e possui um código para cada produto.
# Ex: 
# Coca -> Código: BEB1300543<br>
# Pepsi -> Código: BEB1300545<br>
# Vinho Primitivo Lucarelli -> Código: BAC1546001<br>
# Vodka Smirnoff -> Código: BAC17675002<br>
#
# Repare que todas as bebidas não alcóolicas tem o início do Código "BEB" e todas as bebidas alcóolicas tem o início do código "BAC".
#
# Crie um programa de consulta de bebida que, dado um código qualquer, identifique se a bebida é alcóolica. O programa deve responder True para bebidas alcóolicas e False para bebidas não alcóolicas. Para inserir um código, use um input.
#
# Dica: Lembre-se do comando in para strings e sempre insira os códigos com letra maiúscula para facilitar.

bebida = input('Digite o código: ')
print('BAC' in bebida)
