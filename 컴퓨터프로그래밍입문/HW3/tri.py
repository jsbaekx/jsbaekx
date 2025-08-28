a, b, c = input().split()

n1 = int(a)
n2 = int(b)
n3 = int(c)

if n1 < n2:
    temp = n1
    n1 = n2
    n2 = temp

if n2 < n3:
    temp = n2
    n2 = n3
    n3 = temp

if n1 < n2:
    temp = n1
    n1 = n2
    n2 = temp

if n1 >= n2 + n3:
    result = 0

elif n1**2 == n2**2 + n3**2:
    result = 1

elif n1**2 > n2**2 + n3**2:
    result = 2

elif n1**2 < n2**2 + n3**2:
    result = 3

print(result)