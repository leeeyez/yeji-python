# 트리의 부모 찾기
# 각 노드의 부모 구하기 (루트는 1)

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
edges = [list(map(int, input().split())) for _ in range(n-1)]

# 인접행렬 방식 : 메모리 초과 (인접 노드를 찾기 위해 행렬의 모든 열 확인)
# graph = [[0]*(n+1) for _ in range(n+1)]
# for a,b in edges:
#     graph[a][b] = 1
#     graph[b][a] = 1

# parent = [0] * (n+1) # 각 노드(인덱스)별 부모 노드 기록

# def bfs(start):
#     queue = deque([start])

#     while queue:
#         node = queue.popleft()

#         for nxt in range(1, n+1):
#             if graph[node][nxt] == 1 and parent[nxt] == 0: # 연결되어있고, 부모가 아직 0일떄
#                 parent[nxt] = node
#                 queue.append(nxt)

# bfs(1)

# for i in range(2, n+1):
#     print(parent[i])

# ------------------------------------------------------

# 인접 리스트 방식
graph = [[] for _ in range(n+1)]
for a,b in edges:
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n+1)

def bfs(start):
    queue = deque([start])
    parent[start] = 0 # 최상위 노드인 1의 부모는 자기 자신이므로 0

    while queue:
        node = queue.popleft() # 현재 부모 노드

        # 연결된 모든 노드 탐색
        for nxt in graph[node]:
            if parent[nxt] == 0: # 아직 부모가 정해지지 않았으면 node가 부모
                parent[nxt] = node
                queue.append(nxt)

bfs(1)

for i in range(2, n+1):
    print(parent[i])