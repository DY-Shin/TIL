# import sys
# sys.stdin = open('partsum.txt')

T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    result = []
    partsum = 0
    for i in range(1 << 12):
        subset = []
        for j in range(12):
            if i & (1 << j):
               subset.append(A[j])
        result.append(subset)

    for i in range(len(result)):
        idx = i
        total = 0
        if len(result[idx]) == N:
            for j in range(len(result[idx])):
                total += result[idx][j]
                if total == K:
                    partsum = 1

    print(f'#{test_case} {partsum}')