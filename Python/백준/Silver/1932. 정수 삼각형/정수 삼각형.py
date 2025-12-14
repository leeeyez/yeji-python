# 정수 삼각형
# 선택한 수의 합이 최대가 되는 경로 구하기

import sys
input = sys.stdin.readline

n = int(input())
tree = [list(map(int, input().split())) for _ in range(n)]

# dp[i][i] : i번쨰 줄 j번째 수까지 합한 최대값
dp = [[0] * (i+1) for i in range(n)]
dp[0][0] = tree[0][0]

for i in range(1, n):
    for j in range(len(tree[i])):
        # 왼쪽 위에서 내려오는 경우
        if j == 0:
            left = 0
        else:
            left = dp[i-1][j-1]
        
        # 오른쪽 위에서 내려오는 경우
        if j == len(tree[i-1]):
            right = 0
        else:
            right = dp[i-1][j]
        
        dp[i][j] = tree[i][j] + max(left, right) # left, right 중 최대값 더하기

# 마지막 줄에서 최댓값 찾기
print(max(dp[n-1]))