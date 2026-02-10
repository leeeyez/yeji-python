# 평범한 배낭
# N개의 물건, 무게 W와 가치 V,  최대 K만큼의 무게만을 넣을 수 있는 배낭 -> 물건들의 가치의 최댓값

import sys
input = sys.stdin.readline

n, k = map(int, input().split())  # n: 물건 개수, k: 배낭 최대 무게

# 물건 정보 저장
# items[i] = (무게, 가치)
items = []
items.append((0, 0))  # 인덱스 1부터 사용하기 위해 더미 추가

for _ in range(n):
    w, v = map(int, input().split())  # w: 무게, v: 가치
    items.append((w, v))

# dp[i][w] = i번째 물건까지 고려했을 때, 배낭 무게가 w일 때의 최대 가치
# 행: 0~n (물건 번호), 열: 0~k (배낭 무게)
dp = [[0] * (k + 1) for _ in range(n + 1)]

# i: 현재 고려하는 물건 번호
for i in range(1, n + 1):
    weight, value = items[i]  # i번째 물건의 무게와 가치
    
    # w: 현재 배낭의 무게 제한 (0kg ~ k kg)
    for w in range(k + 1):
        
        # 경우 1: i번째 물건을 넣을 수 없는 경우 (물건이 너무 무거워서 배낭에 안 들어감)
        if weight > w:
            # 이전 물건까지의 최대 가치를 그대로 가져옴
            dp[i][w] = dp[i-1][w]
        
        # 경우 2: i번째 물건을 넣을 수 있는 경우
        else:
            # 두 가지 선택지 중 더 큰 값 선택
            # 1) i번째 물건을 넣지 않는다: dp[i-1][w]
            # 2) i번째 물건을 넣는다: 
            #    - 현재 무게(w)에서 이 물건의 무게(weight)를 뺀 만큼의 공간에
            #    - i-1번째까지 물건으로 채운 최대 가치 dp[i-1][w-weight] (최적화)
            #    - 거기에 현재 물건의 가치(value)를 더함
            dp[i][w] = max(dp[i-1][w],                    # 안 넣음
                          dp[i-1][w-weight] + value)      # 넣음

# n번째 물건까지 고려했을 때, 배낭 무게가 k일 때의 최대 가치
print(dp[n][k])