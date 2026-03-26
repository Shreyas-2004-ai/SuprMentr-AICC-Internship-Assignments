# Student Data Manager (Improved Version)

def get_student_data():
    students = []

    n = int(input("Enter number of students: "))

    for i in range(n):
        print(f"\nEnter details for Student {i+1}")
        name = input("Name: ")
        marks = float(input("Marks: "))

        student = {
            "name": name,
            "marks": marks
        }
        students.append(student)

    return students


def calculate_average(students):
    total = sum(s["marks"] for s in students)
    return total / len(students)


def find_topper(students):
    return max(students, key=lambda s: s["marks"])


def find_lowest(students):
    return min(students, key=lambda s: s["marks"])


def assign_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"


def display_results(students):
    print("\n--- Student Results ---")

    for s in students:
        grade = assign_grade(s["marks"])
        print(f"{s['name']} - Marks: {s['marks']} - Grade: {grade}")

    avg = calculate_average(students)
    topper = find_topper(students)
    lowest = find_lowest(students)

    print("\n--- Summary ---")
    print(f"Class Average: {avg:.2f}")
    print(f"Topper: {topper['name']} with {topper['marks']} marks")
    print(f"Lowest Scorer: {lowest['name']} with {lowest['marks']} marks")


# Run program
students = get_student_data()
display_results(students)