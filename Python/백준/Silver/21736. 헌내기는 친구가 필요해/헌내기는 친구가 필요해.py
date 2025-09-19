# 헌내기는 친구가 필요해
# O: 빈 공간, X: 벽, I: 도연이, P: 사람

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
campus = [list(input().strip()) for _ in range(n)] # 공백 제거 후 한 글자씩

# 도연이 위치 찾기
x, y = 0, 0
for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            x, y = i, j

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

result = 0

def dfs(x, y):
    global result

    campus[x][y] = 'V'

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 안에 존재할 때
        if (0 <= nx < n) and (0 <= ny < m):
            if campus[nx][ny] == 'O':
                dfs(nx, ny)          # 그 주변을 계속 탐색
            elif campus[nx][ny] == 'P':
                result += 1
                campus[nx][ny] = 'V' # 방문처리
                dfs(nx, ny)

dfs(x, y)

if result == 0:
    print("TT")
else:
    print(result)