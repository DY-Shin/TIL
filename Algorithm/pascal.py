N = 100
memo = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(i + 1):
        if j == 0 or i == j:
            memo[i][j] = 1
        else:
            memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    print(f'#{test_case}')
    for i in range(N):
        for j in range(i + 1):
            print(memo[i][j], end=' ')
        print()