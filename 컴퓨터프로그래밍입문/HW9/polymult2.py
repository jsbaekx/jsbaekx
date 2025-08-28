def InputPoly(n):
    r = []
    for i in range(n):
        a, b = map(int, input().split())
        r.append([a, b])
    return r

def polyadd(f, g):
    rst, a, b = [], 0, 0

    while (True):
        if f[a][1] == g[b][1]:
            rst.append([f[a][0] + g[b][0], f[a][1]])
            a += 1
            b += 1
        elif f[a][1] > g[b][1]:
            rst.append([f[a][0], f[a][1]])
            a += 1
        elif f[a][1] < g[b][1]:
            rst.append([g[b][0], g[b][1]])
            b += 1
        if a == len(f):
            rst.extend(g[b:])
            break
        if b == len(g):
            rst.extend(f[a:])
            break

    for i in range(len(rst) - 1, -1, -1):
        if rst[i][0] == 0:
            del rst[i]
    return rst

f1, n1 = input().split()
n1 = int(n1)

f = InputPoly(n1)

f2, n2 = input().split()
n2 = int(n2)

g = InputPoly(n2)

r = []

for i in range(n1):
    k = []
    for j in range(n2):
        k.append([f[i][0] * g[j][0], f[i][1] + g[j][1]])
    if i == 0:
        r = k
        continue
    r = (polyadd(r, k))

print('s', len(r))
for i in r:
    print(i[0], i[1])