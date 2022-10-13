import sys
sys.stdin = open('tournament.txt')

def win(r1, r2):
    if arr[r1] == arr[r2]:
        return r1
    else:
        if arr[r1] == 1 and arr[r2] == 2:
            return r2
        elif arr[r1] == 1 and arr[r2] == 3:
            return r1
        elif arr[r1] == 2 and arr[r2] == 1:
            return r1
        elif arr[r1] == 2 and arr[r2] == 3:
            return r2
        elif arr[r1] == 3 and arr[r2] == 1:
            return r2
        elif arr[r1] == 3 and arr[r2] == 2:
            return r1

def game(left, right):
    if left == right:
        return left
    else:
        r1 = game(left, (left + right) // 2)
        r2 = game((left + right) // 2 + 1, right)
        return win(r1, r2)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    print(f'#{test_case} {game(1, N)}')
