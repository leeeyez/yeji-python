# N과 M(12)
# N개의 자연수 중에서 M개를 고른 수열 (같은 수 여러번 가능, 비내림차순)

import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

# m개를 선택하는 모든 조합 구하기
allcomb = list(set(combinations_with_replacement(numbers, m)))
allcomb.sort()


# 각 조합 출력
for comb in allcomb:
    print(*comb) # 공백으로 구분해서 출력