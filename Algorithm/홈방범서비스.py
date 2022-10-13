import sys
sys.stdin = open('홈방범.txt')


def solve():
    ans = 0
    for k in range(N + 1, 0, -1):
        for x in range(N):
            for y in range(N):
                cnt = 0
                for hx, hy in home:
                    if abs(x - hx) + abs(y - hy) < k:
                        cnt += 1
                if M * cnt - cost[k] >= 0 and ans < cnt:
                    ans = cnt
    return ans


cost = [0] * 22
cost[1] = 1
for k in range(2, 22):
    cost[k] = k * k + (k - 1) * (k - 1)
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    home = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                home.append((i, j))

    print(f'#{test_case} {solve()}')