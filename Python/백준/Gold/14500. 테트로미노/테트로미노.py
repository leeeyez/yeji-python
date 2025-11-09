# 테트로미노
# 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # 재귀 깊이 설정

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
max_val = 0

# 상, 하, 좌, 우 방향
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# DFS로 4칸 연결된 도형 (4가지) 탐색 -> ㅗ 모양 빼고
def dfs(r, c, depth, total_sum):
    global max_val
    if depth == 4: # 깊이가 4이면 max val 갱신 or 유지
        max_val = max(max_val, total_sum)
        return

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        
        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc, depth + 1, total_sum + board[nr][nc])
            visited[nr][nc] = False # 방문 처리 제거

# ㅗ 모양만 따로 계산하는 함수
def check_t_mino(r, c):
    global max_val
    
    # 상(1), 하(2), 좌(3), 우(4) 4방향을 탐색
    # 중심 (r, c)를 제외한 주변 4칸의 값
    around = []
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            around.append(board[nr][nc])
    
    # 주변 칸이 3개 이상일 때만 ㅗ 모양을 만들 수 있음
    if len(around) >= 3:
        current_sum = board[r][c] # 중심 칸의 값
        
        # ㅗ는 중심 칸 + 주변 4칸 중 3칸의 합
        # 4칸의 합을 구한 후, 가장 작은 1칸을 빼는 것이 가장 간단함
        # ㅗ ㅏ ㅜ ㅓ 중에 하나 고르기
        if len(around) == 4:
            current_sum += sum(around) - min(around)
        
        # 주변 칸이 3개일 때 (가장자리)
        elif len(around) == 3:
            current_sum += sum(around)
        
        max_val = max(max_val, current_sum)


# 모든 칸을 시작점으로 완전 탐색
for r in range(n):
    for c in range(m):
        # DFS로 ㅗ를 제외한 4가지 모양 탐색
        visited[r][c] = True
        dfs(r, c, 1, board[r][c])
        visited[r][c] = False
        
        # ㅗ 모양 탐색
        check_t_mino(r, c)

print(max_val)