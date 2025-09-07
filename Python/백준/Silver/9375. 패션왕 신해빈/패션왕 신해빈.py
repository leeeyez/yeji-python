t = int(input())

for _ in range(t):
    c = int(input())
    c_data = [list(input().split()) for _ in range(c)]

    clothes = {} # 타입: 해당 타입 옷 개수
    for _, c_type in c_data:
        if not c_type in clothes:  # 아직 없는 타입이라면 추가
            clothes[c_type] = 1
        else:                      # 이미 있는 타입이라면 해당 key에 +1
            clothes[c_type] += 1

    result = 1 # 모든 경우의 수
    for i in clothes:
        result *= (clothes[i] + 1)  # 경우의 수 : (타입별 옷 개수 + 안 입는 경우(1))를 곱해서 측정
        # ex. 상의 2개, 바지 3개 모든 경우의 수: (2+1(상의 안 입는 경우)) * (3+1(바지 안 입는 경우))

    print(result - 1)
    # 적어도 1개만 걸치면 밖에 나갈 수 있으므로, 모든 경우의 수 - 1(전부 안 입는 경우)