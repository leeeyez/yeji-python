# DSLR
# A에서 B로 변환하기 위해 필요한 최소한의 명령어 나열을 출력


import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    A, B = map(int, input().split())
    
    # 큐에 (현재 숫자, 현재까지의 명령어 경로) 저장
    queue = deque([(A, "")])
    # 숫자가 방문되었는지 확인
    visited = [False] * 10000 
    visited[A] = True
    
    # BFS 시작
    while queue:
        current_num, commands = queue.popleft()
        
        if current_num == B: # B면 끝
            print(commands)
            break

        # D 연산: 2n mod 10000
        next_num_D = (current_num * 2) % 10000
        if not visited[next_num_D]:
            visited[next_num_D] = True
            queue.append((next_num_D, commands + "D"))
            
        # S 연산: n-1 또는 9999
        if current_num != 0:
            next_num_S = (current_num - 1)
        else:
            next_num_S = 9999
        if not visited[next_num_S]:
            visited[next_num_S] = True
            queue.append((next_num_S, commands + "S"))
            
        # L 연산: d1 d2 d3 d4 -> d2 d3 d4 d1
        # (n % 1000) -> d2 d3 d4 | (n // 1000) -> d1
        next_num_L = (current_num % 1000) * 10 + (current_num // 1000)
        if not visited[next_num_L]:
            visited[next_num_L] = True
            queue.append((next_num_L, commands + "L"))
            
        # R 연산: d1 d2 d3 d4 -> d4 d1 d2 d3
        # (n % 10) -> d4 | (n // 10) -> d1 d2 d3
        next_num_R = (current_num % 10) * 1000 + (current_num // 10)
        if not visited[next_num_R]:
            visited[next_num_R] = True
            queue.append((next_num_R, commands + "R"))