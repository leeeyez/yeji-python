# 이중 우선순위 큐
# 최댓값과 최솟값을 출력하는 프로그램

# 시간초과
# import sys, heapq
# input = sys.stdin.readline

# t = int(input())

# for _ in range(t):
#     k = int(input()) # 연산의 개수
    
#     heap = []

#     for _ in range(k):
#         command, n = input().split() 
#         num = int(n) 
        
#         if command == 'I':
#             heapq.heappush(heap, num) 
            
#         elif command == 'D' and heap:
#             if num == 1:
#                 heap.remove(max(heap))
#                 heapq.heapify(heap)
#             else:
#                 heapq.heappop(heap)

#     if heap:
#         print(max(heap), heap[0])
#     else:
#         print('EMPTY')


import sys
import heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    
    # 1. 두 개의 힙과 유효성 검사 딕셔너리
    min_heap = []
    max_heap = []
    # {숫자: 개수}를 저장하여 유효성을 추적 (0이면 삭제된 것)
    counts = {} 
    
    for _ in range(k):
        command, n = input().split() 
        num = int(n)
        
        if command == 'I':
            # 삽입: 두 힙과 카운터에 기록
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num) # 최대 힙은 음수로 저장
            counts[num] = counts.get(num, 0) + 1
        
        elif command == 'D':
            if num == 1: # D 1: 최댓값 삭제
                # 유효한 최댓값을 찾을 때까지 최대 힙에서 제거 (동기화)
                while max_heap:
                    val = -heapq.heappop(max_heap)
                    if counts.get(val, 0) > 0:
                        # 유효한 최댓값 발견. 카운터 감소 후 반복 중단
                        counts[val] -= 1
                        break
            else: # D -1: 최솟값 삭제
                # 유효한 최솟값을 찾을 때까지 최소 힙에서 제거 (동기화)
                while min_heap:
                    val = heapq.heappop(min_heap)
                    if counts.get(val, 0) > 0:
                        # 유효한 최솟값 발견. 카운터 감소 후 반복 중단
                        counts[val] -= 1
                        break

    # 2. 결과 출력 전에 힙 정리 (최종적으로 남은 무효한 값 제거)
    while min_heap and counts.get(min_heap[0], 0) == 0:
        heapq.heappop(min_heap)
    
    while max_heap and counts.get(-max_heap[0], 0) == 0:
        heapq.heappop(max_heap)

    # 3. 최종 결과 출력
    if min_heap:
        # max_heap의 루트는 음수이므로 -를 붙여 출력
        print(-max_heap[0], min_heap[0])
    else:
        print('EMPTY')
