# 알파벳
# 세로 R칸, 가로 C칸 / 좌측 상단(1행 1열) 시작
# 인접한 네 칸 중 하나로 이동 가능 - 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과 달라야함
# 말이 최대한 몇 칸을 지날 수 있는지 구하라

# DFS
# 백트래킹
# 선택 : 하나의 선택지 선택
# 검사(조건문) : 이 선택이 유효한지 확인
# 이동 및 복구 : 유효하다면 더 깊은 단계로 진행 / 탐색 완료 혹은 유효하지 않은 선택이라면 방금한 선택 취소 (이전 상태로 돌아가기)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5) # 재귀 깊이 (Recursion Error 방지)

r, c = map(int, input().split())

# 시간 초과 -> not in 때문인듯
# board = [list(input().strip()) for _ in range(r)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# max_ans = 0
# history = [] # 지나온 알파벳 담을 배열

# def dfs(x,y):
#     global max_ans # 함수 안에서 함수 밖의 변수 값을 직접 수정하고 싶을 때
#     max_ans = max(max_ans, len(history))

#     if max_ans == 26:
#         return

#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]

#         if 0 <= nx < r and 0 <= ny < c:
#             if board[nx][ny] not in history:
#                 history.append(board[nx][ny])
#                 dfs(nx,ny)
#                 history.pop() # 해당 길을 갔다가 탐색이 모두 끝나면 그 알파벳 뺴고 다른 길 갈 준비

# history.append(board[0][0])
# dfs(0,0)

# print(max_ans)


# 시간 초과
# 문자를 아스키 번호로 미리 변환 (ord 반복 호출 방지)
# board = [list(map(lambda x: ord(x) - 65, input().strip())) for _ in range(r)]

# # 알파벳 방문 여부 체크 A~Z : 0~25
# visited = [False] * 26

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# max_ans = 0

# def dfs(x, y, count):
#     global max_ans
#     max_ans = max(max_ans, count) # 갱신

#     if max_ans == 26:
#         return

#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]

#         if 0 <= nx < r and 0 <= ny < c:
#             idx = board[nx][ny]
#             if not visited[idx]:
#                 visited[idx] = True # 방문
#                 dfs(nx, ny, count + 1) # 다음 칸으로 이동
#                 visited[idx] = False # 돌아오면 방문 표시 해제

# # 시작점
# visited[board[0][0]] = True
# dfs(0, 0, 1) # 시작점도 카운팅

# print(max_ans)


# bfs + set
# 같은 위치에 같은 알파벳 조합으로 도착한 상황을 하나로 묶음
board = [list(input().strip()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# set을 사용해 (x, y, 지금까지의 경로)를 저장
# 문자열은 그 자체로 값이 비교
q = set([(0, 0, board[0][0])])
max_ans = 1

while q:
    x, y, path = q.pop()
    max_ans = max(max_ans, len(path))
    
    if max_ans == 26: break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if board[nx][ny] not in path:
                q.add((nx, ny, path + board[nx][ny]))

print(max_ans)