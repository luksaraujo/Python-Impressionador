# Operações com String
# str -> transforma número em string
# in -> verifica se um texto está contido dentro do outro
# operador + -> concatenar string
# format e {} -> substitui valores
# %s -> substitui textos
# %d -> substitui números decimais

faturamento = 1000
custo = 500
lucro = faturamento - custo

# Como concatenar números com strings
print("O faturamento da loja foi de: " + str(faturamento))

# Exibir valores de variáveis dentro das strings com o método format
print("O faturamento foi de: {}".format(faturamento))

# Exibir valores de variáveis dentro das strings com placeholders
print(f"O faturamento foi de: {faturamento}")

# Uso de %s e %d
print("O faturamento foi de: %d e o custo foi de %d" % (faturamento, custo))

# Uso do in
print("@" in "lucas@gmail.com") # Imprime True
print("@" in "lucas.gmail.com") # Imprime False
