# A -> B
# A를 B로 바꾸는데 필요한 연산의 최솟값

import sys
input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())
cnt = 1 # 최솟값에 1을 더해야하므로 초깃값을 1로

while b > a: # b == a 될때까지
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    else:
        cnt = -1
        break
    cnt += 1

if b != a: # b가 a보다 작아졌을 수도 있음
    cnt = -1

print(cnt)