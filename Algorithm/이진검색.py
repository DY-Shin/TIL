def binarySearch(n, arr, key):
    low = 0
    high = n - 1
    mid = low + (high - low) // 2
    if arr[mid] > key:
        flag = 0
    else:
        flag = 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return 1
        elif arr[mid] > key:
            if flag:
                return 0
            flag = 1
            high = mid - 1
        else:
            if flag == 0:
                return 0
            flag = 0
            low = mid + 1
    return 0


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    list_A = list(map(int, input().split()))
    list_A.sort()
    list_B = list(map(int, input().split()))
    ans = 0
    for i in range(M):
        ans += binarySearch(N, list_A, list_B[i])
    print(f'#{test_case} {ans}')
