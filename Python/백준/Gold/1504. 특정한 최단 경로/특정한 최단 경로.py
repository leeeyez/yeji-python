# 특정한 최단경로
# 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동
# 한번 이동했던 정점, 한번 이동했던 간선 다시 이동 가능

import sys
input = sys.stdin.readline
import heapq

INF = int(1e9) # 무한대 설정

n, e = map(int, input().split()) # 정점 N, 간선 E
graph = [[] for _ in range(n+1)] # 각 인덱스 = 출발 노드에 (목적지, 거리) 추가
for _ in range(e):
    u, n_v, w = map(int, input().split())
    graph[u].append((n_v, w)) # u번 정점에서 (목적지, 거리) 형태로 저장
    graph[n_v].append((u, w))

v1, v2 = map(int, input().split()) # 무조건 지나야하는 정점 2개

def dijkstra(start):
    # start부터 각 인덱스번호까지의 최단 경로 배열
    dist = [INF] * (n + 1)

    q = []
    heapq.heappush(q, (0, start)) # 시작 노로 가기 위한 최단 경로는 0 // q라는 리스트를 마치 '최소 힙'처럼 다루겠다
    # 튜플 형태를 힙에 넣으면, 첫 번째 요소(거리)를 기준으로 정렬
    dist[start] = 0

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        current_dist, now = heapq.heappop(q)

        # 해당 노드까지의 최단 경로가 현재 거리보다 짧으면 무시
        if dist[now] < current_dist:
            continue

        # 현재 노드와 연결된 다른 노드 확인
        for nxt_node, weight in graph[now]:
            cost = current_dist + weight # 해당 노드까지의 거리 + 다른 노드까지의 거리(가중치)
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우 갱신
            if cost < dist[nxt_node]:
                dist[nxt_node] = cost
                heapq.heappush(q, (cost, nxt_node))
    
    return dist


dist_from_1 = dijkstra(1) # 1번노드에서 시작했을 떄 다른 노드들까지의 최단거리
dist_from_v1 = dijkstra(v1) # v1번 노드에서 시작했을 때 ..
dist_from_v2 = dijkstra(v2) # v2번 노드에서 시작했을 떄 ..

# 1 -> v1 -> v2 -> n (1부터 v1까지의 최단거리 + v1부터 v2까지의 최단거리 + v2부터 n까지의 최단거리)
# 1 -> v2 -> v1 -> n
path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[n]
path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[n]

result = min(path1, path2)
print(result if result < INF else -1)
