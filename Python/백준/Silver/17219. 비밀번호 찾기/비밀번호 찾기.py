n,m = map(int, input().split())

address = {}
for _ in range(n):
    add, pw = input().split()
    address[add] = pw

for _ in range(m):
    target = input()
    print(address[target])