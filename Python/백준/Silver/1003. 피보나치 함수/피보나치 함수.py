t = int(input())
tc = [int(input()) for _ in range(t)]

# 시간 초과 코드
# def fibonacci(n, print_data):
#     if n == 0:
#         print_data.append(0)
#         return 0
#     elif n == 1:
#         print_data.append(1)
#         return 1
#     else:
#         return fibonacci(n-1, print_data) + fibonacci(n-2, print_data)


# for c in tc:
#     result = []
#     fibonacci(c, result)
#     print(f'{result.count(0)} {result.count(1)}')


# dp[n] = (0 호출 횟수, 1 호출 횟수)
dp = [(0, 0)] * 41   # 문제에서 n ≤ 40 조건 있음

dp[0] = (1, 0)
dp[1] = (0, 1)

# fibonacci(n)에서 0과 1의 호출 횟수
# = fibonacci(n-1) 실행 중 나온 출력 횟수 + fibonacci(n-2) 실행 중 나온 출력 횟수
for i in range(2, 41):
    dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])

for c in tc:
    print(dp[c][0], dp[c][1])