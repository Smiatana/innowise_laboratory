students = []

def get_student(name):
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    return None

def calculate_average(grades):
    return (lambda g: sum(g) / len(g) if g else 0)(grades)

def add_student():
    name = input("Enter student name: ")
    if get_student(name):
        print("Student already exists.")
    else:
        students.append({"name": name, "grades": []})
        print(f"Student '{name}' added.")

def add_grade():
    name = input("Enter student name: ")
    student = get_student(name)
    if not student:
        print("Student not found.")
        return
    try:
        grade = float(input("Enter grade (0-100): "))
        if 0 <= grade <= 100:
            student["grades"].append(grade)
            print(f"Grade {grade} added to {name}.")
        else:
            print("Grade must be between 0 and 100.")
    except ValueError:
        print("Invalid grade. Please enter a number.")

def show_report():
    if not students:
        print("No students to report.")
        return
    print("\n--- Student Report ---")
    total_grades = []
    for student in students:
        avg = calculate_average(student["grades"])
        total_grades.extend(student["grades"])
        print(f"{student['name']}: Grades = {student['grades']}, Average = {avg:.2f}")
    overall_avg = calculate_average(total_grades)
    print(f"\nOverall Average Grade: {overall_avg:.2f}")

def top_performer():
    if not students:
        print("No students available.")
        return
    top_student = None
    top_avg = -1
    for student in students:
        avg = calculate_average(student["grades"])
        if avg > top_avg:
            top_avg = avg
            top_student = student
    if top_student:
        print(f"Top Performer: {top_student['name']} with average grade {top_avg:.2f}")
    else:
        print("No grades available to determine top performer.")

def run_menu():
    while True:
        print("\n--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add a grade for a student")
        print("3. Generate a full report")
        print("4. Find the top student")
        print("5. Exit program")

        try:
            choice = int(input("Choose an option (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            add_student()
        elif choice == 2:
            add_grade()
        elif choice == 3:
            show_report()
        elif choice == 4:
            top_performer()
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose between 1 and 5.")

if __name__ == '__main__':
    run_menu()
