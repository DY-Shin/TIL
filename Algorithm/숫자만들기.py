import sys
sys.stdin = open('숫자만들기.txt')


def perm(n, k):
    global max_ans
    global min_ans
    if n == k:
        result = []
        for i in range(N * 2 - 1):
            if i % 2:
                result.append(op[i//2])
            else:
                if result:
                    if result[-1] == '+':
                        result.pop()
                        n1 = result.pop()
                        result.append(n1 + num[i//2])
                    if result[-1] == '-':
                        result.pop()
                        n1 = result.pop()
                        result.append(n1 - num[i//2])
                    if result[-1] == '*':
                        result.pop()
                        n1 = result.pop()
                        result.append(n1 * num[i//2])
                    if result[-1] == '/':
                        result.pop()
                        n1 = result.pop()
                        result.append(int(n1 / num[i//2]))
                else:
                    result.append(num[i//2])
        if result[0] > max_ans:
            max_ans = result[0]
        if result[0] < min_ans:
            min_ans = result[0]
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                op[k] = oper_list[i]
                perm(n, k + 1)
                visited[i] = 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    oper = list(map(int, input().split()))
    num = list(map(int, input().split()))
    visited = [0] * N
    op = [0] * (N - 1)
    ans = []
    max_ans = -987654321
    min_ans = 987654321
    oper_list = []
    for i in range(oper[0]):
        oper_list.append('+')
    for i in range(oper[1]):
        oper_list.append('-')
    for i in range(oper[2]):
        oper_list.append('*')
    for i in range(oper[3]):
        oper_list.append('/')
    perm((N - 1), 0)
    print(f'#{test_case} {max_ans - min_ans}')
