students = []

first_student = input("Enter the first student's name: ")
students.append(first_student)

second_student = input("Enter the second student's name: ")
students.append(second_student)

third_student = input("Enter the third student's name: ")
students.append(third_student)

print(students)

students[1] = "Samantha"
print(students)

new_student = input("Enter the new student's name: ")
index_text = input("Enter the insertion index (starting at 0): ")
insertion_index = int(index_text)

students.insert(insertion_index, new_student)
print(students)

del students[0]
print(students)

waitlist = []

moved_student = students.pop()
waitlist.append(moved_student)

print(f"Moved to the waitlist: {moved_student}")
print(f"Roster: {students}")
print(f"Waitlist: {waitlist}")

moved_student = students.pop(0)
waitlist.append(moved_student)

print(f"Roster: {students}")
print(f"Waitlist: {waitlist}")

cancelled_student = input("Who is leaving the waitlist? ")
waitlist.remove(cancelled_student)

print(f"Waitlist: {waitlist}")
