import csv

CSV_FILE = 'students.csv'

def add_student(id, name, age, grade, subject_name, mark):
    # Check if a student with the given ID already exists
    existing_student = read_students(student_id=id)
    if existing_student:
        print(f"Student with ID {id} already exists. Skipping addition.")
        return
    
    # If the student doesn't exist, add them to the CSV file
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, name, age, grade, subject_name, mark])
    
    # Sort students by ID after adding the new student
    sort_students_by_id()

def sort_students_by_id():
    with open(CSV_FILE, mode='r') as file:
        rows = list(csv.reader(file))
        header = rows[0]
        data = sorted(rows[1:], key=lambda x: int(x[0]))  # Sort by ID (first column)
        
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

def read_students(student_id=None):
    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)
        if student_id:
            for row in reader:
                if int(row[0]) == student_id:
                    return {header[i]: row[i] for i in range(len(header))}
            return None
        else:
            return [dict(zip(header, row)) for row in reader]

def calculate_average_marks(subject_name):
    total_marks = 0
    count = 0
    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if row[4] == subject_name:
                total_marks += int(row[5])
                count += 1
    return total_marks / count if count > 0 else 0

def update_student_mark(student_id, subject_name, new_mark):
    rows = []
    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if int(row[0]) == student_id and row[4] == subject_name:
                row[5] = new_mark  # Update the mark for the specified student and subject
            rows.append(row)
    
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)


if __name__ == "__main__":
    # Add a new student
    add_student(1, 'John Doe', 20, 'Sophomore', 'Math', 85)
    add_student(2, 'Jane Smith', 22, 'Senior', 'Physics', 90)

    # Attempt to add a student with an existing ID (This will be skipped)
    add_student(1, 'Jack Brown', 19, 'Freshman', 'Math', 92)

    # Read all students
    all_students = read_students()
    print("All Students:", all_students)

    # Read a specific student
    student = read_students(1)
    print("Student 1:", student)

    # Calculate average marks for a subject
    average_math_marks = calculate_average_marks('Math')
    print("Average Math Marks:", average_math_marks)

    # Update a student's mark
    update_student_mark(1, 'Math', 95)
    updated_student = read_students(1)
    print("Updated Student 1:", updated_student)
