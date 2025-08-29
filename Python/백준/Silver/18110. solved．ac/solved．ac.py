# python의 round 함수는 사사오입의 원칙을 따른다.
# 사사오입 : 5에서 반올림할 때, 앞자리 숫자가 홀수면 올림, 짝수면 내림 (1.5 = 2 / 2.5 = 1)
# 이 문제에서는 round 함수를 사용하면 오답처리 -> 5이면 무조건 반올림

# 정수형 자료를 이용한 반올림 함수
def roundUp(num):
    if(num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


#from collections import deque
import sys
input = sys.stdin.readline # 마지막 시간 초과ㄴ

n = int(input()) # 난이도 의견 개수
if n == 0:
    print(0)
else:
    level = [int(input()) for _ in range(n)]

    level.sort()
    exc = roundUp(n * 0.15)
    level = level[exc:n-exc] # 슬라이싱

    # 큐 자료구조로 처음 풀었는데, 시간초과
    # qlevel = deque(level)
    # for i in range(exc):
    #     qlevel.pop()
    #     qlevel.popleft()

    if len(level) == 0:
        print(0)  # 의견이 없으면 0
    else:
        print(roundUp(sum(level)/len(level)))