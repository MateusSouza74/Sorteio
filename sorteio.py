print("Quais os nomes irão participar do sorteio?\n")
nomes_string = input("> ")
nomes = nomes_string.split(", ")

import random

num_itens = len(nomes)
random_escolha = random.randint(0, num_itens - 1)
pessoa_que_vai_pagar = nomes[random_escolha]

print(f"{pessoa_que_vai_pagar} irá pagar a refeição hoje.")