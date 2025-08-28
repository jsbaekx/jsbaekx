def InputPoly(n):
    result = []
    for i in range(n):
        a, b = map(int, input().split())
        k = [a, b]
        result.append(k)
    return result

f1, n1 = input().split()
n1 = int(n1)

f = InputPoly(n1)

f2, n2 = input().split()
n2 = int(n2)

g = InputPoly(n2)

rst = []

for i in range(n1):
    for j in range(n2):
        if f[i][1] == g[j][1] and f[i][0] != 0 and g[j][0] != 0:
            h = [f[i][0] + g[j][0], f[i][1]]
            f[i][0], g[j][0] = 0,0
            rst.append(h)

for i in range(n1):
    rst.append(f[i])
for j in range(n2):
    rst.append(g[j])

ll = len(rst)
for i in range(ll):
    if rst[ll-i-1][0] == 0:
        del rst[ll-i-1]

lll = len(rst)

rst.sort(key=lambda x:-x[1])
if len(rst) != 0:
    print('s', lll)
    for i in range(lll):
        print(rst[i][0],rst[i][1])
else:
    print('0 0')