n,m = map(int, input().split())
chess = [list(input()) for _ in range(n)]

count = []

# 8x8 위치를 정하는 반복문
for a in range(n-7):
    for b in range(m-7):
        index1 = 0 # WBWBWBWB
        index2 = 0 # BWBWBWBW
        # 각 좌표별로 case 따지기
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0: # 두 좌표를 더했을 때 짝수
                    if chess[i][j] != 'W':
                        index1 += 1
                    if chess[i][j] != 'B':
                        index2 += 1
                else: # 두 좌표를 더했을 때 홀수
                    if chess[i][j] != 'B':
                        index1 += 1
                    if chess[i][j] != 'W':
                        index2 += 1
        count.append(min(index1, index2))

print(min(count))