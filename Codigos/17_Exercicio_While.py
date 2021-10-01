# Exercícios
# 1. Input até o usuário parar
# Vamos criar um sistema de vendas. Nosso programa deve registrar os produtos e as quantidades (2 inputs) e adicionar em uma lista.
# O programa deve continuar rodando até o input ser vazio, ou seja, o usuário apertar enter sem digitar nenhum produto ou quantidade.
# Ao final do programa, ele deve printar todos os produtos e quantidades vendidas.

sales = []
while True:
    product = input("Qual é o produto? ")
    if not product:
        break
    qtt = int(input("Qual a quantidade comprada? "))
    sales.append([product, qtt])
print(sales)