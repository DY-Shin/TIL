T = int(input())
for test_case in range(1, T + 1):
    N = float(input())
    result = ''
    cnt = 0
    while N % 1 != 0:
        if N * 2 >= 1:
            result += '1'
            N = N * 2 - 1
        else:
            result += '0'
            N *= 2
        cnt += 1
        if cnt > 12:
            result = 'overflow'
            break
    print(f'#{test_case} {result}')
