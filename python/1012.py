points = input().split(' ') # Lê uma linha de inputs e separa baseado nos espaços
A = float(points[0])
B = float(points[1])
C = float(points[2])

print(f"TRIANGULO: {(A * C)/2:.3f}")    # Realiza os calculos necessários
print(f"CIRCULO: {3.14159 * C**2:.3f}")
print(f"TRAPEZIO: {((A+B) * C)/2:.3f}")
print(f"QUADRADO: {B**2:.3f}")
print(f"RETANGULO: {A*B:.3f}")