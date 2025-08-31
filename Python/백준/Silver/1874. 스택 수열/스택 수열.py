n = int(input())
seq = [int(input()) for _ in range(n)]

num = 1
stack = []
result = []

def push_num(x):
    stack.append(x)
    result.append("+")

def pop_num():
    stack.pop()
    result.append("-")

for s in seq:
    # s가 등장할 때까지 push (1 ~ s)
    while num <= s:
        push_num(num)
        num += 1

    # stack이 비어있지 않고, 가장 마지막 원소가 s일 경우 pop
    if stack and stack[-1] == s:
        pop_num()
    else: # num이 s보다 큰 상황인데, pop할 수 없으면 아예 불가능
        print("NO")
        exit(0) # break하게 되면 아래의 result print하는 for문이 실행됨

for r in result:
    print(r)