num = list(map(int, input().split()))

sum = 0
for n in num:
    sum += n*n

print(sum%10)