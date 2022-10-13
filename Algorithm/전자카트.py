def perm(n, k, ssum):
    global ans
    if ssum > ans:
        return

    if n == k:
        ssum += arr[p[n - 1]][0]
        if ssum < ans:
            ans = ssum

    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                p[k] = a[i]
                perm(n, k + 1, ssum + arr[p[k - 1]][p[k]])
                visited[i] = 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    a = []
    ans = 987654321
    for i in range(N):
        a.append(i)
    p = [0] * (N + 1)
    p[0] = p[N] = a[0]
    visited = [0] * N
    visited[0] = 1
    perm(N, 1, 0)
    print(f'#{test_case} {ans}')
