"""
Author: Phuc Tran
Program: Student's GPA
Purpose: Test If the Student Qualifies for Either the Dean's List or the Honor Roll
"""


def main():
    last_name = input("Enter Student's Last Name or ZZZ to Quit: ")

    while last_name != "ZZZ":
        first_name = input("Enter First Name: ")

        while True:
            try:
                student_gpa = float(input("Enter GPA: "))
            except ValueError:
                print("Wrong data type! Please Enter Number for GPA (0.00 to 4.00).")
                continue
            else:
                if 3.5 <= student_gpa <= 4.0:
                    print(first_name + " " + last_name + " Has Made The Dean's List.\n")
                elif 3.25 <= student_gpa < 3.5:
                    print(first_name + " " + last_name + " Has Made The Honor Roll.\n")
                else:
                    print(first_name + " " + last_name + " Has Made Neither the Dean’s List nor the Honor Roll.\n")
                break

        last_name = input("Enter Next Student's Last Name or ZZZ to Quit: ")


main()


