import sys

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# dp[상태][r][c] -> 상태: 0(가로), 1(세로), 2(대각선)
dp = [[[0] * n for _ in range(n)] for _ in range(3)]

# 시작점 (0, 1)에 가로로 놓여있음
dp[0][0][1] = 1

for r in range(n):
    for c in range(2, n): # 0, 1열은 이미 처리됨
        if board[r][c] == 1:
            continue
            
        # 1. 가로로 오는 경우
        dp[0][r][c] = dp[0][r][c-1] + dp[2][r][c-1]
        
        # 2. 세로로 오는 경우
        if r - 1 >= 0:
            dp[1][r][c] = dp[1][r-1][c] + dp[2][r-1][c]
            
        # 3. 대각선으로 오는 경우 (주변 3칸 확인 필수)
        if r - 1 >= 0 and board[r-1][c] == 0 and board[r][c-1] == 0:
            dp[2][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]

# 모든 상태의 합 출력
print(dp[0][n-1][n-1] + dp[1][n-1][n-1] + dp[2][n-1][n-1])