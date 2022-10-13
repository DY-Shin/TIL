T = int(input())
for test_case in range(1, T + 1):
    stack = []
    arr = list(map(str, input()))
    for i in range(len(arr)):
        if stack:
            if stack[-1] == arr[i]:
                stack.pop()
            else:
                stack.append(arr[i])
        else:
            stack.append(arr[i])
    print(f'#{test_case} {len(stack)}')