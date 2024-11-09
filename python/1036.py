import math

# Separa o input em 3 variáveis
n = input().split() 
a = float(n[0])
b = float(n[1])
c = float(n[2])

# Verifica se a != 0 antes de continuar
if a == 0:
    print("Impossivel calcular")
else:
    delta = b**2 - 4 * a * c

    if delta < 0:
        print("Impossivel calcular")
    else:
        positive = (-b + math.sqrt(delta)) / (2 * a)
        negative = (-b - math.sqrt(delta)) / (2 * a)
        print(f"R1 = {positive:.5f}")
        print(f"R2 = {negative:.5f}")