n = int(input())
year = 0
while int(n) < 700000:
    n = n + n * (7.1 / 100)
    year += 1
print(year)

x = 700000
years = 0
money = int(input())

while money < 700000:
    money *= 1.071
    years += 1

print(years)

sum_deposit = int(input())
years = 0
value_protected = 700000
interest_rate = 0.071
if 50000 <= sum_deposit <= value_protected:
    while sum_deposit <= value_protected:
        sum_deposit += (sum_deposit * interest_rate)
        years += 1
print(years)