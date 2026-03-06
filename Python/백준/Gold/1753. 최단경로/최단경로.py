# 최단경로
# 시작점에서 다른 모든 정점으로의 최단 경로 구하기
# 정점의 개수 : V / 간선의 개수 : E / 시작 정점의 번호 : K
# u에는 v로 가는 가중치 w인 간선이 존재

# BFS 한계: 모든 간선의 가중치가 동일할 때만 최단 경로 보장
# 다익스트라: BFS 확장판. 무조건 먼저 도달하는 순서가 아니라, 현재까지 발견된 경로 중 가장 비용이 적은 순서
# heapq: 배열은 매번 누가 제일 짧은지를 찾기 위해 전체를 훑어야함. 그러나 heapq는 데이터 넣을 때 자동 정렬

import sys
input = sys.stdin.readline
import heapq

INF = int(1e9) # 무한대 설정

v, e = map(int, input().split())
k = int(input()) # 시작 정점의 번호
graph = [[] for _ in range(v+1)] # 각 인덱스 = 출발 노드에 (목적지, 가중치) 추가
for _ in range(e):
    u, n_v, w = map(int, input().split())
    graph[u].append((n_v, w)) # u번 정점에서 (목적지, 가중치) 형태로 저장

# 각 인덱스번호까지의 최단 경로 배열
dist = [INF] * (v + 1)

def dijkstra(start):
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

dijkstra(k)

# 모든 정점으로 가기 위한 최단 거리 출력
for i in range(1, v+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
