def DFS(n, k, e, cnt):
    global ans
    if ans <= cnt:
        return

    if n == k:
        if ans > cnt:
            ans = cnt
    else:
        DFS(n, k + 1, arr[k] - 1, cnt + 1)
        if e > 0:
            DFS(n, k + 1, e - 1, cnt)


T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    ans = 987654321
    DFS(arr[0], 2, arr[1] - 1, 0)
    print(f'#{test_case} {ans}')
