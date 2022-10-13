import sys
sys.stdin = open('arrayminsum.txt')

def perm(n, k, ssum):
    global ans
    if ans < ssum:
        return
    if n == k:
        if ans > ssum:
            ans = ssum
    else:
        for i in range(k, n):
            A[k], A[i] = A[i], A[k]
            perm(n, k + 1, ssum + arr[k][A[k]])
            A[k], A[i] = A[i], A[k]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 987654321
    A = list(range(N))
    perm(N, 0, 0)
    print(f'#{test_case} {ans}')
