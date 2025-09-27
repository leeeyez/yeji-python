# 단지번호 붙이기
# 단지 수, 각 단지별 집의 수(오름차순)

import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) # 지도의 크기
map = [[int(x) for x in input().strip()] for _ in range(n)] # 개행문자 무시

dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 방문 처리 배열을 전역변수로 선언
visited = [[-1] * (n) for _ in range(n)] # 방문 안했으면 -1

def bfs(x,y):
    queue = deque([(x,y)])
    visited[x][y] = 0 # 방문하면 0

    h_cnt = 1 # 단지 내의 집 개수

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n: # 범위 내에 있을 떄
                if map[nx][ny] == 1 and visited[nx][ny] == -1: # 1이고(집이 있고) 방문하지 않았을 때
                    visited[nx][ny] = 0
                    queue.append((nx,ny))
                    h_cnt += 1

    return h_cnt

cnt = 0    # 총단지의 개수
house = [] # 단지별 집의 개수를 담을 배열

for a in range(n):
    for b in range(n):
        if map[a][b] == 1 and visited[a][b] == -1: # 집이 있고 방문하지 않았을 때 bfs 탐색
            house.append(bfs(a,b))
            cnt += 1

house.sort()

print(cnt)
for h in house:
    print(h)


# DFS로 풀기
# sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 늘리기
# def dfs(x,y):
#     visited[x][y] = 0 # 방문 처리
#     h_cnt = 1 # 현재 집 포함한 단지 내 집의 개수

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0 <= nx < n and 0 <= ny < n:
#             if map[nx][ny] == 1 and visited[nx][ny] == -1:
#                 visited[nx][ny] = 0
#                 h_cnt += dfs(nx, ny) # 재귀로 연결된 집들 탐색

#     return h_cnt

# cnt = 0    # 총단지의 개수
# house = [] # 단지별 집의 개수를 담을 배열

# for a in range(n):
#     for b in range(n):
#         if map[a][b] == 1 and visited[a][b] == -1: # 집이 있고 방문하지 않았을 때 bfs 탐색
#             house.append(dfs(a,b))
#             cnt += 1

# house.sort()

# print(cnt)
# for h in house:
#     print(h)