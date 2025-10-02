# 경로 찾기
# 모든 정점 (i, j)에 대해서, i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 구하기

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]

# (i,j)는 i부터 j까지 경로 존재 여부를 의미
result = [[0] * n for _ in range(n)]

def bfs(start):
    visited = [False] * n
    queue = deque([start])
    # visited[start] = True # 자기 자신으로 돌아오는 경로도 탐색해야하므로 방문처리 제외

    while queue:
        node = queue.popleft()

        for nxt in range(n):
            if info[node][nxt] == 1 and not visited[nxt]:  # 연결되어있고 방문하지 않은 노드
                visited[nxt] = True
                result[start][nxt] = 1  # start에 대해 탐색 중이므로 start부터 nxt까지 연결되어있음을 표시
                queue.append(nxt)
        

for i in range(n):
    bfs(i)

for row in result:
    print(' '.join(map(str, row)))