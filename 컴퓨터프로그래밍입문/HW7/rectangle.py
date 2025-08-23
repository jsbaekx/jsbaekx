for i in range(4):
    a = map(int, input().split())
    a = list(a)
    r1 = a[:4]
    r2 = a[4:]

    x1 = range(r1[0], r1[2]+1)
    y1 = range(r1[1], r1[3]+1)

    x2 = range(r2[0], r2[2]+1)
    y2 = range(r2[1], r2[3]+1)

    rst1 = len(set(x1) & set(x2))
    rst2 = len(set(y1) & set(y2))

    if rst1 * rst2 == 1:
        print("POINT")
    elif rst1 > 1 and rst2 > 1:
        print('FACE')
    elif rst1 > 1 and rst2 == 1:
        print('LINE')
    elif rst1 == 1 and rst2 > 1:
        print('LINE')
    else:
        print('NULL')
