import sys
sys.stdin = open('nodedistance.txt')

from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1

    while q:
        v = q.popleft()
        for w in adj_list[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[v] + 1

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)

    for _ in range(E):
        s, e = map(int, input().split())
        adj_list[s].append(e)
        adj_list[e].append(s)

    S, G = map(int, input().split())
    bfs(S)
    result = visited[G] - visited[S]
    if result < 0:
        result = 0
    print(f'#{test_case} {result}')
