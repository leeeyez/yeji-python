n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]

# 자기보다 덩치 큰 사람의 수를 담을 배열
k = [0] * n

# 자기보다 덩치 큰 사람의 수를 리턴
def search(w, h):
    count = 0
    for other_w, other_h in info:
        if other_w > w and other_h > h:
            count += 1

    return count

# 가장 작은 수를 1로 만들기 위해 각 원소에 더해줄 수
# 왜냐면 자기보다 덩치 큰 사람의 수 = 순위 자체이기 때문
rank = 1 - min(k) 

# 배열을 돌면서 k를 채움 (인덱스별로 자신보다 덩치 큰 사람의 수)
for i in range(n):
    k[i] = search(info[i][0], info[i][1]) + rank


for ranking in k:
    print(ranking, end=" ")