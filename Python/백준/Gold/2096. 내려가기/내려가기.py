# 내려가기
# 내려가기 게임에서 얻을 수 있는 최대 점수, 최소 점수를 구하기
# 내려가기 게임 : 바로 아래의 수로 넘어가거나, 아니면 바로 아래의 수와 붙어 있는 수로만 이동 가능

import sys
input = sys.stdin.readline

n = int(input())

# 메모리 초과
# # N×3 크기 배열 생성
# dp_max = [[0] * 3 for _ in range(n)]
# dp_min = [[0] * 3 for _ in range(n)]

# # 첫 줄 초기화
# dp_max[0] = list(map(int, input().split()))
# dp_min[0] = dp_max[0][:]

# # DP
# for i in range(1, n):
#     arr = list(map(int, input().split()))
    
#     # 0열: 이전 줄의 0열 또는 1열에서 올 수 있음
#     dp_max[i][0] = arr[0] + max(dp_max[i-1][0], dp_max[i-1][1])
#     # 1열: 이전 줄의 0, 1, 2열 모두에서 올 수 있음
#     dp_max[i][1] = arr[1] + max(dp_max[i-1][0], dp_max[i-1][1], dp_max[i-1][2])
#     # 2열: 이전 줄의 1열 또는 2열에서 올 수 있음
#     dp_max[i][2] = arr[2] + max(dp_max[i-1][1], dp_max[i-1][2])
    
#     # 최솟값도 동일
#     dp_min[i][0] = arr[0] + min(dp_min[i-1][0], dp_min[i-1][1])
#     dp_min[i][1] = arr[1] + min(dp_min[i-1][0], dp_min[i-1][1], dp_min[i-1][2])
#     dp_min[i][2] = arr[2] + min(dp_min[i-1][1], dp_min[i-1][2])

# print(max(dp_max[n-1]), min(dp_min[n-1]))


# 메모리 최적화: N×3 배열이 아닌 1×3 배열만 사용
# 이전 줄의 정보만 저장하면 됨
dp_max = [0, 0, 0]  # 최댓값을 저장하는 배열
dp_min = [0, 0, 0]  # 최솟값을 저장하는 배열

# N개의 줄을 입력받으며 DP 진행
for i in range(n):
    arr = list(map(int, input().split()))  # 현재 줄의 숫자 3개
    
    # 첫 번째 줄인 경우
    if i == 0:
        # 첫 줄은 그냥 그 값이 최댓값이자 최솟값
        dp_max = arr[:]  # 복사
        dp_min = arr[:]  # 복사
    
    # 두 번째 줄부터
    else:
        # 이전 줄의 값을 임시로 저장 (곧 덮어쓸 예정이므로)
        prev_max_0, prev_max_1, prev_max_2 = dp_max[0], dp_max[1], dp_max[2]
        prev_min_0, prev_min_1, prev_min_2 = dp_min[0], dp_min[1], dp_min[2]
        
        # 최댓값 계산
        # 0열: 이전 줄의 0열 or 1열
        dp_max[0] = arr[0] + max(prev_max_0, prev_max_1)
        
        # 1열: 이전 줄의 0열, 1열, 2열 모두
        dp_max[1] = arr[1] + max(prev_max_0, prev_max_1, prev_max_2)
        
        # 2열: 이전 줄의 1열 or 2열
        dp_max[2] = arr[2] + max(prev_max_1, prev_max_2)
        
        # 최솟값 계산
        dp_min[0] = arr[0] + min(prev_min_0, prev_min_1)
        dp_min[1] = arr[1] + min(prev_min_0, prev_min_1, prev_min_2)
        dp_min[2] = arr[2] + min(prev_min_1, prev_min_2)

print(max(dp_max), min(dp_min))