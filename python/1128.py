MAXSIZE = 2010

def dfs(u):
    vis[u] = True
    for i in range(1, n + 1):
        if g[u][i] and not vis[i]:
            dfs(i)

while True:
    n, m = map(int, input().split())
    
    if n == 0 and m == 0:  # Quando n e m forem zero, interrompe o loop
        break

    g = [[False] * MAXSIZE for _ in range(MAXSIZE)]
    for _ in range(m):
        u, v, p = map(int, input().split())
        if p == 1:
            g[u][v] = True
        else:
            g[u][v] = g[v][u] = True

    result = 1  # Presumindo que a promessa foi cumprida
    for i in range(1, n + 1):
        vis = [False] * MAXSIZE
        dfs(i)
        if not any(vis[1:n+1]):  # Verifica se todos os vértices foram visitados
            result = 0  # Se não foram, então a promessa não foi cumprida
            break

    print(result)