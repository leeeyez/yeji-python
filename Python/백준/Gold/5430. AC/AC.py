# AC
# R(뒤집기) D(버리기)

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input()
    n = int(input())

    arr_input = input().strip().strip("[]").split(',') # 맨뒤 개행문자(\n) 제거 -> [] 제거 -> , 기준으로 나눔

    if n: # n > 0 일 때 deque에 
        queue = deque([int(a) for a in arr_input]) # int로
    else: # n = 0 일 때 빈 deque
        queue = deque([])

    iserror = False
    isreverse = False

    for pp in p.strip(): # p 입력시 문자열 끝에 \n 포함되어 반복문 한번 더 돌게 됨
        if not queue and pp == 'D':
            iserror = True
            break
        elif pp == 'R':
            # queue.reverse() --> 시간초과
            isreverse = not isreverse # 플래그로 관리
        else:
            if isreverse: # 리버스 상태이면 맨 뒤를 제거
                queue.pop()
            else:
                queue.popleft()
        
    if isreverse: # 최종 상태가 리버스인 경우 1회만 reverse()
        queue.reverse()

    if iserror:
        print('error')
    else:
        # print(list(queue)) --> 각 원소 사이에 공백 추가되어 출력
        print('[' + ','.join(map(str, queue)) + ']')
