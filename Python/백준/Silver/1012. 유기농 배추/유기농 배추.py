# 배추를 해충으로 보호하는 배추흰지렁이 : 해충을 잡아 먹으면서 배추 보호
# 어떤 배추에 배추흰지렁이가 살고 있으면 이 지렁이는 인접한 다른 배추로 이동 가능
# 인접 = 상하좌우 네 방향에 다른 배추가 위치한 경우
# => 결국 뭉쳐있는 덩어리 개수

# dfs & bfs

# 런타임 에러 : 재귀 최대 깊이 설정하기
import sys
sys.setrecursionlimit(10**6)

t = int(input())

# 상하좌우 탐색 배열
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 안에 존재하고, 아직 방문하지 않은 배추일 때
        if (0 <= nx < m) and (0 <= ny < n) and loc[ny][nx] == 1:
            loc[ny][nx] = -1     # 방문 처리
            dfs(nx, ny)          # 그 배추 주변을 계속 탐색

for _ in range(t):
    m, n, k = map(int, input().split())
    loc = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        loc[y][x] = 1 # x(가로), y(세로)이므로 2차원 배열 표기시 위치 바꿔 표기

    cnt = 0
    for a in range(m):
        for b in range(n):
            if loc[b][a] == 1:
                dfs(a,b)
                cnt += 1

    print(cnt)


# from collections import deque

# def bfs(x,y):
#     queue = deque()
#     queue.append((x,y))
#     loc[y][x] = -1 # 방문 처리

#     while queue:
#         cx, cy = queue.popleft()
#         for i in range(4):
#             nx = cx + dx[i]
#             ny = cy + dy[i]
#             # 범위 안이고, 아직 방문 안 한 배추(=1)라면
#             if 0 <= nx < m and 0 <= ny < n and loc[ny][nx] == 1:
#                 loc[ny][nx] = -1
#                 queue.append((nx, ny))


# bfs: nx,ny로 네 방향 모두 확인하고 큐에 넣음 -> 큐에 있는 것들을 하나씩 빼서 또 네방향 확인 후 넣음 -> 반복
# dfs: nx.ny로 일단 한 방향 확인 -> 조건 만족 시 그 칸에서 또 dfs(재귀) -> 모든 방향 동일하게 진행