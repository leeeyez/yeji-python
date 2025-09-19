# 연결 요소의 개수

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split()) # n: 정점의 개수 / m: 간선의 개수
edges = [list(map(int, input().split())) for _ in range(m)]

graph = [[0]*(n+1) for _ in range(n+1)]
for a,b in edges:
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(start, visited):
    visited[start] = True

    for nxt in range(1, n+1): # 현재 낸 node와 (1~n)노드가 연결되었는지 탐색
        if graph[start][nxt] == 1 and not visited[nxt]: # 연결되어있고 방문하지 않았다면
            visited[nxt] = True
            dfs(nxt, visited) # nxt 노드와 연결된 다른 노드 탐색 (재귀)


cnt = 0
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i]:   # 방문 안 한 노드만 탐색
        dfs(i, visited)
        cnt += 1         # 연결된 모든 노드를 방문하면 +1

print(cnt)