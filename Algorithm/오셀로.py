import sys
sys.stdin = open('오셀로.txt')


def print_arr():
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            print(arr[i][j], end=' ')
        print()
    print()


def check(sx, sy, dol):
    for i in range(8):
        nx = sx + dx[i]
        ny = sy + dy[i]
        flag = False
        while 0 < nx <= N and 0 < ny <= N:
            if arr[nx][ny] == 0:
                break
            if arr[nx][ny] == dol:
                flag = True
                ex = nx
                ey = ny
                break
            nx += dx[i]
            ny += dy[i]
        if flag:
            nx = sx
            ny = sy
            while not(nx == ex and ny == ey):
                nx += dx[i]
                ny += dy[i]
                arr[nx][ny] = dol


dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * (N + 1) for _ in range(N + 1)]

    mid = N // 2
    arr[mid][mid] = arr[mid + 1][mid + 1] = 2
    arr[mid][mid + 1] = arr[mid + 1][mid] = 1
    # print_arr()

    for i in range(M):
        x, y, dol = map(int, input().split())
        arr[x][y] = dol
        check(x, y, dol)
        # print_arr()

    B = 0
    W = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if arr[i][j] == 1:
                B += 1
            elif arr[i][j] == 2:
                W += 1
    print(f'#{test_case} {B} {W}')
