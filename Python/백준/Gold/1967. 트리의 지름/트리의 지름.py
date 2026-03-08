# 트리의 지름
# 루트가 있는 트리를 가중치가 있는 간섣늗롤 줄 때, 트리의 지름을 구해서 출력
# 트리의 지름 : 존재하는 모든 경로들 중에서 가장 긴 것

# DFS

# 아무 곳이나 잡고 위로 쭉 들어올리면 가장 끝자락에 있는 점(A) 하나를 찾을 수 있다.
# A점을 잡고 위로 쭉 들어올리면 반대편 끝자락에 가장 멀리 매달리는 점(B)가 생긴다.
# A와 B 사이의 거리가 지름

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5) # 재귀 깊이 (Recursion Error 방지)

n = int(input()) # 노드의 개수
graph = [[] for _ in range(n+1)] # 각 인덱스 = 출발 노드에 (목적지, 거리) 추가
for _ in range(n-1):
    u, n_v, w = map(int, input().split())
    graph[u].append((n_v, w)) # u번 정점에서 (목적지, 거리) 형태로 저장
    graph[n_v].append((u, w))

def dfs(node, d):
    for nxt, weight in graph[node]: # node랑 연결된 다른 노드 중에서
        if dist[nxt] == -1: # 방문하지 않은 노드라면
            dist[nxt] = d + weight # 현재 노드까지의 가중치 + 해당 노드까지의 가중치
            dfs(nxt, d + weight) # 연결된 다음 노드와 dfs 탐색

# 1. 임의의 노드(1번)에서 가장 먼 노드 찾기
dist = [-1] * (n+1)
dist[1] = 0
dfs(1,0)

# 1번에서 가장 먼 노드 찾기
farthest_node = dist.index(max(dist))

# 2. 그 노드에서 다시 가장 먼 노드 찾기
dist = [-1] * (n + 1)
dist[farthest_node] = 0
dfs(farthest_node, 0)

# 결과 출력 (최댓값이 곧 지름)
print(max(dist))