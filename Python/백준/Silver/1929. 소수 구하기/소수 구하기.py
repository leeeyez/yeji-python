m, n = map(int, input().split())

def prime(num):
    if num < 2:   # 0, 1 제외
        return False
    # 시간초과 방지 : 루트 num까지만 확인해도 충분
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

for i in range(m, n+1):
    if prime(i):
        print(i)