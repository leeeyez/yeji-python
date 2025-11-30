# N과 M(9)
# N개의 자연수 중에서 M개를 고른 수열

import sys
input = sys.stdin.readline
from itertools import permutations

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

# m개를 선택하는 모든 조합 구하기
allperm = list(set(permutations(numbers, m)))
allperm.sort()


# 각 조합 출력
for perm in allperm:
    print(*perm) # 공백으로 구분해서 출력