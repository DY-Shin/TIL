import sys
sys.stdin = open("행렬찾기.txt")

def my_min(arr):
    mul = []
    idx = []
    for a in range(len(arr)):
        for b in range(a + 1, len(arr)):
            if arr[a][0] > arr[b][0] and arr[a][0] * arr[a][1] == arr[b][0] * arr[b][1]:
                arr[a], arr[b] = arr[b], arr[a]
    for a in range(len(arr)):
        mul.append(arr[a][0] * arr[a][1])
    new = sorted(mul)
    for a in range(len(new)):
        for b in range(len(mul)):
            if new[a] == mul[b]:
                idx.append(b)
    return idx


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    x_y_list = []
    i = 0
    j = 0
    di = [-1, 0]
    dj = [0, -1]

    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                flag = 1
                for k in range(2):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if ni >= 0 and nj >= 0:
                        if arr[ni][nj] != 0:
                            flag = 0
                            break
                if flag:
                    x = n + 1
                    y = n + 1
                    for k in range(i, n):
                        if arr[k][j] == 0:
                            x = k
                            break
                    for l in range(j, n):
                        if arr[i][l] == 0:
                            y = l
                            break
                    if x == n + 1:
                        x = n
                    if y == n + 1:
                        y = n
                    x -= i
                    y -= j
                    x_y_list.append([x, y])

    idx = my_min(x_y_list)

    print(f'#{test_case} {len(x_y_list)}', end=' ')
    for i in idx:
        print(*x_y_list[i], end=' ')
    print()
