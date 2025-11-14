students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

total_class = 0

for s in range(1, students + 1):
    print("Student", s)
    total = 0
    for sub in range(1, subjects + 1):
        score = float(input("Enter score " + str(sub) + ": "))
        total += score
    avg = total / subjects
    print("Average for Student", s, "=", avg)
    total_class += avg

print("Class Average =", total_class / students)
