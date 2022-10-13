import sys
sys.stdin = open('raser.txt')

T = int(input())
for test_case in range(1, T + 1):
    arr = input()
    cnt = 0
    stick = 0
    for i in range(len(arr)):
        if arr[i] == '(':
            stick += 1
        else:
            stick -= 1
            if arr[i - 1] == '(':
                cnt += stick
            else:
                cnt += 1

    print(f'#{test_case} {cnt}')