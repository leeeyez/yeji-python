n = int(input())
nlist = set(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

for mm in mlist:
    if mm in nlist:
        print(1)
    else:
        print(0)
