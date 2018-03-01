def get_students():
    student_tup = ("Omar", "Akbar", "Anthony")

    return student_tup


def get_student_points(stds_tup):
    points = []
    for std in stds_tup:
        point = int(input("Enter " + std + "'s points: "))
        points.append(point)

    return points


def get_letter_grade(points):
    grades = []
    for point in points:
        if 0 <= point <= 59:
            grades.append("F")
        elif 60 <= point <= 69:
            grades.append("D")
        elif 70 <= point <= 79:
            grades.append("C")
        elif 80 <= point <= 89:
            grades.append("B")
        elif 90 <= point <= 100:
            grades.append("A")
    return grades

def main():
    my_students = get_students()
    #print(my_students)

    #print(my_points)
    grade_sheet = []
    # point_sheet = list(zip(my_students, my_points))
    # for std,pts in point_sheet:
    #     print(std,pts)
    while True:
        course_points = []
        course = input("Enter the course name: ")
        my_points = get_student_points(my_students)
        my_grade = get_letter_grade(my_points)
        course_points.append(course)
        course_points.append(my_students)
        course_points.append(my_points)
        grade_sheet.append(course_points)
        loop_again = input("Do you want to enter another course? Y/N: ").upper()
        if loop_again != "Y":
            break

    #print(point_sheet)
    for course_info in grade_sheet:
        print("Course: \t{}".format(course_info[0])) # There is only 1 course name for all students so let's print it & get rid of it
        course_info.pop(0)
        for index, std in enumerate(course_info[0]):
            print("\t{} - {}".format(std,course_info[1][index]))
        print("\n")


if __name__ == "__main__":
    main()