# N과 M (4)
# 1부터 N까지 자연수 중에서 중봅 없이 M개를 고르 수열 (오름차순) + 길이 M
# 같은 수를 여러 번 골라도 O + 비내림차순(오름차순인데, 같아도 됨)

import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement # 중복 조합 내장 함수

n, m = map(int, input().split())

# 1부터 n까지의 숫자 리스트 만들기
numbers = []
for i in range(1, n + 1):
    numbers.append(i)

# 1~n 리스트에서 m개를 선택하는 모든 조합 구하기
allcomb = combinations_with_replacement(numbers, m)

# 각 조합 출력
for combo in allcomb:
    print(*combo) # 공백으로 구분해서 출력