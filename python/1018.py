N = int(input())                                        # Lê o input N

print(N)                                                # Printa N

banknotes = [100, 50, 20, 10, 5, 2, 1]                  # Banco com valor das notas

for note in banknotes:                                  # Loop para definir quanto de cada nota
    quantity = N // note                                # Define quanto precisa de tal nota 
    print(f"{quantity} nota(s) de R$ {note},00")        # Printa essa quantidade
    N %= note                                           # Da um update no resto pra repetir o loop