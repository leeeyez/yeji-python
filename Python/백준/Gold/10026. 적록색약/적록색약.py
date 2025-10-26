# 적록색약
# 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
paint = [list(input().strip()) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
visited = [[False] * n for _ in range(n)]

def bfs(x,y):
    queue = deque([(x,y)])
    visited[y][x] = True
    color = paint[y][x] # 현재 좌표의 색 저장

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if paint[ny][nx] == color and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((nx,ny))
cnt = 0
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            bfs(x,y)
            cnt += 1

# 적록색약인 경우
for y in range(n):
    for x in range(n):
        if paint[y][x] == 'G': # 초록색을 빨간색으로 바꿔버림
            paint[y][x] = 'R'

# visited 다시 초기화
visited = [[False] * n for _ in range(n)]
rgcnt = 0
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            bfs(x,y)
            rgcnt += 1

print(f'{cnt} {rgcnt}')