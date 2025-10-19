# 토마토
# 며칠이 지나면 다 익게 되는지 최소 일수
# 1: 익은 토마토 / 0: 익지 않은 토마토 / -1: 토마토 없는 칸

import sys
from collections import deque
input = sys.stdin.readline

m,n,h = map(int, input().split())

# 3차원 배열
box = []
for _ in range(h):
    floor = [list(map(int, input().split())) for _ in range(n)]
    box.append(floor)

dx = [0,0,-1,1,0,0]
dy = [-1,1,0,0,0,0]
dz = [0,0,0,0,-1,1]

# 1차 시도 틀린 이유 - 각 익은 토마토마다 bfs()를 따로 돌림 -> 동시 전파 X 로직 상의 문제
# 익은 날짜를 저장할 배열
# -1: 방문 X / 0: 원래 익어있었음 / 1~: 익은 날짜
# visited = [[[-1 for _ in range(m)] for _ in range(n)] for _ in range(h)]

# def bfs(x,y,z): # 익은 토마토에서 bfs 탐색
#     queue = deque([(x, y, z)])
#     visited[z][y][x] = 0  # 시작점 (익은 토마토) 방문 표시

#     while queue:
#         x, y, z = queue.popleft()

#         for i in range(6):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             nz = z + dz[i]

#             if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h: # 범위 안에 있는지 확인
#                 # 안 익은 토마토 중에 아직 방문 안 한 곳
#                 if box[nz][ny][nx] == 0 and visited[nz][ny][nx] == -1:
#                     visited[nz][ny][nx] = visited[z][y][x] + 1 # 익음을 전파 (날짜 + 1)
#                     box[nz][ny][nx] = 1  # 익음 표시
#                     queue.append((nx, ny, nz))


# # 방문하지 않은 곳 중 익은 토마토에서 bfs 탐색 시작
# for z in range(h):
#     for y in range(n):
#         for x in range(m):
#             if box[z][y][x] == 1 and visited[z][y][x] == -1:
#                 bfs(x, y, z)

# result = 0
# for z in range(h):
#     for y in range(n):
#         for x in range(m):
#             if box[z][y][x] == 0: # 모든 탐색 이후에도 안 익은 토마토가 있다면 -1 출력
#                 print(-1)
#                 sys.exit(0)
#             if visited[z][y][x] > result: # 모든 토마토가 익은 날짜로 갱신
#                 result = visited[z][y][x]

# print(result)


queue = deque()

# 방문 배열을 따로 둘 필요 없음 (box 값으로 판별 가능)
# 처음부터 익은 토마토(1) 모두 큐에 추가
for z in range(h):
    for y in range(n):
        for x in range(m):
            if box[z][y][x] == 1:
                queue.append((x, y, z))

# bfs
while queue:
    x, y, z = queue.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
            if box[nz][ny][nx] == 0:  # 안 익은 토마토면
                box[nz][ny][nx] = box[z][y][x] + 1  # 날짜 갱신
                queue.append((nx, ny, nz))

# 결과 계산
result = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if box[z][y][x] == 0: # 모든 탐색 이후에도 안 익은 토마토가 있다면 -1 출력
                print(-1)
                sys.exit(0)
            result = max(result, box[z][y][x])

print(result - 1)  # 처음 익은 토마토가 1이므로 -1 보정