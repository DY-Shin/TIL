def specsort(a, N):
    for i in range(N - 1):
        idx = i
        if i % 2:
            for j in range(i + 1, N):
                if a[idx] > a[j]:
                    idx = j
            a[i], a[idx] = a[idx], a[i]
        else:
            for j in range(i + 1, N):
                if a[idx] < a[j]:
                    idx = j
            a[i], a[idx] = a[idx], a[i]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    specsort(arr, N)

    print(f'#{test_case}', end=' ')
    print(*arr[:10])