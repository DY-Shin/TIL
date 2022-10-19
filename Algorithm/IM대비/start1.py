T = int(input())
for test_case in range(1, T + 1):
    lst = list(map(int, input()))

    ans = []
    n = 0
    for i in range(len(lst)):
        n = lst[i] + n * 2
        if i % 7 == 6:
            ans.append(n)
            n = 0

    print(f'#{test_case}', *ans)
