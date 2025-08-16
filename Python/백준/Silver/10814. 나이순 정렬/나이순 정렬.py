n = int(input())
info = [list(input().split()) for _ in range(n)]

result = sorted(info, key=lambda x:int(x[0]))

for age, name in result:
    print(f"{age} {name}")