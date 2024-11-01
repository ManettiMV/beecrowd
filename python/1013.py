inputs = input().split(' ') # Lê os inputs e separa baseado nos espaços
A = int(inputs[0])
B = int(inputs[1])
C = int(inputs[2])
maior = lambda a, b: (a + b + abs(a - b)) / 2

print(f"{int(maior(maior(A,B),C))} eh o maior")