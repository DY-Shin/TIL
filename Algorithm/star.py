import sys
sys.stdin = open('star.txt')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    print(f'#{test_case}')

    s_list = list(map(int, input().split()))

    N = s_list[0]
    n = s_list[1]

    if n == 1:
        for i in range(1, N + 1):
            print(i * '*')
    if n == 2:
        for i in range(N):
            print((N - i) * '*')
    if n == 3:
        for i in range(1, N + 1):
            print((N - i) * ' ' + (i * 2 - 1) * '*')