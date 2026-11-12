from student import Student


def add_student(students, student_id, name, age, grade):
    for s in students:
        if s.student_id == student_id:
            print(f"Error: Student ID {student_id} already exists!")
            return students
    new_student = Student(student_id, name, age, grade)
    students.append(new_student)
    print(f"Added student: {new_student}")
    return students


def search_student(students, keyword):
    kw = keyword.lower()
    return [
        s for s in students
        if kw in s.student_id.lower() or kw in s.name.lower()
    ]


def main():
    print("=" * 50)
    print("STUDENT MANAGER - DevOps Lab 5")
    print("=" * 50)

    students = [
        Student("SV001", "Nguyen Van A", 20, "K20"),
        Student("SV002", "Tran Thi B", 21, "K20"),
        Student("SV003", "Le Van C", 19, "K21"),
    ]

    students = add_student(students, "SV004", "Pham Thi D", 22, "K19")

    print("\nStudent List:")
    for s in students:
        print(f"  {s}")
    print(f"\nTotal: {len(students)} students")

    print("\n--- Search: Van ---")
    for r in search_student(students, "Van"):
        print(f"  Found: {r}")


if __name__ == "__main__":
    main()
