import sys
sys.stdin = open('디저트카페.txt')


def DFS(x, y, dir, cnt):
    global result
    nx = x + dx[dir]
    ny = y + dy[dir]
    if nx == sx and ny == sy:
        result = max(result, cnt)
        return
    if 0 <= nx < N and 0 <= ny < N and visited[arr[nx][ny]] == 0:
        visited[arr[nx][ny]] = 1
        DFS(nx, ny, dir, cnt + 1)
        if dir < 3:
            DFS(nx, ny, dir + 1, cnt + 1)
        visited[arr[nx][ny]] = 0


dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * 101
    result = -1
    for i in range(N):
        for j in range(N):
            sx, sy = i, j
            visited[arr[i][j]] = 1
            DFS(i, j, 0, 1)
            visited[arr[i][j]] = 0

    print(f'#{test_case} {result}')
    