# 미로 탐색
# (1,1)에서 (n,m) 이동 시 지나야 하는 최소 칸의 개수

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
maze = [[int(x) for x in input().strip()] for _ in range(n)] # 개행문자 무시

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x, y):
    visited = [[-1] * m for _ in range(n)] # 방문 안 했으면 -1
    queue = deque([(y,x)])
    visited[y][x] = 1 # 방문했으면 1 (칸 개수에 포함시켜야함)

    while queue:
        y, x = queue.popleft()

        # 마지막 칸에 도달하면 지나온 칸의 개수를 출력하고 break
        if y == n-1 and x == m-1:
            print(visited[y][x])
            break

        for i in range(4):
            # 상하좌우로 움직이기
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n: # 범위 안에 있는지 확인
                if maze[ny][nx] == 1 and visited[ny][nx] == -1: # 이동 가능한 칸(1)이고 방문하지 않은 칸인지 확인
                    visited[ny][nx] = visited[y][x] + 1 # 이전 칸까지의 이동 개수 + 1
                    queue.append((ny,nx))

                    
bfs(0,0)