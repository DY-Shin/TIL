import sys
sys.stdin = open('최소생산비용.txt')


def perm(n, k, ssum):
    global ans
    if ssum >= ans:
        return
    if n == k:
        ans = min(ans, ssum)
        return
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                perm(n, k + 1, ssum + arr[k][i])
                visited[i] = 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 987654321
    perm(N, 0, 0)
    print(f'#{test_case} {ans}')
