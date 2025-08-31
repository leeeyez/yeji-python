import sys
input = sys.stdin.readline

n,m = map(int, input().split())
d = set(input().strip() for _ in range(n)) # 집합으로 저장, 개행 제거해야 출력형식오류 X

result = []

for _ in range(m):
    b = input().strip()
    if b in d: # 리스트일 경우 O(n*m), 집합일 경우 O(1)
        result.append(b)

result.sort()

print(len(result))
for r in result:
    print(r)