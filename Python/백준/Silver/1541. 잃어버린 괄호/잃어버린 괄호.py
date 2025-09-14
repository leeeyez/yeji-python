# 잃어버린 괄호
# 괄호 없는 식에 괄호를 적절히 넣어서 값을 최소로 만들기

exp_input = input()

# 00009 같은 형태를 9로 정수화 처리
tokens = []
num = ''
for ch in exp_input:
    if ch in '+-':
        if num:  # num이 있으면 연산자 앞까지 나온 숫자들을 token에 넣어줌 (int 처리 = 0009 같은 수 -> 9)
            tokens.append(str(int(num)))
            num = ''
        tokens.append(ch)  # 연산자 그대로 추가
    else:
        num += ch

if num:  # 마지막 숫자 처리
    tokens.append(str(int(num)))

exp = ''.join(tokens)

# ---------------------------------------------------------
# - 위치에 따라 계산하는 방법 : 틀림

# # -의 인덱스 위치를 저장
# minus = [i for i in range(len(exp)) if exp[i] == '-']

# # 최대수로 초기값 정의
# result = float('inf')

# # 각 - 인덱스를 기준으로 두 덩어리로 나누어 계산 후 뺄셈
# for midx in minus:
#     left = eval(exp[:midx])
#     right = eval(exp[midx+1:])

#     result = min(result, left - right) # 더 작은 수로 갱신

# print(result)
# ---------------------------------------------------------

# 첫 번째 '-' 기준으로 나누되,
# 오른쪽은 '-'를 모두 '+'로 바꿔 "모든 수의 합"으로 만든 뒤 한 번에 빼기
if '-' in exp:
    left, right = exp.split('-', 1)
    left_val = eval(left) if left else 0
    right_sum = eval(right.replace('-', '+')) if right else 0
    result = left_val - right_sum
else:
    result = eval(exp)

print(result)