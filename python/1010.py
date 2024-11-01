values = input().split(' ') # Lê a linha de input e separa baseado nos espaços
product1_code = int(values[0])  # Define o inicio pro código
product1_num = int(values[1])   # Define os outros a partir dos espaços e assim vai
product1_price = float(values[2])

values = input().split(' ')
product2_code = int(values[0])
product2_num = int(values[1])
product2_price = float(values[2])

amount = product1_num * product1_price + product2_num * product2_price  # Calcula o que foi pedido

print(f"VALOR A PAGAR: R$ {amount:.2f}")