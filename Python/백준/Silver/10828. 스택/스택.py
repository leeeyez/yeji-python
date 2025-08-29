n = int(input())

stack = []
result = []

for _ in range(n):
    order = input()
    if order == "top":
        if not stack:
            result.append("-1")
        else:
            result.append(stack[-1])
    elif order == "size":
        result.append(str(len(stack)))
    elif order == "empty":
        if not stack:
            result.append("1")
        else:
            result.append("0")
    elif order == "pop":
        if not stack:
            result.append("-1")
        else:
            result.append(stack.pop())
    else:
        p, num = order.split()
        stack.append(num)

print("\n".join(result))