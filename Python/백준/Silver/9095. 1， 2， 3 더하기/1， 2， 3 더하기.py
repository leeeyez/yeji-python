t = int(input())
tc = [int(input()) for _ in range(t)]

for c in tc:

    dp = [0] * (max(c+1, 4)) # dp 리스트 dp[n]: n을 만드는 방법의 수
    # 인덱스 오류 막기 위해 최소 크기 4로 함
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4 # (1+1+1, 1+2, 2+1, 3)

    for i in range(4, c+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    print(dp[c])
