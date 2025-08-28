def i(n):
    r=[]
    for _ in range(n):
        f = int(input())
        g = input().split()
        for k in range(len(g)):
            if g[k] == '$':
                break
            g[k] = int(g[k])
        g.append(f)
        r.append(g)
    return r

def a(f,g):
    r=[];x=y=0
    while 1:
        if x==len(f):r+=g[y:];break
        if y==len(g):r+=f[x:];break
        if f[x][1]==g[y][1]:
            c=f[x][0]+g[y][0]
            if c:r+=[[c,f[x][1]]]
            x+=1;y+=1
        elif f[x][1]>g[y][1]:
            r+=[f[x]];x+=1
        else:
            r+=[g[y]];y+=1
    return r

def polymult(f, g):
    r=[]
    for x in f:
        t=[[x[0]*y[0],x[1]+y[1]]for y in g]
        t.sort(key=lambda z:-z[1])
        r=a(r,t)
    return r

def polyadd(f, g):
    r = []
    for a in f:
        for b in g:
            if a[1] == b[1] and a[0] and b[0]:
                r.append([a[0] + b[0], a[1]])
                a[0] = b[0] = 0

    r += f + g
    r = [x for x in r if x[0]]
    r.sort(key=lambda x: -x[1])
    return r

_,n=input().split();f=i(int(n))
_,m=input().split();g=i(int(m))
rst = []
for i in f:
    for j in g:
        iii = i[:-2]
        jjj = j[:-2]
        ii = [[x, y] for x, y in zip(iii[0::2], iii[1::2])]
        jj = [[x, y] for x, y in zip(jjj[0::2], jjj[1::2])]
        t = polymult(ii, jj)
        t.append('$')
        t.append(i[-1]+j[-1])
        for u,k in enumerate(rst):
            if k[-1] == t[-1]:
                t = polyadd(t[:-2], k[:-2])
                t.append('$')
                t.append(k[-1])
                del rst[u]
                break
        rst.append(t)
rrst = sorted(rst, key=lambda x: x[-1], reverse=True)
print('s', len(rrst))
for i in rrst:
    print(i[-1])
    s = ' '.join(map(str, sum(i[:-2], [])))
    print(s, '$')
