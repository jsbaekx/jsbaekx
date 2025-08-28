M, N = map(int, input().split())
mm = M-1
nn = N
num = 1
m=0
n=-1
pan = []

for i in range(M):
    line = []
    for j in range(N):
        line.append(0)
    pan.append(line)

if nn % 2 == 0:
    nnn = nn + 1
else:
    nnn = nn

if mm % 2 == 0:
    mmm = mm + 1
else:
    mmm = mm


try:
    while(True):
        if nn == 0:
            raise Exception


        for i in range(nn):
            n += (-1) ** (nnn+1)
            pan[m][n] = num
            num += 1


        nn -= 1
        nnn += 1

        if mm == 0:
            raise Exception

        for j in range(mm):
            m += (-1) ** (mmm+1)
            pan[m][n] = num
            num += 1


        mm -= 1
        mmm += 1


except Exception:

    for k in range(4):
        a = list(map(int, input().split()))
        if len(a) == 1:
            if a[0] > (M*N):
                print(0,0)
                continue
            for i in range(M):
                for j in range(N):
                    if pan[i][j] == a[0]:
                        break
                if pan[i][j] == a[0]:
                    ii = i
                    jj = j
                    break
            print(ii+1, jj+1)
        elif len(a) == 2:
            print(pan[a[0]-1][a[1]-1])