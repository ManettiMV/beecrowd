N = int(input())             # Lê o input em segundos

horas = N // 3600            # Calcula a quantidade de horas inteiras
N %= 3600                    # Atualiza N para o restante após calcular horas

minutos = N // 60            # Calcula a quantidade de minutos inteiros no restante
segundos = N % 60            # O restante representa os segundos

print(f"{horas}:{minutos}:{segundos}")