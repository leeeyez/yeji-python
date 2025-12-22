# 스티커
# 점수의 합이 최대가 되면서 서로 변을 공유하지 않는 스티커 집합

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    # dp[i][n] == n열에서 i행 스티커를 마지막으로 골랐을 때의 최대합
    dp = [[0] * n for _ in range(2)]

    # 스티커 길이가 1인 경우 : 위, 아래 중 큰 점수 스티커 고르기
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue

    # 스티커 길이가 2인 경우 : 대각선 스티커 + 자기자신
    dp[0][1] = arr[1][0] + arr[0][1]
    dp[1][1] = arr[0][0] + arr[1][1]
    if n == 2:
        print(max(dp[0][1], dp[1][1]))
        continue

    # 스티커 길이가 3 이상인 경우 :
    # ex. [0][i] 선택 시
    # 1. [0][i](자기자신) + 이전 대각선 스티커까지의 합 (dp[1][i-1])
    # 2. [0][i](자기자신) + 이전이전 대각선 스티커까지의 합 (dp[1][i-2])
    for i in range(2, n):
        dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + arr[0][i]
        dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + arr[1][i]

    print(max(dp[0][-1], dp[1][-1]))
