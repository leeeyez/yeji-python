# IOIOI
# S 안에 Pn이 몇 군데 포함되어 있는지 구하기

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()

# 50점 답안 - 시간 복잡도 O(n x m)
# pn = "IO" * n + "I"  # pn 문자열 만들기
# len_pn = 2*n + 1     # pn의 길이

# # 인자가 pn 문자열을 만족하면 1 아니면 0을 리턴하는 함수
# def checkPn(checkstr):
#     if checkstr == pn:
#         return 1
#     else: return 0


# cnt = 0
# for i in range(m - len_pn + 1):
#     if s[i] == 'I': # 모든 pn은 I로 시작하므로 I일 때 checkpn
#         cnt += checkPn(s[i:i+len_pn])

# print(cnt)


cnt = 0
i = 0

while i < m - 2:
    if s[i:i+3] == "IOI":  # IOI 패턴 발견 (모든 pn이 포함함)
        pattern_count = 0
        
        # 연속된 OI 개수 세기
        while i + 2 < m and s[i:i+3] == "IOI": # +2했을 때 범위 벗어나지 않는지 확이
            pattern_count += 1
            i += 2  # IO만큼 건너뛰기
            
            # pn을 만족하면 카운트
            if pattern_count == n:
                cnt += 1
                pattern_count -= 1  # 겹치는 패턴 고려
        
    i += 1

print(cnt)