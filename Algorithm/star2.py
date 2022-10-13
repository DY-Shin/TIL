import sys
sys.stdin = open('star2.txt')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    print(f'#{test_case}')

    s_list = list(map(int, input().split()))
    N = s_list[0]
    n = s_list[1]

    if n == 1:
        for i in range(1, (N // 2) + 2):
            print(i * '*')
        for i in range((N // 2), 0, -1):
            print(i * '*')
    if n == 2:
        for i in range(1, (N // 2) + 2):
            print((N // 2 + 1 - i) * ' ' + i * '*')
        for i in range((N // 2), 0, -1):
            print((N // 2 + 1 - i) * ' ' + i * '*')
    if n == 3:
        for i in range(N // 2 + 1, 0, -1):
            print(' ' * (N // 2 - i + 1) + '*' * (2 * i - 1))
        for i in range(2, N // 2 + 2):
            print(' ' * (N // 2 - i + 1) + '*' * (2 * i - 1))
    if n == 4:
        for i in range(N // 2 + 1, 0, -1):
            print((N // 2 + 1 - i) * ' ' + '*' * i)
        for i in range(2, N // 2 + 2):
            print((N // 2) * ' ' + '*' * i)