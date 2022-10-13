import sys
sys.stdin = open('minmax.txt')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    mm_list = list(map(int, input().split()))

    def my_max(mm):
        tmp = 0
        for i in mm:
            if i > tmp:
                tmp = i
        return tmp

    def my_min(mm):
        tmp = 1000000
        for i in mm:
            if i < tmp:
                tmp = i
        return tmp

    print(f'#{test_case} {my_max(mm_list) - my_min(mm_list)}')