# 뱀과 사다리 게임 (1번 -> 100번)
# 100번 칸에 도착하기 위해 주사위를 굴려야 하는 횟수의 최솟값

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split()) # n = 사다리 수 / m = 뱀의 수
ladder = [list(map(int, input().split())) for _ in range(n)]
snake = [list(map(int, input().split())) for _ in range(m)]

# 게임 보드 만들기 (아무것도 없으면 0, 뱀이나 사다리 있으면 이동하는 칸을 원소로)
board = [0] * 101
for start, end in ladder:
    board[start] = end
for start, end in snake:
    board[start] = end
visited = [-1] * 101 # 미방문은 -1


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 0 # 방문은 0

    while queue:
        node = queue.popleft()

        if node == 100: # 100번째 노드이면 visited[100] 반환
            return visited[100]

        # 주사위 돌리기
        for dice in range(1,7):
            nxt = node + dice # 현재 노드 + 주사위 번호

            if nxt <= 100: # 이동한 칸이 100번 안
                if board[nxt] != 0: # 뱀이나 사다리가 있으면 이동
                    nxt = board[nxt]

                if visited[nxt] == -1: # 방문하지 않았던 곳이면 횟수 갱신
                    visited[nxt] = visited[node] + 1
                    queue.append(nxt)

    return visited[100]

print(bfs(1))