def InputPoly(n):
    result = []
    for i in range(n):
        a, b = map(int, input().split())
        result.append([a, b])
    return result

f1, n1 = input().split()
n1 = int(n1)

f = InputPoly(n1)

f2, n2 = input().split()
n2 = int(n2)

g = InputPoly(n2)

rst = []
a = 0
b = 0

while(True):
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
    if a == n1:
        rst.extend(g[b:n2])
        break
    if b == n2:
        rst.extend(f[a:n1])
        break

for i in range(len(rst)-1, 0-1, -1):
    if rst[i][0] == 0:
        del rst[i]
print(rst)