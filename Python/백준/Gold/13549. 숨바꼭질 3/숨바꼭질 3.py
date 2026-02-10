# 숨바꼭질 3
# 수빈 N, 동생 K / 수빈 걷기 : 1초 후 X+1, X-1 / 수빈 순간이동 : 0초 후 2*X
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

max_pos = 100001
# visited 리스트를 -1로 초기화 (방문하지 않았다는 뜻)
visited = [-1] * max_pos

# 큐 생성 및 시작점(n) 넣기
queue = deque([n])
visited[n] = 0 # 시작 위치의 소요 시간은 0초

while queue:
    now = queue.popleft()
    
    # 동생을 찾았다면 걸린 시간 출력 후 종료
    if now == k:
        print(visited[now])
        break
    
    # 이동 가능한 3가지 경우 확인
    # 순간이동 (0초 소요) -> 'appendleft'로 큐의 맨 앞에 넣기 (0초 걸리니까 훨씬 이득이라 앞으로 새치기)
    if 0 <= now * 2 < max_pos and visited[now * 2] == -1:
        visited[now * 2] = visited[now]
        queue.appendleft(now * 2)
        
    # 뒤로 걷기 (1초 소요) -> 'append'로 큐의 맨 뒤에 넣기
    if 0 <= now - 1 < max_pos and visited[now - 1] == -1:
        visited[now - 1] = visited[now] + 1
        queue.append(now - 1)
        
    # 앞으로 걷기 (1초 소요) -> 'append'로 큐의 맨 뒤에 넣기
    if 0 <= now + 1 < max_pos and visited[now + 1] == -1:
        visited[now + 1] = visited[now] + 1
        queue.append(now + 1)