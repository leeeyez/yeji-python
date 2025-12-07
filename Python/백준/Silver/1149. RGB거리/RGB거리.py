# RGB거리
# N개의 집을 빨강, 초록, 파랑 중 하나의 색으로 칠하는 비용의 최솟값

# 1번 집의 색 != 2번 집의 색
# N번 집의 색 != N-1번 집의 색
# i번 집의 색 != i-1번, i+1번 집의 색

import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j] : i번째 집을 j색으로 칠할 때까지의 최소 비용 (이미 1~i-1번째까지는 다 칠한 상황)
# j : 0=빨강, 1=초록, 2=파랑
dp = [[0] * 3 for _ in range(n)]

# 1번째 집
dp[0][0] = cost[0][0] # 빨
dp[0][1] = cost[0][1] # 초
dp[0][2] = cost[0][2] # 파

# 두 번째 집부터
for i in range(1, n):
    # i번째 집을 빨가으로 칠하는 경우
    # 이전 집은 초 or 파
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]

    # i번째 집을 초록으로 칠하는 경우
    # 이전 집은 빨 or 파
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]

    # i번째 집을 파랑으로 칠하는 경우
    # 이전 집은 빨 or 초
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

# 마지막 집까지 칠한 후 최소값
print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))