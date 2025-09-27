# 케빈 베이컨의 6단계 법칙
# 케빈 베이컨 수가 최소인 사람 찾기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# n : 유저의 수 / m : 관계의 수
rel = [list(map(int, input().split())) for _ in range(m)]

# 인접 행렬로 친구 관계 표현하기
graph = [[0] * (n+1) for _ in range(n+1)]
for a, b in rel:
    graph[a][b] = 1 # 1이면 a와 b는 친구사이, 0이면 모르는 사이
    graph[b][a] = 1

from collections import deque

def bfs(start):
    visited = [-1] * (n+1) # 방문하지 않았을 때 -1
    queue = deque([start])
    visited[start] = 0 # 방문했으면 0

    while queue:
        node = queue.popleft()
        for nxt in range(1, n+1):
            if graph[node][nxt] == 1 and visited[nxt] == -1: # 방문하지 않은 노드 중 연결된 노드
                visited[nxt] = visited[node] + 1 # visited[n] : start와 n 사이의 거리  (만나기 위해 몇 단계를 거쳐야하는지)
                queue.append(nxt)

    return sum(visited[1:]) # 다른 노드까지의 거리의 합 (케빈베이컨의 수)

min_kb = sys.maxsize
result = -1

# 만약 케빈베이컨 수가 같으면 숫자가 작은 사람을 출력해야하므로
# n부터 1까지 내림차순으로 탐색하여 더 작은 수로 갱신되게끔 구현
for i in range(n, 0, -1):
    kb_sum = bfs(i)
    if kb_sum <= min_kb: # 케빈베이컨의 수를 최소로 갱신
        min_kb = kb_sum
        result = i # 최소인 케빈베이컨의 수를 갖는 사람 갱신

print(result)