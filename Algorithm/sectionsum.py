import sys
sys.stdin = open('sectionsum.txt')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N_M = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    N = N_M[0]
    M = N_M[1]

    def my_sum(num):
        sum_list = [0] * N
        for i in range(N - M + 1):
            for j in range(M):
                sum_list[i] += num[i + j]
        return sum_list

    def my_max(mm):
        tmp = 0
        for i in mm:
            if i > tmp:
                tmp = i
        return tmp

    def my_min(mm):
        tmp = 100000000000
        for i in mm:
            if i < tmp and i != 0:
                tmp = i
        return tmp

    print(f'#{test_case} {my_max(my_sum(num_list)) - my_min(my_sum(num_list))}')