c = int(input())  # 컴퓨터(노드) 수
n = int(input())  # 연결 쌍 개수
edges = [list(map(int, input().split())) for _ in range(n)]

# 인접 행렬 생성
graph = [[0]*(c+1) for _ in range(c+1)]
for a, b in edges:
    graph[a][b] = 1   # graph[i][j] = 1이면 i와 j가 연결되었다고 표시
    graph[b][a] = 1   # 양방향 연결

from collections import deque

def bfs(start):
    visited = [False] * (c+1)
    queue = deque([start])
    visited[start] = True

    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for nxt in range(1, c+1):   # 1번부터 c번까지 탐색
            if graph[node][nxt] == 1 and not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

    return len(result) - 1

# 실행
print(bfs(1))