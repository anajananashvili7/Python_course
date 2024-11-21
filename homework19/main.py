import json
from models import Student, Address

# Creating student instances
students = [
    Student("Paata", 87, Address("Tbilisi", "Saburtalo")),
    Student("Demetre", 100, Address("Tbilisi", "Gldani-7-11-4-93")),
    Student("Alexander", 100, Address("Tbilisi", "Gldani-7-11-4-93")),
    Student("Teona", 92, Address("Tbilisi", "Gldani-7-11-4-93")),
    Student("Nino", 99, Address("Tbilisi", "Leselidzs str. 25")),
    Student("Andria", 87, Address("Tbilisi", "Varketili IV 407-5-123")),
]

# Saving data to JSON
with open("students.json", "w") as file:
    json.dump([student.to_dict() for student in students], file, indent=2)

# Reading from JSON
with open("students.json", "r") as file:
    students_data = json.load(file)

# Modifying student data
def calculate_grade(mark):
    if mark >= 91:
        return "A"
    elif mark >= 81:
        return "B"
    elif mark >= 71:
        return "C"
    else:
        return "D"

for student in students_data:
    student["mark"] += 1  # Example change
    student["grade"] = calculate_grade(student["mark"])

# Saving updated data back to JSON
with open("students.json", "w") as file:
    json.dump(students_data, file, indent=2)
