# 최대 힙

import sys, heapq
input = sys.stdin.readline

heap = []

n = int(input())

for _ in range(n):
    x = int(input())
    if x == 0 and heap:
        print(heapq.heappop(heap)[1]) # 최대값 꺼내기 (튜플에서 인덱스 1인 것)
    elif x == 0 and not heap:
        print(0)
    else:
        heapq.heappush(heap, (-x, x)) # (우선순위, 값) : 우선순위를 반대로 설정함으로써 역순 정렬 - 부모가 최소