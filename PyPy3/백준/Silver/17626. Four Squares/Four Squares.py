import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1) # dp[n] : n을 만드는 제곱수 개수의 최소 개수
# dp[1] = 1 # 1^2
# dp[2] = 2 # 1^2 + 1^2
# dp[3] = 3 # 1^2 + 1^2 + 1^2
# dp[4] = 1 # 2^2

for i in range(1, n+1):
    dp[i] = i  # 최악의 경우 1^2을 i번 쓰는 경우 (i개)
    for j in range(1, int(i**0.5)+1):
        # i를 만들 때 마지막에 쓴 한 개의 제곱수가 j*j라고 생각하면, 남은 값은 i - j*j
         # 그걸 최적으로 만드는 개수는 dp[i - j*j]
         # 마지막으로 쓴 j*j 하나를 포함해서 dp[i - j*j] + 1
        dp[i] = min(dp[i], dp[i - j*j] + 1)
        j += 1

print(dp[n])