T = int(input())
for test_case in range(1, T + 1):
    expression = list(map(str, input().split()))
    stack = []

    for i in range(len(expression)):
        if expression[i].isdecimal():
            stack.append(int(expression[i]))
        else:
            if len(stack) > 1:
                k2 = stack.pop()
                k1 = stack.pop()
                if expression[i] == '*':
                    stack.append(k1 * k2)
                elif expression[i] == '/':
                    stack.append(k1 // k2)
                elif expression[i] == '+':
                    stack.append(k1 + k2)
                elif expression[i] == '-':
                    stack.append(k1 - k2)
            else:
                if expression[i] == '.':
                    result = stack[0]
                else:
                    result = 'error'
                    break

    if len(stack) > 1:
        result = 'error'

    print(f'#{test_case} {result}')
