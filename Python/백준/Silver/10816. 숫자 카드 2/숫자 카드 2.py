from bisect import bisect_left, bisect_right

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

cards.sort()

result = []

# 시간초과
# for t in target:
#     count = 0
#     for c in cards:
#         if t == c:
#             count += 1
#     result.append(count)


# bisect_left(a, x): 배열 a의 정렬된 상태를 유지하면서 원소 x를 삽입할 수 있는 가장 왼쪽 인덱스를 리턴
# bisect_right(a, x): 배열 a의 정렬된 상태를 유지하면서 원소 x를 삽입할 수 있는 가장 오른쪽 인덱스를 리턴
for t in target:
    left = bisect_left(cards, t)
    right = bisect_right(cards, t)
    result.append(right - left)

for r in result:
    print(r, end=" ")