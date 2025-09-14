# dfs & bfs

n,m,v = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# n: 정점, m: 간선, v: 탐색 시작하는 정점 번호

# 인접 행렬 - 2606 바이러스 참고
graph = [[0]*(n+1) for _ in range(n+1)]
for a, b in edges:
    graph[a][b] = 1   # graph[i][j] = 1이면 i와 j가 연결되었다고 표시
    graph[b][a] = 1   # 양방향 연결

def dfs(start, visited):
    visited[start] = True
    print(start, end=" ")

    for nxt in range(1, n+1): # 현재 낸 node와 (1~n)노드가 연결되었는지 탐색
        if graph[start][nxt] == 1 and not visited[nxt]: # 연결되어있고 방문하지 않았다면
            visited[nxt] = True
            dfs(nxt, visited) # nxt 노드와 연결된 다른 노드 탐색 (재귀)

# bfs - 2606 바이러스 참고
from collections import deque

def bfs(start):
    visited = [False] * (n+1)
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for nxt in range(1, n+1): # 현재 낸 node와 (1~n)노드가 연결되었는지 탐색
            if graph[node][nxt] == 1 and not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

visited = [False] * (n+1) # 방문 정보 저장 배열 # dfs에서만 사용
dfs(v, visited)
print()
bfs(v)

# dfs는 재귀호출이기 때문에 visited가 누적되어야하는데, bfs는 한 번 정의하고 while 안에서 계속 탐색해서 인자로 넘겨줄 필요 x