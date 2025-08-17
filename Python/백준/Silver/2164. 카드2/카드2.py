# n = int(input())
# card = [i for i in range(1, n+1)]

# while len(card) > 1:
#     card.pop(0)

#     t = card[0]
#     card.pop(0)
#     card.append(t)

# print(card[0])

# deque를 써야하는 이유: append와 pop() 자체는 O(1)이지만, 
# pop(0)을 할 경우 맨 뒤 원소부터 당겨야해서 O(N) -> 시간 초과
# deque는 양쪽에서 pop/append 모두 O(1)

from collections import deque

n = int(input())
card = deque(range(1, n+1))

while len(card) > 1:
    card.popleft()
    card.append(card.popleft()) 

print(card[0])
