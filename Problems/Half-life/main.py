initial = int(input())
final = int(input())
i = 0

while initial >= final:
    initial = initial // 2
    i += 1

print(i * 12)

Qi, Qf = int(input()), int(input())
half_lifes = 0
if 2 <= Qi <= 1000000:
    while Qi >= Qf:
        half_lifes += 1
        Qi = Qi / 2
print(half_lifes * 12)

init = int(input())
final = int(input())
period = 0

while init >= final:
    period += 1
    init //= 2

result = period * 12
print(result)