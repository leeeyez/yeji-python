# 가장 긴 증가하는 부분 수열

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

# DP - dp[i]: a[i]를 마지막 원소로 갖는 최대 수열 길이
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]: # 증가하는 형태이면
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

# bisect_left: 똑같은 원소가 있을 때 가장 좌측
# import bisect
# result = []
# for num in a:
#     pos = bisect.bisect_left(result, num) # 들어갈 위치 인덱스
#     if pos = len(result): # 맨 끝자리면 append
#         result.append(num)
#     else: # 맨 끝이 아니면 해당 위치에 넣기
#         result[pos] = num

# print(len(result))