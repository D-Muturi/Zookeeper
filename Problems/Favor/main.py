k = int(input().strip())
num = 0
total = 0
while num <= k:
    total += num
    num += 1
print(total)

x = int(input())
i = x
j = list()
while i >= 0:
    z = x - i
    j.append(z)
    i -= 1
print(sum(j))

n = int(input())
s = 0
while n > 0:
    s += n
    n -= 1
print(s)

k = int(input())
natural_numbers = list(range(k + 1))
print(sum(natural_numbers))

k = int(input())
# count = 1
# while count <= k:
#    sum1 += count
#    count += 1
# print(sum1)
print((k * (k + 1)) // 2)