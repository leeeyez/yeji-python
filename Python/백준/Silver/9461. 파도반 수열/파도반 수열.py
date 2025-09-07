t = int(input())
tc = [int(input()) for _ in range(t)]

for c in tc:
    # 파도반 수열 규칙 P(n) = P(n-2) + P(n-3)
    # dp[n] : n번째 삼각형 변의 길이
    dp = [0] * (max(c+1, 4)) # 인덱스 오류 방지 : 최소 4개 인덱스
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1

    for i in range(4, c+1):
        dp[i] = dp[i-2] + dp[i-3]
    
    print(dp[c])