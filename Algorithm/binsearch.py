import sys
sys.stdin = open('binsearch.txt')

T = int(input())


def binsearch(p, pa):
    l = 1
    r = p
    c = int((l + r) / 2)
    cnt = 0
    while c:
        if pa > c:
            l = c
            c = int((l + r) / 2)
            cnt += 1
        elif pa < c:
            r = c
            c = int((l + r) / 2)
            cnt += 1
        else:
            break
    return cnt


for test_case in range(1, T + 1):
    p, pa, pb = map(int, input().split())

    cnt_a = binsearch(p, pa)
    cnt_b = binsearch(p, pb)

    if cnt_a > cnt_b:
        print(f'#{test_case} B')
    elif cnt_a < cnt_b:
        print(f'#{test_case} A')
    else:
        print(f'#{test_case} 0')