#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = 8
    arr = list(map(int, input().split()))

    for i in range(5):
        arr[0] -= 1