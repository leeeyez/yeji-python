# 마인크래프트
# (i,j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣음 = 2초
# 인벤토리에서 블록 하나를 꺼내서 (i,j) 가장 위에 있는 블록 위에 놓음 = 1초
# 땅을 고르는데 걸리는 최소 시간과 땅의 높이 출력 (땅의 높이 여러개이면 가장 높은것)

import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())

time = int(1e9)
ground = 0

# 시간복잡도가 O(257 × N × M)로 시간초과
# block = [list(map(int, input().split())) for _ in range(n)]
# for i in range(257): # 땅 높이
#     use = 0   # 사용한 블록 개수
#     take = 0  # 가져온 블록 개수
#     for x in range(n):
#         for y in range(m):
#             if block[x][y] > i:         # 현재 i 높이보다 크면 그 개수만큼 가져온다
#                 take += block[x][y] - i
#             else:                       # 현재 i 높이보다 작으면 그 개수만큼 뺀다
#                 use += i - block[x][y]

#         if use <= take + b:   # 사용한 블록 수가 전체 인벤토리 내 개수보다 작을 때
#             if (take * 2 + use) <= time: # 최소 time이면 갱신
#                 time = take * 2 + use
#                 ground = i


# 모든 블록의 높이를 1차원 리스트에 저장
block = []
for _ in range(n):
    block.extend(list(map(int, input().split())))

# 높이별 개수 카운팅
height_count = [0] * 257
for height in block:
    height_count[height] += 1

# 누적합을 이용한 최적화
total_blocks = sum(block)

for target_height in range(257):
    use = 0
    take = 0
    
    for h in range(257):
        if height_count[h] == 0: # 해당 높이가 block에 존재하지 않으면 무시
            continue
            
        # 높이별로 한번에 처리
        if h > target_height: # 타겟 높이보다 높을 때 take
            take += (h - target_height) * height_count[h]
        elif h < target_height: # 타겟 높이보다 낮을 때 use
            use += (target_height - h) * height_count[h]
    
    if use <= take + b: # 가능한 경우임을 확인 (use가 총 블록 수보다 작아야함)
        current_time = take * 2 + use
        if current_time <= time:
            time = current_time
            ground = target_height

print(time, ground)


# # 수학적으로 최적화
# min_height = min(block)
# max_height = max(block)

# time = int(1e9)
# ground = 0

# # 타겟 높이를 min에서 max까지로 잡음
# for target in range(min_height, max_height + 1):
#     use = 0
#     take = 0
    
#     for height in block:
#         if height > target:
#             take += height - target
#         else:
#             use += target - height
    
#     if use <= take + b:
#         current_time = take * 2 + use
#         if current_time <= time:
#             time = current_time
#             ground = target

# print(time, ground)