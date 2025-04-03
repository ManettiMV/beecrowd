import sys
from math import inf

def dijkstra(src, des, n, matrix):
    dist = [inf] * (n + 1)
    visited = [False] * (n + 1)
    
    dist[src] = 0

    for _ in range(1, n + 1):
        short_dist = inf
        next_vertex = -1

        # Encontra o próximo vértice não visitado com a menor distância
        for i in range(1, n + 1):
            if not visited[i] and dist[i] < short_dist:
                short_dist = dist[i]
                next_vertex = i

        if short_dist == inf:
            break

        visited[next_vertex] = True

        # Atualiza as distâncias para os vizinhos
        for i in range(1, n + 1):
            if matrix[next_vertex][i] != inf and dist[next_vertex] + matrix[next_vertex][i] < dist[i]:
                dist[i] = dist[next_vertex] + matrix[next_vertex][i]

    return dist[des]


def main():
    input = sys.stdin.read
    data = input().strip().split("\n")
    idx = 0

    while True:
        n, e = map(int, data[idx].split())
        idx += 1

        if n == 0 and e == 0:
            break

        # Inicializa a matriz de adjacência
        matrix = [[inf] * (n + 1) for _ in range(n + 1)]

        for _ in range(e):
            x, y, h = map(int, data[idx].split())
            idx += 1
            matrix[x][y] = h
            if matrix[y][x] != inf:  # Verifica se já existe uma estrada no sentido oposto
                matrix[x][y] = matrix[y][x] = 0

        k = int(data[idx])
        idx += 1

        results = []
        for _ in range(k):
            o, d = map(int, data[idx].split())
            idx += 1
            r = dijkstra(o, d, n, matrix)
            if r == inf:
                results.append("Nao e possivel entregar a carta")
            else:
                results.append(str(r))

        print("\n".join(results))
        print()


if __name__ == "__main__":
    main()
