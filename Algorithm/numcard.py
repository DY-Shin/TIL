import sys
sys.stdin = open('numcard.txt')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    card = int(input())
    cnt = [0] * 10
    for _ in range(N):
        cnt[card % 10] += 1
        card //= 10

    def my_max(mm):
        tmp = 0
        for i in mm:
            if i > tmp:
                tmp = i
        return tmp

    max_i = 0
    max_n = my_max(cnt)
    for i in range(1, 10):
        if cnt[i] == max_n:
            max_i = i

    print(f'#{test_case} {max_i} {max_n}')
