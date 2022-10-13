from collections import deque


def BFS(n, m):
    Q = deque()
    visited[n] = 1
    Q.append(n)
    while Q:
        n = Q.popleft()
        if n == m:
            return visited[n] - 1
        for t in [n + 1, n - 1, n * 2, n - 10]:
            if 0 < t <= 1000000 and visited[t] == 0:
                Q.append(t)
                visited[t] = visited[n] + 1


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    print(f'#{test_case} {BFS(N, M)}')
