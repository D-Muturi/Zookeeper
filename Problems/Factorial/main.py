inp = int(input())
i = 1
fct = 1
while inp > i:
    fct *= inp
    inp -= 1
print(fct)

num = int(input())
fac = 1
i = 1
while i <= num:
    if num <= 100:
        fac = fac * i
    i = i + 1
    if num > 100:
        print()
print(int(fac))

N = int(input())
factorial_n = 1
count = 1
while count <= N:
    factorial_n *= count
    count += 1
print(factorial_n)


N = int(input())
y = 1
x = 1

while x <= N:
    y = y * x
    x = x + 1

print(y)

N = int(input())
factorial = 1
while N > 0:
    factorial *= N
    N -= 1
print(factorial)