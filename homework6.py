#1

my_dict = {
    "students": [
        {"id": 20, "name": "Giorgi", "age": 25},
        {"id": 25, "name": "Giorgi", "age": 23},
        {"id": 100, "name": "Nika", "age": 22},
        {"id": 56, "name": "Nika", "age": 25},
        {"id": 1232, "name": "Dato", "age": 22},
        {"id": 846723, "name": "Archili", "age": 32}
    ],
    "subjects": [
        {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "100": "A", "56": "B", "1232": "C", "846723": "A"}},
        {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "100": "A", "56": "B", "1232": "C", "846723": "B"}},
        {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "100": "A", "56": "A", "1232": "B", "846723": "A"}},
        {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
        {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
    ]
}

def print_student_info(student_id):
   
    student = next((s for s in my_dict["students"] if s["id"] == student_id), None)
    
    if student:
        print(f"Student Information:")
        print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")
        
       
        for subject in my_dict["subjects"]:
            grade = subject["grades"].get(str(student_id), "Not available")
            print(f"Subject: {subject['name']}, Grade: {grade}")
    else:
        print("Selected student ID not found.")

def main():
    
    student_ids = [student["id"] for student in my_dict["students"]]
    print("Student IDs:", ", ".join(map(str, student_ids)))
    
    
    chosen_id = int(input("Please choose a student ID: "))
    
    print_student_info(chosen_id)

if __name__ == "__main__":
    main()

