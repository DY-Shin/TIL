import sys
sys.stdin = open('graph.txt')

def DFS(v):
    visited[v] = 1
    stack.append(v)
    for w in adj_list[v]:
        if visited[w] == 0:
            DFS(w)
    return

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())  # 정점, 간선
    adj_list = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    stack = []
    for i in range(E):
        s, e = map(int, input().split())
        adj_list[s].append(e)

    S, G = map(int, input().split())
    DFS(S)

    print(f'#{test_case}', end=' ')
    if G in stack:
        print(1)
    else:
        print(0)
    print(adj_list)