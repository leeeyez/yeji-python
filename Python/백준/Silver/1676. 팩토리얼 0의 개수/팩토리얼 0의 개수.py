n = int(input())

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)

nfac = str(fac(n))
count = 0
for i in range(len(nfac)):
    if nfac[len(nfac)-1-i] == "0":
        count += 1
    else:
        break

print(count)