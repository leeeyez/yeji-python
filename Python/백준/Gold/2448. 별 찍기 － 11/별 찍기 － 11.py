# 별 찍기 - 11

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5) # 재귀 깊이 (Recursion Error 방지)

n = int(input())

def draw_stars(n):
    # 가장 작은 기본 단위
    if n == 3:
        return ["  *  ", " * * ", "*****"]

    # 이전 단계(n/2)의 별 패턴을 가져옴
    prev_stars = draw_stars(n // 2)
    new_stars = []

    # [위쪽 파트] 이전 패턴의 양옆에 공백을 채워 가운데로 보냄
    # n // 2 만큼의 공백을 앞뒤로 붙여야 아래쪽 파트와 너비가 맞음
    for row in prev_stars:
        new_stars.append(" " * (n // 2) + row + " " * (n // 2))

    # [아래쪽 파트] 이전 패턴 두 개를 공백 하나를 사이에 두고 나란히 붙임
    for row in prev_stars:
        new_stars.append(row + " " + row)

    return new_stars


result = draw_stars(n)
print("\n".join(result))