r = input()

shooting = list(r)

result = 0
point = 0

for i in shooting:
    if i == 'h':
        if point == -1:
            point = 1
        else:
            point += 1


    elif i == 'o':
        point = -1

    result += point

print(result)