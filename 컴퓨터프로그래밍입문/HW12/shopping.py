def similarity(a, b):
    return len(a & b) / (len(a | b) + 1)

shop_list = []
M_list = []
f_list = []
try:
    while(True):
        max_sim = 0
        m_list = []
        Flag = True
        shop = input().split()
        a = shop.pop(0)
        for i in range(len(shop)):
            shop[i] = int(shop[i])
        shop.insert(0, a)
        if len(shop_list) == 0:
            shop_list.append(shop)
            continue
        for i,j in enumerate(shop_list):
            if j[0] == shop[0]:
                shop_list[i].extend(shop[1:])
                Flag = False
        if (Flag):
            shop_list.append(shop)
        for i, j in enumerate(shop_list):
            if i == len(shop_list) - 1:
                break
            for l, k in enumerate(shop_list[i+1:]):
                s = similarity(set(j[1:]), set(k[1:]))
                if s == max_sim:
                    m_list.append([i, l+i+1])
                if s > max_sim:
                    max_sim = s
                    m_list = []
                    m_list.append([i, l+i+1])
        M_list = []
        for i in m_list:
            M_list.append([shop_list[i[0]][0], shop_list[i[1]][0]])
        for i, j in enumerate(M_list):
            if j[0] > j[1]:
                temp = M_list[i][0]
                M_list[i][0] = M_list[i][1]
                M_list[i][1] = temp
        f_list = sorted(M_list, key=lambda x : (x[0], x[1]))
except:
    for i in f_list:
        print(i[0], i[1])
