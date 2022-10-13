import sys
sys.stdin = open('color.txt')

T = int(input())
for test_case in range(1, T + 1):

    N = int(input())
    total = 0
    arr = [[0]*10 for _ in range(10)]
    for i in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        if color == 1:
            for j in range(x2 - x1 + 1):
                for k in range(y2 - y1 + 1):
                    arr[x1 + j][y1 + k] += 1
        elif color == 2:
            for j in range(x2 - x1 + 1):
                for k in range(y2 - y1 + 1):
                    arr[x1 + j][y1 + k] += 2

    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                total += 1

    print(f'#{test_case} {total}')
