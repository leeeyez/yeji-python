import sys
input = sys.stdin.readline

n = int(input())
num = [int(input()) for _ in range(n)]

# 음수일때 처리!!
def roundUp(x):
    if x > 0:
        return int(x + 0.5)
    else:
        return int(x - 0.5)

def mean(num):
    return roundUp(sum(num) / len(num))

def median(num):
    num.sort()
    return num[(len(num) // 2)]

from collections import Counter
def mode(num):
    counts = Counter(num) # {3: 3, 4: 3, 2: 2, 1: 1}
    most_common = counts.most_common() # (요소, 빈도) 리스트 반환 (이미 빈도순으로 정렬)
    # most_common.sort(key=lambda x: (-x[1], x[0]))
    # 최빈값이 여러 개면 두 번째로 작은 값
    if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
        return most_common[1][0]
    else:  # 하나면 그냥 반환
        return most_common[0][0]

def rangeOfnum(num):
    return max(num) - min(num)

print(mean(num))
print(median(num))
print(mode(num))
print(rangeOfnum(num))