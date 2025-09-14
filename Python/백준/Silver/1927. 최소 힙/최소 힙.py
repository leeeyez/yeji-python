# 최소 힙
import sys, heapq
input = sys.stdin.readline

n = int(input())

# result = []

# for _ in range(n):
#     x = int(input())
#     if x == 0 and result:
#         target = min(result)
#         print(target)
#         result.remove(target)
#     elif x == 0 and not result:
#         print(0)
#     else:
#         result.append(x)

heap = []

# 힙 : 완전 이진 트리 구조를 리스트로 표현 => 부모가 최소로 알아서 정렬
# pop : 루트 노드부터 내려가면서 꺼냄
# push : 가장 끝 노드에 삽입
for _ in range(n):
    x = int(input())
    if x == 0 and heap:
        print(heapq.heappop(heap)) # 최소값 꺼내기
    elif x == 0 and not heap:
        print(0)
    else:
        heapq.heappush(heap, x) # 삽입