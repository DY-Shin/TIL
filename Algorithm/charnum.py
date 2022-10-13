import sys
sys.stdin = open('charnum.txt')

T = int(input())
for test_case in range(1, T + 1):
    char = list(map(str, input()))
    text = list(map(str, input()))
    N = len(char)
    arr = [0] * N
    maxval = -1

    for i in range(len(text)):
        for j in range(N):
            if char[j] == text[i]:
                arr[j] += 1

    for i in range(len(arr)):
        if arr[i] > maxval:
            maxval = arr[i]

    print(f'#{test_case} {maxval}')