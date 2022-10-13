import sys
sys.stdin = open('pizza.txt')

from collections import deque

def pizza():
    q = deque()
    for i in range(1, N + 1):
        q.append(i)

    idx = N + 1     # 아직 화덕에 넣지 않은 첫번쨰 피자
    while len(q) > 1:
        tmp = q.popleft()
        arr[tmp] = arr[tmp] // 2    # 치즈 반으로 줄이기
        # 치즈가 남아 있으면 -> q에 넣기
        if arr[tmp] != 0:
            q.append(tmp)
        # 치즈가 다 녹았을때 -> 총 피자수 확인
        elif idx <= M:
            q.append(idx)
            idx += 1
    return q[0]


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [0] + list(map(int, input().split()))

    print(f'#{test_case} {pizza()}')
