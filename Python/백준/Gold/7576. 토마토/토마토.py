# 토마토
# 모든 토마토가 익을 때까지 최소 날짜 출력
# 1: 익은 토마토 / 0: 익지 않은 토마토 / -1: 토마토 없는 칸

import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

queue = deque()

# 익은 토마토가 들어있는 칸을 모두 큐에 넣음
for y in range(n):
    for x in range(m):
        if box[y][x] == 1:
            queue.append((x,y))

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if box[ny][nx] == 0:
                box[ny][nx] = box[y][x] + 1 # 안 익은 토마토면 날짜 갱신
                queue.append((nx,ny))

result = 0
for y in range(n):
    for x in range(m):
        if box[y][x] == 0: # bfs 탐색을 마쳤는데도 안 익은 토마토가 남아있으면 -1
            print(-1)
            sys.exit(0)

        result = max(result, box[y][x])

print(result - 1)