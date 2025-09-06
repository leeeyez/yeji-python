stairs = int(input())
score = [int(input()) for _ in range(stairs)]

# 예외 처리: 계단이 1개인 경우
if stairs == 1:
    print(score[0])
    exit()

# 계단이 2개인 경우
if stairs == 2:
    print(score[0] + score[1])
    exit()

dp = [0] * (stairs) # dp 리스트 dp[n]: n번째 계단까지의 점수

dp[0] = score[0]
dp[1] = score[0] + score[1]
dp[2] = max(score[0] + score[2], score[1] + score[2])

# 1. 2칸 밑의 계단에서 현재 계단으로 올라온다 : dp[i-2] + s[i]
# 2. 1칸 밑의 계단에서 현재 계단으로 올라온다 (이때, 연속된 3칸을 오를 수 없으므로 무조건 1칸 밑으로 올라오는 선행 단계에서는 2칸을 올라와야 한다.)
# : dp[i-3] + s[i-1] + s[i]
for i in range(3, stairs):
    dp[i] = max(dp[i-3] + score[i-1] + score[i], dp[i-2] + score[i]) # 둘 중 점수가 더 큰 쪽으로

print(dp[-1]) # 가장 마지막 칸에 올라갔을 때 점수