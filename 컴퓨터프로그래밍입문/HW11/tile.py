count = 0
n = map(int, input().split())
tile_n = list(n)
tile = []
count = len(tile_n) - 1

for i in range(count):
    r = []
    for t in range(tile_n[0]):
        r.append(0)
    tile.append(r)

for k in range(count):
    for u in range(tile_n[k]):
        tile[k][u] = 1
result = []
for i in range(tile_n[0]):
    r_count = 0
    for j in range(count):
        if tile[j][i] == 1:
            r_count += 1
    result.append(r_count)

s_result = ' '.join(map(str, result)) + ' 0'
print(s_result)
