with open('genome.txt', 'r') as f:
    g = f.read().splitlines()
    G = "".join(g)


def fstr(S, key):
    r = []
    i = 0
    while True:
        n = S[i:].find(key)
        if n == -1:
            break
        r.append(n + i)
        i += n + len(key)
    return r


S = input().split()
E = input().split()
S_r = []
E_r = []

for i in S:
    S_r.append(fstr(G, i))
for i in E:
    E_r.append(fstr(G, i))

Mlen = float('inf')
M_list = []
SE_all = set(S + E)

for k, i in enumerate(S_r):
    for j in i:
        ss = len(S[k])
        for n, l in enumerate(E_r):
            for m in l:
                if j >= m:
                    continue
                substr_len = m - j
                if substr_len < ss:
                    continue
                substr = G[j + ss:m]

                if any(x in substr for x in SE_all if len(x) <= substr_len):
                    continue

                total_len = m - j + len(E[n])
                if total_len < Mlen:
                    Mlen = total_len
                    M_list = [G[j:m + len(E[n])]]
                elif total_len == Mlen:
                    M_list.append(G[j:m + len(E[n])])

print(min(M_list))
