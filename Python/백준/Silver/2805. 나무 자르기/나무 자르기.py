# 나무 자르기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start, end = 1, max(tree)
result = 0

while start <= end:
    mid = (start + end) // 2
    cut_tree = 0
    for t in tree:
        if mid < t:
            cut_tree += t - mid
    
    if cut_tree >= m:  # m미터 이상 만들 수 있다면, 더 높이 올려서 자를 수 있는지 확인
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)