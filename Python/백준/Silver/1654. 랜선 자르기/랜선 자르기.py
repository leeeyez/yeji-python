# 랜선 자르기
import sys
input = sys.stdin.readline

k,n = map(int, input().split())
lan = [int(input()) for _ in range(k)]

start, end = 1, max(lan)
result = 0

while start <= end:
    mid = (start + end) // 2 # 중간지점을 기준으로 이등분
    cnt = 0 # 자른 개수
    for l in lan:
        cnt += l // mid

    if cnt >= n: # n개 이상 만들 수 있으면 늘리기
        result = mid
        start = mid + 1
    else: # n개가 안 되면 줄이기
        end = mid - 1

print(result)