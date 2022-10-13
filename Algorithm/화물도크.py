T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: x[1])

    post_e = 0
    cnt = 0
    for s, e in arr:
        if post_e <= s:
            post_e = e
            cnt += 1
    print(f'#{test_case} {cnt}')
