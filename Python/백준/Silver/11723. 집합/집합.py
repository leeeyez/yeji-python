import sys
input = sys.stdin.readline

m = int(input())
s = set()

for _ in range(m):
    o = input().strip()
    if o == "all":
        s = set([i for i in range(1,21)])
    elif o == "empty":
        s = set()
    else:
        op, num = o.split()
        num = int(num)
        if op == "add":
            s.add(num)
        elif op == "remove":
            if num in s:
                s.remove(num)
        elif op == "check":
            if num in s:
                print(1)
            else:
                print(0)
        elif op == "toggle":
            if num in s:
                s.remove(num)
            else:
                s.add(num)
