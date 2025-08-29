from collections import deque
n = int(input())

queue = deque([])
result = []

for _ in range(n):
    order = input()
    if order == "front":
        if not queue:
            result.append("-1")
        else:
            result.append(queue[0])
    elif order == "back":
        if not queue:
            result.append("-1")
        else:
            result.append(queue[-1])
    elif order == "size":
        result.append(str(len(queue)))
    elif order == "empty":
        if not queue:
            result.append("1")
        else:
            result.append("0")
    elif order == "pop":
        if not queue:
            result.append("-1")
        else:
            result.append(queue.popleft())
    else:
        p, num = order.split()
        queue.append(num)

print("\n".join(result))