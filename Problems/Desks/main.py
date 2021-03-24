first_group = abs(int(input()))
second_group = abs(int(input()))
third_group = abs(int(input()))

desk1 = (first_group - (first_group % 2)) // 2
desk2 = (second_group - (second_group % 2)) // 2
desk3 = (third_group - (third_group % 2)) // 2

sum_desk = (desk1 + (first_group % 2)) + (desk2 + (second_group % 2)) + (desk3 + (third_group % 2))

print(sum_desk)

# class1_student_count = int(input())
# class2_student_count = int(input())
# class3_student_count = int(input())

# class1_bench_count = (class1_student_count // 2) + (class1_student_count % 2)
# class2_bench_count = (class2_student_count // 2) + (class2_student_count % 2)
# class3_bench_count = (class3_student_count // 2) + (class3_student_count % 2)

# print(class1_bench_count + class2_bench_count + class3_bench_count)

class_sizes = [int(input()) for classroom in range(3)]

desks = [
    (n_students + 1) // 2
    for n_students in class_sizes
]

print(sum(desks))

n1_students = int(input())
n2_students = int(input())
n3_students = int(input())

print((n1_students // 2) + (n1_students % 2) + (n2_students // 2) + (n2_students % 2) + (n3_students // 2) + (n3_students % 2))

total_deck = 0
for _ in range(3):
    people = abs(int(input()))
    deck = people // 2
    deck = (deck + 1)\
        if (deck * 2 < people)\
        else deck
    total_deck += deck

print(total_deck)

