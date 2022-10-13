import sys
sys.stdin = open('사칙연산.txt')


def calc(op, left, right):
    if op == '+':
        result = left + right
    elif op == '-':
        result = left - right
    elif op == '*':
        result = left * right
    elif op == '/':
        result = left / right
    return int(result)


def post(n):
    # 잎노드
    if ch1[n] == 0 or ch2[n] == 0:
        return num[n]
    # 가지노드
    else:
        L = post(ch1[n])
        R = post(ch2[n])
        num[n] = calc(oper[n], L, R)
        return num[n]


T = 10
for test_case in range(1, T + 1):
    N = int(input())
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    oper = [''] * (N + 1)
    num = [0] * (N + 1)

    for i in range(N):
        temp = list(input().split())
        idx = int(temp[0])
        # 연산자
        if temp[1] == '+' or temp[1] == '-' or temp[1] == '*' or temp[1] == '/':
            oper[idx] = temp[1]
            ch1[idx] = int(temp[2])
            ch2[idx] = int(temp[3])
        # 피연산자
        else:
            num[idx] = int(temp[1])

    ans = post(1)
    print(f'#{test_case} {ans}')
