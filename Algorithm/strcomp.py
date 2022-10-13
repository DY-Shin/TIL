import sys
sys.stdin = open('strcomp.txt')

def BruteForce(t, p):
    for i in range(N - M + 1):
        flag = 1
        for j in range(M):
            if t[i + j] != p[j]:
                flag = 0
                break
        if flag:
            return 1
    return 0

T = int(input())
for test_case in range(1, T + 1):
    pattern = input()
    text = input()
    N = len(text)
    M = len(pattern)

    print(f'#{test_case} {BruteForce(text, pattern)}')