import sys
sys.stdin = open('pali_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N - M + 1):
            char = ''
            stri_list = arr[i][j:j + M]
            if stri_list == stri_list[::-1]:
                stri = ''.join(stri_list)

            for k in range(M):
                char += arr[j + k][i]
            if char == char[::-1]:
                stri = char

    print(f'#{test_case} {stri}')
