import sys
from itertools import combinations

# 입력 받기
n, m = map(int, sys.stdin.readline().split())
houses = []
chickens = []

for r in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for c in range(n):
        if row[c] == 1:
            houses.append((r, c))
        elif row[c] == 2:
            chickens.append((r, c))

# 결과값을 저장할 변수 (최댓값으로 초기화)
min_city_distance = float('inf')

# 치킨집 중에서 m개를 고르는 조합 반복
for selected_chickens in combinations(chickens, m):
    city_distance = 0
    
    # 각 집마다 가장 가까운 치킨집과의 거리를 계산
    for hr, hc in houses:
        temp_dist = float('inf')
        for cr, cc in selected_chickens:
            dist = abs(hr - cr) + abs(hc - cc)
            if dist < temp_dist:
                temp_dist = dist
        city_distance += temp_dist
    
    # 도시 전체 치킨 거리의 최솟값 갱신
    if city_distance < min_city_distance:
        min_city_distance = city_distance

print(min_city_distance)