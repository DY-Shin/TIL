def check(data):
    stack = []
    for i in range(len(data)):
        if data[i] == '(' or data[i] == '{':
            stack.append(data[i])
        elif data[i] == ')':
            if len(stack) > 0:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return 0
            else:
                return 0
        elif data[i] == '}':
            if len(stack) > 0:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return 0
            else:
                return 0
    if len(stack):
        return 0
    return 1

T = int(input())
for test_case in range(1, T + 1):
    sentence = input()

    print(f'#{test_case} {check(sentence)}')
