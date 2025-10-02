# IOIOI
# S 안에 Pn이 몇 군데 포함되어 있는지 구하기

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()

pn = "IO" * n + "I"  # pn 문자열 만들기
len_pn = 2*n + 1     # pn의 길이

# 인자가 pn 문자열을 만족하면 1 아니면 0을 리턴하는 함수
def checkPn(checkstr):
    if checkstr == pn:
        return 1
    else: return 0


cnt = 0
for i in range(m - len_pn + 1):
    if s[i] == 'I': # 모든 pn은 I로 시작하므로 I일 때 checkpn
        cnt += checkPn(s[i:i+len_pn])

print(cnt)