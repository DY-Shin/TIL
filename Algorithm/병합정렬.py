from collections import deque


def merge_sort(arr):
    global cnt
    if len(arr) == 1:
        return arr
    middle = len(arr) // 2
    left = []
    right = []
    for i in range(middle):
        left.append(arr[i])
    for i in range(middle, len(arr)):
        right.append(arr[i])
    left = merge_sort(left)
    right = merge_sort(right)
    if left[-1] > right[-1]:
        cnt += 1
    return merge(left, right)


def merge(left, right):
    result = []
    left = deque(left)
    right = deque(right)
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.popleft())
            else:
                result.append(right.popleft())
        elif len(left) > 0:
            result.append(left.popleft())
        elif len(right) > 0:
            result.append(right.popleft())
    return result


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(arr)
    print(f'#{test_case} {result[N//2]} {cnt}')
