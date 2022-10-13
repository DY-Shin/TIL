import sys
sys.stdin = open('elecbus.txt')

def elecbus(arr, k , n, m):
    arr = [0] + arr + [n]
    last = 0  # 마지막 충전한 충전소 번호
    cnt = 0  # 충전 횟수

    for i in range(1, m + 2):
        # 충전기 사이가 K보다 크면 충전할 수 없음
        if arr[i] - arr[i - 1] > k:
            return 0
        # 충전할 수 없는 경우 앞쪽에서 충전해야 함
        if arr[i] > last + k:
            last = arr[i - 1]
            cnt += 1
    return cnt

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # K : 최대 이동할 수 있는 거리 N : 종점 M : 충전기가 설치된 개수
    K, N, M = map(int, input().split())

    bus_stop = list(map(int, input().split()))

    print(f'#{test_case} {elecbus(bus_stop, K, N, M)}')