# 쉬운 최단거리
# 모든 지점에 대해서 목표지점까지의 거리

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# 0: 갈 수 없는 땅, 1: 갈 수 있는 땅, 2: 목표 지점

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    visited = [[-1] * m for _ in range(n)] # 방문하지 않은 곳 = -1
    queue = deque([(x,y)])
    visited[x][y] = 0 # 현재 위치는 0으로 
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 0 and visited[nx][ny] == -1: # 갈 수 있는 곳(1,2)이고 방문하지 않은 곳
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))

    return visited # 전체 배열 리턴


# 각 좌표에서 목표지점까지의 거리 = 목표지점에서 각 좌표까지의 거리이므로
# 2인 좌표를 찾아서 해당 좌표에서 bfs 탐색을 하면 visited 배열에 [목표지점에서 각 좌표까지의 거리] 정보를 담을 수 있음
for a in range(n):
    for b in range(m):
        if graph[a][b] == 2:
            result = bfs(a,b)

# 도달하지 못한 곳들(result에서 -1) 중 원래 갈 수 없었던 땅(graph에서 0)은 0으로 바꿔줌
for a in range(n):
    for b in range(m):
        if graph[a][b] == 0:
            result[a][b] = 0

for row in result:
    print(*row)

# 실제로는 이렇게 변환됨:
# print(row[0], row[1], row[2], row[3])