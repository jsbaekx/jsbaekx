month = int(input())

days = map(int, input().split())
days = list(days)

day = input()
day_list = ['월','화', '수', '목', '금', '토', '일']


now = 0
for i in day_list:
    if i == day:
        break
    now += 1

for k in range(3):

    f = now
    total_days = 0

    m, d = map(int, input().split())


    if mm > month:
        print("땡")
        continue

    for j in range(m-1):
        total_days += days[j]

    total_days += d-1

    result = total_days % 7
    f += result

    if f > 6:
        f = f-7

    rr = day_list[f]

    if d > days[m-1]:
        rr = '땡'

    print(rr)