"""
Tammy Metz
4-4-18

Lab for chapter 9
Creates a gradebook as a dictionary object to store key-value pairs of names and grade lists
"""

def main ():
    print("Welcome to your gradebook.")
    enter_another = 'y'
    grade_book = {}
    while enter_another == 'y':
        test_list = []
        name = input("Enter the student's name: ")
        for grade_no in range(3):
            test_list.append(int(input("Enter score for test #{}: ".format(grade_no+1))))
        grade_book[name] = test_list
        enter_another = input("Do you want to enter another student? ").lower()
    print("\nGrade Book Complete.")
    print("The grade book is")
    print(grade_book)

if __name__ == "__main__":
    main()