# 회의실 배정
# 

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]

# info.sort()

# result = 0

# 시간 초과
# for i in range(n):
#     timeline = []
#     for start, end in info:
#         if not timeline or timeline[-1][1] <= start:
#             timeline.append([start, end])
    
#     result = max(result, len(timeline))
        
# print(result)


# 끝나는 시간 기준으로 정렬 (끝나는 시간이 같으면 시작 시간 기준)
info.sort(key=lambda x: (x[1], x[0]))

result = 0
last_end = 0 # 끝나는 시간

for start, end in info:
    if last_end <= start:
        result += 1
        last_end = end
        
print(result)