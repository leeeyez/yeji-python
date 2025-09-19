# 좌표 압축

import sys
input = sys.stdin.readline
import bisect

n = int(input())
coor = list(map(int, input().split()))

# 시간 초과
# result = [0] * n

# for i in range(n):
#     for j in range(n):
#         if coor[i] > coor[j]:
#             result[i] += 1

# for r in result:
#     print(r, end=" ")

sort_coor = sorted(set(coor))
result = [bisect.bisect_left(sort_coor, x) for x in coor]
# arr = [1,2,2,2,5] -> bisect_left(arr, 2) = 1 / bisect_right(arr, 2) = 4

for r in result:
    print(r, end=" ")


# ex
# coor = [2, 4, -10, 4, -9]
# sort_coor = [-10, -9, 2, 4]
# bisect_left(sort_coor, 2) = 2 / (sort_coor, 4) = 3 / (sort_coor, -10) = 0 ...