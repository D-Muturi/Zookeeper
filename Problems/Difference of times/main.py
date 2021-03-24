hour1 = int(input())
minutes1 = int(input())
seconds1 = int(input())

hour2 = int(input())
minutes2 = int(input())
seconds2 = int(input())

total1_sec = hour1 * 60 * 60 + minutes1 * 60 + seconds1
total2_sec = hour2 * 60 * 60 + minutes2 * 60 + seconds2

print(total2_sec - total1_sec)

time = []

for i in range(6):
    time.append(int(input()))

first = time[:3]
sec = time[3:]

def calc(arr):
    hour = arr[0] * 60 * 60
    mins = arr[1] * 60
    sec = arr[2]

    return hour + mins + sec



t1 = calc(first)
t2 = calc(sec)

print(t2 - t1)

# print(abs(int(input()) * 3600 + int(input()) * 60 + int(input()) - int(input()) * 3600 - int(input()) * 60 - int(input())))

# a = int(input())
# b = int(input())
# c = int(input())
# a1 = int(input())
# b1 = int(input())
# c1 = int(input())
# print ((a1 * 3600 + b1 * 60 + c1)-(a * 3600 + b * 60 + c))