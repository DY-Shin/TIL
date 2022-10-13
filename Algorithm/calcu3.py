import sys
sys.stdin = open('calcu3.txt')

icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}
isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}

def infix_to_postfix(exp):
    stack = []
    result = []
    for token in exp:
        if '0' <= token <= '9':
            result.append(token)
        elif token == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            if stack:
                while icp[token] <= isp[stack[-1]]:
                    result.append(stack.pop())
                    if not stack:
                        break
            stack.append(token)

    while stack:
        result.append(stack.pop())
    return ''.join(result)

def calc(exp):
    stack = []
    for token in exp:
        if '0' <= token <= '9':
            stack.append(int(token))
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            if token == '+':
                stack.append(op1 + op2)
            elif token == '*':
                stack.append(op1 * op2)
    return stack.pop()

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    infix = input()
    postfix = infix_to_postfix(infix)
    print(f'#{test_case} {calc(postfix)}')

