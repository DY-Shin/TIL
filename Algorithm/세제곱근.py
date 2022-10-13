def binary_search():
    low = -1
    high = N
    while low <= high:
        mid = (low + high) // 2
        key = mid ** 3
        if key == N:
            return mid
        elif key > N:
            high = mid - 1
        else:
            low = mid + 1
    return -1


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    print(f'#{test_case} {binary_search()}')