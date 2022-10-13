import heapq


def dijkstra(x, y):
    # 출발점 설정
    heap = []
    D[x][y] = 0
    heapq.heappush(heap, (D[x][y], x, y))   # 가중치, x, y
    # N x N 만큼 반복
    # for _ in range(N * N):
    while heap:
        # 최소값
        # min_value = INF
        # for i in range(N):
        #     for j in range(N):
        #         if visited[i][j] == 0 and D[i][j] < min_value:
        #             min_value = D[i][j]
        #             x, y = i, j
        d, x, y = heapq.heappop(heap)
        # 방문체크
        visited[x][y] = 1
        if x == N - 1 and y == N - 1:  # 도착지점에 도착
            return
        # 인접정점 갱신
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 인접하고 방문 안한 정점
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                diff = 0
                if arr[nx][ny] > arr[x][y]:     # 오르막일때
                    diff = arr[nx][ny] - arr[x][y]
                if D[nx][ny] > D[x][y] + 1 + diff:  # 갱신
                    D[nx][ny] = D[x][y] + 1 + diff
                    heapq.heappush(heap, (D[nx][ny], nx, ny))


INF = 987654321
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    D = [[INF] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    dijkstra(0, 0)
    print(f'#{test_case} {D[N - 1][N - 1]}')
