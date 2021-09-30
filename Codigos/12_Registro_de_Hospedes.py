# Exercícios
# 1. Criando um Registro de Hóspedes
# Digamos que você está criando o sistema para registrar a
# chegada de hóspedes em um hotel. No hotel, os hóspedes podem
# ter quartos com 1, 2, 3 e 4 pessoas. Seu sistema deve conseguir:
#
# Identificar quantas pessoas o hóspede que acabou de chegar
# vai ter no quarto (perguntando por meio de input)
# De acordo com a quantidade de pessoas do hóspede, ele deve
# fazer um for para perguntar o cpf e o nome de cada pessoa,
# a fim de registrá-la no quarto (2 inputs para cada pessoa,
# 1 para o cpf e outro para o nome)
# O seu programa então deve gerar uma lista com todas as pessoas
# que ficarão no quarto em que cada item dessa lista é o nome da
# pessoa e o cpf da pessoa, assim:
# quarto = [
#     ['João', 'cpf:00000000000'],
#     ['Julia', 'cpf:11111111111'],
#     ['Marcus', 'cpf:22222222222'],
#     ['Maria', 'cpf:33333333333'],
# ]
# Para simplificar, não vamos nos preocupar com possibilidades de "tentar
# colocar mais de 1 hóspede, digitar o cpf errado, etc. Nosso objetivo é
# treinar a criação de uma rotina de cadastro

# --------------- Variavel ---------------
quantity_of_people_in_the_room = int(input("Quantas pessoas haverão no quarto? "))
room = []
# ----------------------------------------

# --------------- Programa ---------------
for i in range(quantity_of_people_in_the_room):
    person_name = input(f"Qual o nome do {i+1}º hóspede? ")
    person_cpf = input(f"Qual o CPF do {i+1}º hóspede? ")
    guest = [person_name, f"CPF: {person_cpf}"]
    room.append(guest)

print(room)
# ----------------------------------------