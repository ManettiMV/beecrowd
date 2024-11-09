value = float(input())

# Lista de notas e moedas
banknotes = [100, 50, 20, 10, 5, 2]
coins = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

# Processamento das notas
print("NOTAS:")
for note in banknotes:
    quantity = int(value // note)
    print(f"{quantity} nota(s) de R$ {note:.2f}")
    value %= note  # Atualiza o valor para o restante

# Ajuste para evitar problemas de precisão com valores decimais
value = round(value, 2)

# Processamento das moedas
print("MOEDAS:")
for coin in coins:
    quantity = int(value // coin)
    print(f"{quantity} moeda(s) de R$ {coin:.2f}")
    value %= coin  # Atualiza o valor para o restante
