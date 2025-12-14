# 곱셈

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

# 시간 초과
# print(a**b % c)


# 분할 정복
result = 1

while b > 0:
    # b(지수)가 홀수면 result에 a 곱하기 (a^(짝수 + 1) 형태이기 때문)
    if b % 2 == 1:
        result = (result * a) % c  # 어차피 나머지를 구하는거니까 계속 c로 나누기

    # a를 제곱하고 b를 반으로 줄이기
    a = (a*a) % c
    b //= 2

print(result)