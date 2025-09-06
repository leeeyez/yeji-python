from collections import deque

n = int(input())
queue = deque([(n, 0)])   # (현재 숫자, 연산 횟수)
visited = set([n])        # 방문 체크

while queue:
    cur, time = queue.popleft()
    if cur == 1:
        print(time)
        break
    
    # 가능한 다음 상태들
    if cur % 3 == 0 and cur // 3 not in visited:
        visited.add(cur // 3)
        queue.append((cur // 3, time + 1))
    if cur % 2 == 0 and cur // 2 not in visited:
        visited.add(cur // 2)
        queue.append((cur // 2, time + 1))
    if cur - 1 not in visited:
        visited.add(cur - 1)
        queue.append((cur - 1, time + 1))