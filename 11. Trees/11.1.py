from collections import deque


def main():
    n, v = map(int, input().split())
    graph = {}
    for i in range(n):
        arr = list(map(int, input().split()))
        filtered = list(filter(lambda x: x != -1, arr))
        graph[i] = filtered
    q = deque(graph[v])
    visited = set()
    visited.add(v)
    while len(q) != 0:
        el = q.popleft()
        visited.add(el)
        [q.append(x) for x in graph[el] if x not in visited]
    print(*sorted(visited))
main()