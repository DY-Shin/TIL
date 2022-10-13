import sys
sys.stdin = open('miro.txt')

def dfs(r, c):
    global flag
    visited[r][c] = 1
    if arr[r][c] == 3:
        flag = 1
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr == N:
            continue
        if nc < 0 or nc == N:
            continue
        if visited[nr][nc] == 1:
            continue
        if arr[nr][nc] == 1:
            continue
        dfs(nr, nc)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    flag = 0
    start_i = 0
    start_j = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start_i = i
                start_j = j

    dfs(start_i, start_j)
    print(f'#{test_case} {flag}')


