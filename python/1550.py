from collections import deque

def bfs(a, b):
    d = [-1] * 100010
    queue = deque()
    queue.append(a)
    d[a] = 0

    while queue:
        v = queue.popleft()
        if d[b] != -1:
            break

        rev = int(str(v)[::-1])
        if d[rev] == -1:
            d[rev] = d[v] + 1
            queue.append(rev)
        
        if d[v + 1] == -1:
            d[v + 1] = d[v] + 1
            queue.append(v + 1)

    return d[b]

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(bfs(a, b))
