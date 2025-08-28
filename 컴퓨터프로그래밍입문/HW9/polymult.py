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

_,n=input().split();f=i(int(n))
_,m=input().split();g=i(int(m))
r=[]
for x in f:
    t=[[x[0]*y[0],x[1]+y[1]]for y in g]
    t.sort(key=lambda z:-z[1])
    r=a(r,t)
print('s',len(r)if r else 1)
print(*r[0]) if not r else [print(*x) for x in r]