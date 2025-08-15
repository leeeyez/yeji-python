n = int(input())
words = [input() for _ in range(n)]

word = list(set(words))

result = sorted(word, key=lambda x: (len(x), x))

for r in result:
    print(r)