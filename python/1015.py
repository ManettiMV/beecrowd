import math
p1 = input().split(' ') # Lê e separa os inputs baseado nos espaços
p2 = input().split(' ')

x1 = float(p1[0])
y1 = float(p1[1])
x2 = float(p2[0])
y2 = float(p2[1])

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)   # Realiza os calculos necessários
print(f"{distance:.4f}")