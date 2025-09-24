# 과일 탕후루

import sys
input = sys.stdin.readline

n = int(input())
fruits = list(map(int, input().split()))

# 시간 초과
# max_length = 0

# for i in range(n):
#     ggochi = []
#     set_f = set()

#     for j in range(i, n):         # i부터 n까지 하나씩 추가해가면서 확인
#         ggochi.append(fruits[j])
#         set_f.add(fruits[j])

#         if len(set_f) <= 2:
#             max_length = max(max_length, len(ggochi))
#         else:
#             break

# print(max_length)


# 슬라이딩 윈도우 (투 포인터) 기법
left = 0
max_length = 0
fruit_count = {}  # 각 과일의 개수를 저장

for right in range(n):
    # 오른쪽 포인터의 과일을 추가
    fruit_count[fruits[right]] = fruit_count.get(fruits[right], 0) + 1
    
    # 과일 종류가 2개를 초과하면 왼쪽 포인터를 이동
    while len(fruit_count) > 2:
        fruit_count[fruits[left]] -= 1
        if fruit_count[fruits[left]] == 0:
            del fruit_count[fruits[left]]
        left += 1
    
    # 현재 윈도우의 길이를 확인
    max_length = max(max_length, right - left + 1)

print(max_length)

# defaultDict(int) key값에 대한 value값을 0으로 알아서 초기화