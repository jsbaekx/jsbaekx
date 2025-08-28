def i(n):
 r=[]
 for _ in range(n):
  x=int(input());p=input().split()[:-1]
  r+=[[x,[[int(p[i]),int(p[i+1])]for i in range(0,len(p),2)]]]
 return r

def a(x,y):
 d={}
 for c,p in x+y:d[p]=d.get(p,0)+c
 return[[c,p]for p,c in d.items()if c]

def m(x,y):
 d={}
 for a,p in x:
  for b,q in y:
   z=p+q
   d[z]=d.get(z,0)+a*b
 return[[c,p]for p,c in d.items()if c]

def mm(f,g):
 d={}
 for x,a1 in f:
  for y,a2 in g:
   z=x+y
   t=m(a1,a2)
   d[z]=a(d[z],t)if z in d else t
 return d

def o(d):
 r=[[x,sorted(y,key=lambda z:-z[1])]for x,y in d.items()if y]
 r.sort(reverse=1)
 if not r:print('0 0');return
 print('s',len(r))
 for x,y in r:
  print(x)
  for c,p in y:print(c,p,end=' ')
  print('$')

_,n=input().split();f=i(int(n))
_,n=input().split();g=i(int(n))
o(mm(f,g))