# 색종이 만들기
import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white, blue = 0, 0


def div(x, y, n):
    global white, blue # 전역 변수 사용 (선언하지 않으면 로컬 변수로 인식해서 UnboundLocalError)
    # 각 섹션 안에 원소들의 합을 구해서 cnt에 저장
    cnt = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] == 1:
                cnt += 1

    # 섹션 안의 원소 합이 0이면 모두 0이므로 하얀색
    if cnt == 0:
        white += 1
    # 원소 합이 n*n이면 모두 1이므로 파란색
    elif cnt == n*n:
        blue += 1
    else:
        n //= 2        # n을 이등분
        div(x,y,n)     # 왼쪽 위
        div(x+n,y,n)   # 오른쪽 위
        div(x,y+n,n)   # 왼쪽 아래
        div(x+n,y+n,n) # 오른쪽 아래

div(0,0,n)
print(white)
print(blue)