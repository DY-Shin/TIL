def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    p = list(range(N + 1))

    for i in range(M):
        a, b = arr[i * 2], arr[i * 2 + 1]
        p[find_set(b)] = find_set(a)

    cnt = 0
    for i in range(1, N + 1):
        if p[i] == i:
            cnt += 1
    print(f'#{test_case} {cnt}')
