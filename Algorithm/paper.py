def paper(N):
    memo = [1, 1]
    for i in range(2, N + 1):
        memo.append(memo[i - 2] * 2 + memo[i - 1])
    return memo[N]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input()) // 10

    print(paper(N))
