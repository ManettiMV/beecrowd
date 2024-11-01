# Lê os inputs e realiza o calculo pedido
name = str(input())
salary = float(input())
sales = float(input())

received = sales * 0.15

print(f"TOTAL = R$ {salary+received:.2f}")