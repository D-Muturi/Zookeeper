n = int(input())
a = 1

while a < n:
    if a % 2 == 0:
        print(a)
    else:
        pass

    a += 1

n = int(input())
s = 2
while s < n:
    print(s)
    s += 2

n = int(input())

for i in range(2, n, 2):
    print(i)