student_name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")
num_subjects = int(input("Enter number of subjects: "))

subject_marks = {}
for i in range(num_subjects):
    sub_name = input(f"Enter Subject {i + 1} Name: ")
    marks = float(input(f"Enter Marks obtained in {sub_name}: "))
    subject_marks[sub_name] = marks

total_marks = 0.0
for marks in subject_marks.values():
    total_marks += marks

max_possible_marks = num_subjects * 100.0
percentage = (total_marks / max_possible_marks) * 100.0

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 43:
    grade = "D"
else:
    grade = "F (Fail)"

print("\n==================================")
print("           MARKSHEET              ")
print("==================================")
print(f"Student Name : {student_name}")
print(f"Roll Number  : {roll_number}")
print("----------------------------------")
for sub, marks in subject_marks.items():
    print(f"{sub:<15} : {marks}/100")
print("----------------------------------")
print(f"Total Marks  : {total_marks}/{max_possible_marks}")
print(f"Percentage   : {percentage:.2f}%")
print(f"Final Grade  : {grade}")
print("==================================")