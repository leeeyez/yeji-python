# 숨바꼭질
# 수빈이 동생을 찾을 수 있는 가장 빠른 시간

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
# n : 수빈 위치 / m : 동생 위치

def bfs(start):
    visited = [-1] * (100001) # 방문 안하면 -1
    queue = deque([start])
    visited[start] = 0 # 방문하면 0

    while queue:
        node = queue.popleft()

        if node == m:  # 가장 먼저 동생 위치 m에 도달하는 시간 출력 후 break
            print(visited[node])
            break

        # 뒤로 걷는 경우
        if 0 <= node-1 <= 100000 and visited[node-1] == -1:
            visited[node-1] = visited[node] + 1 # visited[n] : start부터 n까지 이동하는데 걸리는 최소 시간
            queue.append(node-1)
        
        # 앞으로 걷는 경우
        if 0 <= node+1 <= 100000 and visited[node+1] == -1:
            visited[node+1] = visited[node] + 1 # 1초 소모
            queue.append(node+1)

        # 앞으로 2배만큼 순간이동하는 경우
        if 0 <= node*2 <= 100000 and visited[node*2] == -1:
            visited[node*2] = visited[node] + 1 # 1초 소모
            queue.append(node*2)

bfs(n)