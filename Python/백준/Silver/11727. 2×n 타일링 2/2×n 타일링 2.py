n = int(input())

dp = [0] * (max(n+1,3)) # dp[n] : 2xn 크기를 채우는 방법의 수

dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2] * 2 # (총 3개의 경우의 수가 있는데, 하나는 dp[i-1]과 겹침)

print(dp[n] % 10007)