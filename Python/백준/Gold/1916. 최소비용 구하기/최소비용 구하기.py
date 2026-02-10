# 최소비용 구하기
# a번째 도시에서 b번째 도시까지 가는데 드는 최소 비용

import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())  # 도시 개수
m = int(input())  # 버스 개수

# # 간선 정보 저장
# edges = []
# for _ in range(m):
#     a, b, cost = map(int, input().split())
#     edges.append((a, b, cost))

# start, end = map(int, input().split())

# # 거리 테이블 초기화
# distance = [INF] * (n + 1)
# distance[start] = 0

# # 모든 간선 확인
# for i in range(n - 1):
#     for a, b, cost in edges:
#         # 출발 도시를 방문한 적이 있고, 더 짧은 경로를 발견하면 (다른 노드를 거쳐 오는게 더 빠른지)
#         if distance[a] != INF and distance[a] + cost < distance[b]:
#             distance[b] = distance[a] + cost # 갱신

# print(distance[end])


import heapq

# graph[출발도시] = [(도착도시1, 비용1), (도착도시2, 비용2), ...]
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost)) # 단방향 그래프 (a->b만 가능, b->a는 따로 입력)

start, end = map(int, input().split())

# distance[i] = 시작 도시에서 i번 도시까지 가는 최소 비용
distance = [INF] * (n + 1)
distance[start] = 0

# heapq: 자동으로 최소값이 앞에 오는 리스트
heap = []
heapq.heappush(heap, (0, start))  # (비용 0, 시작도시)를 힙에 추가

while heap:
    current_cost, current_city = heapq.heappop(heap)  # 가장 비용이 적은 경로를 꺼냄
    
    # 현재 비용보다 더 저렴한 비용의 경로가 있다면 skip
    if current_cost > distance[current_city]:
        continue
    
    # 현재 도시에서 갈 수 있는 모든 인접 도시 확인
    for next_city, bus_cost in graph[current_city]:
        new_cost = current_cost + bus_cost
        # (시작점->현재도시 비용) + (현재도시->다음도시 비용)
        
        # 새로운 경로가 기존에 알고 있던 경로보다 저렴한가?
        if new_cost < distance[next_city]:
            distance[next_city] = new_cost # 최소 비용 업데이트
            heapq.heappush(heap, (new_cost, next_city)) # 힙에 추가

print(distance[end])