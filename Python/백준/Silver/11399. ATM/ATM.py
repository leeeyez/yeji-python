n = int(input())
p = list(map(int, input().split()))

# 짧은 시간부터 세우는 것이 전체 대기 시간의 합을 최소화
p.sort()

time = 0
result = 0
for i in p:
    time += i
    result += time

print(result)

# permutations로 모든 경우의 수를 확인하려고 했으나, 시간 초과 O(n!)