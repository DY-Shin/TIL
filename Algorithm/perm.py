def perm(n, k, ssum):
    global ans
    if ans < ssum:
        return

    if k == n:
        if ans > ssum:
            ans = ssum
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k + 1, ssum + arr[k][num[k]])
            arr[k], arr[i] = arr[i], arr[k]

arr = [1, 2, 3]
N = len(arr)
num = [i for i in range(N)]
ans = 0
perm(N, 0, 0)
print(ans)