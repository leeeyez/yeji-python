# 구간 합 구하기 5
# (x1, y1)부터 (x2, y2)까지 합 (직사각형 영역)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 패딩(0) 추가하는 이유 = 문제에서 1부터 시작하는 인덱스를 사용
arr = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

# 2차원 누적 합 배열 생성
prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]

# 누적 합 계산 (1,1)부터 해당 위치까지의 모든 수의 합
for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_sum[i][j] = arr[i][j] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

# 원본 배열:           누적 합 배열:
# 1  2  3  4          1   3   6  10
# 2  3  4  5          3   8  15  24
# 3  4  5  6          6  15  27  42
# 4  5  6  7         10  24  42  64

# 입력 처리
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1] # 중복으로 빠진 부분 더해주기
    print(result)
