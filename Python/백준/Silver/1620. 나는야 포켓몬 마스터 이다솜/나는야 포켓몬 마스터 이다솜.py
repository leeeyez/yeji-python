n,m = map(int, input().split())

# index()로 인한 시간초과
# pokemon = [input() for _ in range(n)]

# for _ in range(m):
#     q = input()
#     if q.isdigit(): # 숫자인 경우
#         print(pokemon[int(q)])
#     else:
#         print(pokemon.index(q) + 1)

# 양방향 dict 구조
# ex. 
# name_to_num = {"이상해씨": 1, "피카츄": 2, "파이리": 3}
# num_to_name = {1: "이상해씨", 2: "피카츄", 3: "파이리"}
pokemon = {}
pokemon_num = {}

for i in range(1, n+1):
    name = input()
    pokemon[name] = i
    pokemon_num[i] = name

for _ in range(m):
    q = input()
    if q.isdigit():
        print(pokemon_num[int(q)])
    else:
        print(pokemon[q])