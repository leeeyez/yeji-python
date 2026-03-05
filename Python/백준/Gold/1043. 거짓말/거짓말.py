# 거짓말
# 사람의 수 = N / 파티의 수 = M
# 거짓말쟁이로 알려지지 않으면서, 과장된 이야기를 할 수 있는 파티 개수의 최댓값

# 거짓말을 할 수 없는 두가지 경우
# 1. 직접적으로 진실을 아는 사람이 파티에 있을 때
# 2. 진실을 아는 사람과 함께 파티에 참석했던 사람이 파티에 있을 때
# -> 진실을 아는 사람과 연결된 모든 사람이 있는 파티에서 무조건 진실만 말해야함

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
t = list(map(int, input().split())) # 진실 관련 전체 input
tp = t[1:] # 진실을 아는 사람들 번호를 담은 배열

adj = [[] for _ in range(n+1)] # 사람 간의 관계 그래프
party = []

# 하나의 파티에 참석한 사람들 연결시키기
for _ in range(m):
    p = list(map(int, input().split())) # 파티 정보 : 오는 사람 수, 오는 사람 번호1, 번호2 ...
    pp = p[1:] # 해당 파티에 오는 사람들 번호 리스트
    party.append(pp)

    # 같은 파티 사람들끼리 양방향 연결
    for i in range(len(pp)):
        for j in range(i+1, len(pp)):
            adj[pp[i]].append(pp[j]) # 1, 3이 같은 파티에 참석했다면 adj[1] = 3 / adj[3] = 1
            adj[pp[j]].append(pp[i])


# 진실을 알게 되는 사람들 (인덱스가 사람 번호)
know_truth = [False] * (n+1)
for p in tp: # 이미 진실을 아는 사람들
    know_truth[p] = True 

# bfs 통해 진실 전파 (원래 진실 알던 사람들 - 같은 파티 참석한 사람들 간)
queue = deque(tp) # 진실을 아는 사람 큐
while queue:
    cur = queue.popleft()
    for nxt in adj[cur]:
        if not know_truth[nxt]:
            know_truth[nxt] = True
            queue.append(nxt) # 진실을 아는 사람 큐에 넣음

# 파티마다 진실을 아는 사람이 있는지 검사
answer = 0
for p in party:
    if not any(know_truth[person] for person in p): # 파티의 사람들 중 진실을 아는 사람이 1명도 없는 경우
        answer += 1

print(answer)