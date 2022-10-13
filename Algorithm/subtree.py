import sys
sys.stdin = open('subtree.txt')


def postorder(n):
    global cnt
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        cnt += 1


T = int(input())
for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    V = E + 1
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    cnt = 0
    for i in range(E):
        p, c = arr[i*2], arr[i*2 + 1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    postorder(N)
    print(f'#{test_case} {cnt}')
