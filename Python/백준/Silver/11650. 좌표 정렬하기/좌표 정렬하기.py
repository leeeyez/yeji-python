n = int(input())
coor = [list(map(int, input().split())) for _ in range(n)]

result = sorted(coor, key=lambda x: (x[0], x[1]))

for x, y in result:
    print(f"{x} {y}")