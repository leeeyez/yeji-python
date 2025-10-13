# Z
# r행c열을 몇 번째로 방문했는지 출력

n, r, c = map(int, input().split())

# # r,c의 홀짝여부를 통해 사분면 결정
# if r % 2 == 0 and c % 2 == 0:
#     quadrant = 0
#     qr, qc = 0, 0
# elif r % 2 == 0 and c % 2 != 0:
#     quadrant = 1
#     qr, qc = 0, 1
# elif r % 2 != 0 and c % 2 == 0:
#     quadrant = 2
#     qr, qc = 1, 0
# else:
#     quadrant = 3
#     qr, qc = 1, 1

# result = quadrant

# for i in range(qr, r, 2):
#     for j in range(qc, c, 2):
#         result += 4

# print(result)

result = 0

# 현재 크기
size = 2 ** n

while size > 1:
    size //= 2
    
    # r,c의 현재 사분면 결정
    if r < size and c < size:
        quadrant = 0
        qr, qc = 0, 0
    elif r < size and c >= size:
        quadrant = 1
        qr, qc = 0, size
    elif r >= size and c < size:
        quadrant = 2
        qr, qc = size, 0
    else:
        quadrant = 3
        qr, qc = size, size
    
    # 해당 사분면 이전 칸들을 더함
    result += quadrant * (size * size)
    
    # 다음 단계를 위해 상대 좌표로 변환
    r -= qr
    c -= qc

print(result)