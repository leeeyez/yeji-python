# N과 M (4)
# N개의 자연수 중 M개를 고른 수열

import sys
input = sys.stdin.readline
from itertools import permutations

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

# m개를 선택하는 모든 조합 구하기
allperm = list(permutations(numbers, m))
allperm.sort()


# 각 조합 출력
for perm in allperm:
    print(*perm) # 공백으로 구분해서 출력


# 백트래킹 풀이 (순열의 경우, 조합과 다르게 start부터 선택하는 것이 아니라 항상 리스트의 처음부터 끝까지 탐색)
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# numbers = list(map(int, input().split()))
# numbers.sort()

# selected = []
# visited = [False] * N # 중복 방지

# def backtrack(depth):
#     # 종료 조건: M개를 모두 선택
#     if depth == m:
#         print(*selected)
#         return
    
#     # 순서 고려: 항상 리스트의 처음부터 끝까지 탐색
#     for i in range(n):
#         if not visited[i]: # 중복 방지 조건
#             visited[i] = True
#             selected.append(numbers[i])      # 선택
#             backtrack(depth + 1)             # 탐색 (i부터 = 중복 허용)
#             selected.pop()                   # 취소 (M개 모두 선택 후)
#             visited[i] = False

# backtrack(0) # depth 0부터