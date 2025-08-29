lines = []

while True:
    line = input()
    if line == ".":
        break
    lines.append(line)

for l in lines:
    p = []
    balance = True

    for w in l:
        if w == "[" or w == "(":
            p.append(w)
        elif w == "]":
            if not p or p[-1] != "[": # p가 비었거나 [이 아닐때
                balance = False
                break
            p.pop()
        elif w == ")":
            if not p or p[-1] != "(":
                balance = False
                break
            p.pop()

    if balance and not p: # 균형이 맞고 p에 아무것도 없을 때
        print("yes")
    else:
        print("no")   