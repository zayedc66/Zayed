import os
import time
import numpy as np

studentData = [
    ["John", "Doe", "Passed", 80.0, 79.0, 83.0, 72.0, 78.5],
    ["Jane", "Doe", "Passed", 83.0, 95.0, 92.0, 94.0, 91],
    ["George", "Python", "Failed", 37.0, 23.0, 51.0, 46.0, 39.3],
    ["Luke", "Skywalker", "Passed", 19.0, 77.0, 80.0, 83.0, 64.8],
    ["Teerth", "Panchal", "Failed", 5.0, 15.0, 13.0, 7.0, 10.0]
]

# initial variables
menu = True
start = False
add = False
list_stud = False
Course_avg = False
login = False
wel_msg = "WELCOME TO STUDENT GRADES PROGRAM\n"
start == True


def main():
    # intro print statement
    print("\nWelcome to Student Grades Program \n\n-----------------------------------\n1) Add Student to list \n2) List Students + Student Average \n3) Course Average\n4) Exit Program\n-----------------------------------")
    user_input = int(input("Please input your desired option: "))
    check_user_input(user_input)

    # if type(user_input) == int:
    #     num = int(user_input)
    #     check_user_input(num)
    # else:
    #     print("misinpit")
    
    
def check_user_input(user):
    match user:
        case 1:
            add_student()
        case 2:
            list_student()
        case 3:
            course_average()
        case 4:
            quit()
        case _:
            try:
                user_input = int(input("Sorry, there seems to be a misinput. Retry: ")) 
                check_user_input(user_input)
            except Exception as x:
                print(x)


def add_student():
    print("add")
    print(studentData)
    keepAdding = 1
    first = input('Plz give first')
    last = input('Plz give last')
    status = input('Plz give first')
    grades = input('Plz give grades').split(' ') 
    while keepAdding == 1:
        studentData.append([first,last,status, grades])
        keepAdding = input('keep adding? 0 or 1')
        
        


def list_student():

    for row in studentData:

        print(f""" First Name:{row[0]}\n 
        Last Name:{row[1]}\n {row[2]}\n 
        MATH------>{row[3]}%\n 
        ENGLISH--->{row[4]}%\n 
        HISTORY--->{row[5]}%\n 
        GYM------->{row[6]}%\n 
        STUDENT AVERAGE--->{row[7]}%\n
        ----------------------------""") 


def student_average(student_data):

    print("student average")
    


def course_average():
    print("course average")
    # can be hardcoded


main()