import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nlist = list(map(int, input().split()))
# mlist = [list(map(int, input().split())) for _ in range(m)]

# 시간 초과
# sum(nlist[i-1:j]) 는 쿼리마다 부분 리스트를 잘라서 합을 구함
# O(n·m) → n,m ≤ 100,000이면 10¹⁰ 연산
# for i, j in mlist:
#     print(sum(nlist[i-1:j]))

# 누적합 배열 (1-based)
prefix = [0] * (n+1) # prefix[n] : 첫번째 원소부터 n번째 원소까지의 합
for i in range(1, n+1):
    prefix[i] = prefix[i-1] + nlist[i-1]

for _ in range(m):
    i, j = map(int, input().split())
    print(prefix[j] - prefix[i-1]) # i번째부터 j번째까지 합