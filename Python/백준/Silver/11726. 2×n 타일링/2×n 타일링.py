n = int(input())

dp = [0] * (max(n+1,3)) # dp[n] : 2xn 크기를 채우는 방법의 수

dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)