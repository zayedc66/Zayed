import os
import time

studentData = [
    ["Yeast", "Dune", "Passed", 80.0, 79.0, 83.0, 72.0, 78.5],
    ["Noel", "Noa", "Passed", 83.0, 95.0, 92.0, 94.0, 91],
    ["Cris", "Ron", "Failed", 37.0, 23.0, 51.0, 46.0, 39.3],
    ["Leo", "Mane", "Passed", 19.0, 77.0, 80.0, 83.0, 64.8],
    ["Tyrone", "Ream", "Failed", 5.0, 15.0, 13.0, 7.0, 10.0]
]

#initial variables
options = True
initiate = False
addition = False
listing = False
course_avg = False
welcome = "WELCOME TO STUDENT GRADES PROGRAM\n"
initiate = True


def main():
    # intro print statement
    print("\nWelcome to Student Grades Program \n\n-----------------------------------\n1) Add Student to list (Calculates Student Average) \n2) List Students + Student Average \n3) Course Average\n4) Exit Program\n-----------------------------------")
    user_input = int(input("Please input your desired option: "))
    check_user_input(user_input)
    
#parentheses tell Python to execute the named function rather than just refer to the function    
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
    os.system('cls')
    print("\nAdding student \n")
    f_name = input("Student First Name: ")
    l_name = input("Student Last Name: ")
    os.system('cls')    
    valid=False
    mrks = True
    while mrks == True:    
                os.system('cls')
                print("Enter the marks for tests 1-4") 
                try:        
                    MATH = float(input("MATH mark %: "))
                    ENGLISH = float(input("ENGLISH mark %: "))
                    HISTORY = float(input("HISTORY mark %: "))
                    GYM = float(input("GYM mark %: "))
                    valid=True
                except:
                    os.system('cls') 
                    valid=False
                    print("please enter marks in numerical format, ##.# or ##")
                    time.sleep(2)
                if valid == True and MATH in range(0,100) and ENGLISH in range(0,100) and HISTORY in range(0,100) and GYM in range(0,100):
                    os.system('cls')
                    student_avg = (MATH + ENGLISH + HISTORY + GYM)/4
                    if student_avg >= 50:
                        passed = "Passed"
                    elif student_avg < 50:
                        passed = "Failed"             
                    print(f_name,l_name,passed,"with an overall mark of: ",student_avg,"%" )
                    confirm = input("Enter 'Y' to add student to database OR Enter 'N' to cancel (will return you to menu!): ").upper()
                    if confirm == "Y":
                        os.system('cls')
                        studentData.append([f_name,l_name,passed,MATH,ENGLISH,HISTORY,GYM,student_avg ])
                        main()
                        os.system('cls')
                    else:
                        print("Student was not added to list..... Returning to main menu.....")
                        os.system('cls')
                        main()

def list_student():
    os.system('cls')
    for row in studentData:
        print(f""" First Name:{row[0]}\n Last Name:{row[1]}\n {row[2]}\n 
        MATH------>{row[3]}%\n 
        ENGLISH--->{row[4]}%\n 
        HISTORY--->{row[5]}%\n 
        GYM------->{row[6]}%\n 
        STUDENT AVERAGE--->{row[7]}%\n----------------------------""")
    back = input("Press the enter key to go back to menu...")
    os.system('cls')
    main() 


def course_average():
    courses = ["Math", "English", "History", "Gym"]
    for i in courses:
            x = 0
            for student in studentData:
                x += student[courses.index(i) + 3]      
            print (f"{i} avg: {x / studentData}") 
            #len(studentData)
    back = input("Press any key to go back to menu...")
    main()

def quit():
    os.system('cls')    
    print("Application Shutting Down...")
    time.sleep(2)
    os.system('cls')    
    print("Shut down")

main()