from collections import deque
n, k = input().split()
num = [i+1 for i in range(int(n))]

circle = deque(num)

result = []

while circle:
    circle.rotate(-int(k)) # 왼쪽 회전시킴
    result.append(circle.pop())

# <1, 2, 3> 구조로 만들기
formatted = "<" + ", ".join(map(str, result)) + ">"
print(formatted)