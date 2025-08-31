n,k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

coins.sort(reverse=True) # 내림차순 정렬

answer = 0
for coin in coins:
    if k >= coin: # 현재 동전보다 k가 클 때
        answer += k // coin # 현재 동전으로 몇 개 쓸 수 있는지
        k %= coin # 동전으로 쓰고 난 나머지 금액
        if k <= 0:
            break

print(answer)