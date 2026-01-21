##
#  Manage student grades.
#

# Use a dictionary named 'grades' to track student grades.
# code grades: dict = {}


# Loop until the user chooses to quit.
# Check user input for the following "(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? "
# Prevent unexected inputs by converting input to upper-case
# code here
user_input: str = ""
while user_input != "Q":
    user_input = input("(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? ").strip()[0].upper()

    # Use a condition to handle adding a new student.
    # Convert grade into integer
    # Gather user input for "Enter the name of the student: "
    # Check if student name already exists "Sorry, that student is already present."
    # Gather user input for student grade "Enter the student's grade: "
    # Validate input is in correct format or range, if not notify "Please enter grade as number 0-100"
    # code here
    if user_input == "A":
        student_name: str = input("Enter the name of the student: ")
        student_grade: int = int(input("Enter the student's grade: "))
        if student_name in grades:
            print("Sorry, that student is already present.")
        elif student_grade < 0 or student_grade > 100:
            print("Please enter grade as number 0-100")
        else:
            grades[student_name] = student_grade


    # Handle removing a student if user inputs 'R'
    # Check input for "What student do you want to remove? "
    # use pop to remove key/value form grades
    # see notes https://www.programiz.com/python-programming/methods/dictionary/pop
    # Check if student doesn't exist - "Sorry, that student doesn't exist and couldn't be removed."
    # code here
    elif user_input == "R":
        student_name: str = input("What student do you want to remove? ")
        if student_name not in grades:
            print("Sorry, that student doesn't exist and couldn't be removed.")
        else:
            grades.pop(student_name)


    # Handle modifying a student grade if user inputs 'M'
    # "Enter the name of the student to modify: "
    # Convert grade into integer
    # If student is in grades dictionary, show existing grade "The old grade is"
    # Gather input for new grade "Enter the new grade: "
    # If student doesn't exist "Sorry, that student doesn't exist and couldn't be modified."
    # code here
    elif user_input == "M":
        student_name: str = input("Enter the name of the student to modify: ")
        if student_name not in grades:
            print("Sorry, that student doesn't exist and couldn't be modified.")
        else:
            print(f"The old grade is {grades[student_name]}")
            new_grade: int = int(input("Enter the new grade: "))
            if student_grade < 0 or student_grade > 100:
                print("Please enter grade as number 0-100")
            else:
                grades[student_name] = new_grade


    # Handle printing grade average as a string if user input is 'P'
    # Use "The average grade is "
    # Handle printing all of the student names with associated grade
    # Display explictly as strings
    # code here
    elif user_input == "P":
        total_grade: int = 0
        total_students: int = len(grades)
        # Loop for calculating average
        for student, grade in grades.items():
            total_grade += grade
        average_grade: float = total_grade / total_students
        print(f"The average grade is {average_grade:.1f}")
        # Loop for printing out each student's grade
        for student, grade in grades.items():
            print(f"{student}: {grade}")



    # Handle the case for quiting if user inputs 'Q' "Goodbye!"
    # code here
    elif user_input == "Q":
        print("Goodbye!")


    # Handle the case of invalid input. "Sorry, that wasn't a valid choice."
    # code here
    if user_input not in ["A", "R", "M", "P", "Q"]:
        print("Sorry, that wasn't a valid choice.")