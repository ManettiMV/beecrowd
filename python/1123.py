import heapq
import sys
from math import inf

def dijkstra(start, destination, n, graph):
    distances = [inf] * n
    distances[start] = 0
    priority_queue = [(0, start)] 

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances[destination]


def main():
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    idx = 0
    while True:
        n, m, c, k = map(int, data[idx].split())
        idx += 1

        if n == 0 and m == 0 and c == 0 and k == 0:
            break

        graph = [[] for _ in range(n)]

        for _ in range(m):
            u, v, p = map(int, data[idx].split())
            idx += 1

            if u >= c and v >= c: 
                graph[u].append((v, p))
                graph[v].append((u, p))
            elif u >= c and v < c: 
                graph[u].append((v, p))
            elif u < c and v >= c: 
                graph[v].append((u, p))
            elif u < c and v < c and abs(u - v) == 1: 
                graph[u].append((v, p))
                graph[v].append((u, p))

        result = dijkstra(k, c - 1, n, graph)
        print(result)


if __name__ == "__main__":
    main()