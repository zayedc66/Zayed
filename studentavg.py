#student averages program
#Program by Zayed
#Date: 2 / 21 / 2023
import os, time
#for catching any misinputs 
try:    
    Students=[["Tyteth","Bob","Pass",80,70,83,72,78],["Leslie", "Jone", "Pass",95,90,93,89,75],["Rock", "Coop", "Fail",84,28,39,21],["Maria", "Silva", "Pass",84,59,71,91,58],["Aaliyah","Rob","Fail",48,29,57,29,59]]
    menu = True
    start = False
    add = False
    list_stud = False
    Course_avg = False
    login = False
    wel_msg = "Welcome to The application\n"
    while login == False:
            start = True
            login = True
    while start == True:  
        while menu == True:
            os.system('cls')
            print("\nWelcome to Student Grades Program \n\n-----------------------------------\n1)Add Student to list \n2)List Students + Student Average \n3)Course Average\n4)Exit Program\n-----------------------------------")
            try:  
                menu_sel = (input("\nEnter 1,2,3 or 4 : "))
                menu_sel=int(menu_sel)
                if menu_sel == 1:   
                    add = True
                    menu = False
                elif menu_sel == 2:
                    list_stud = True
                    menu = False
                elif menu_sel == 3:
                    Course_avg = True
                    menu = False
                elif menu_sel == 4:
                    os.system('cls')
                    menu = False
                    start = False
                else:
                    os.system('cls')
                    print(menu_sel,"is not a valid menu option")
                    time. sleep(2)        
            except Exception as e:
                os.system('cls')
                if not menu_sel == "4":
                    print(menu_sel,"is not a valid menu option")
                time. sleep(2)
                os.system('cls')    
        while add == True:
            os.system('cls')
            print("\nAdding student \n")
            f_name = input("Student First Name: ")
            l_name = input("Student Last Name: ")
            os.system('cls')    
            valid=False
            mrks = True
            while mrks == True:    
                os.system('cls')
                print("Now you will enter the marks for tests 1-4")
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
                        confirm = True
                    else:
                        confirm = False
                        print("Student was not added to list..... Returning to main menu.....")
                        time.sleep(2)
                        valid = False
                        add = False
                        mrks == False
                        menu = True    
                    try:  
                        while confirm == True:
                            os.system('cls') 
                            try:
                                Students.append([f_name,l_name,passed,MATH,ENGLISH,HISTORY,GYM,student_avg ])
                                valid = False 
                                add = False
                                mrks = False
                                menu = True   
                                confirm = False  
                                print("Student added, would you like to view list?")
                                list2 = input("'Y' for yes or 'N' for no: ").upper()
                                if list2 == "Y":
                                    valid = False
                                    mrks = False
                                    add = False                                    
                                    list_stud = True
                                    confirm = False                                    
                                else:
                                    valid = False
                                    add = False
                                    mrks = False
                                    menu = True 
                                    confirm = False                                                                       
                            except:
                                print("Student could not be added!....")
                                valid = False 
                                add = False
                                mrks = False
                                menu = True  
                                confirm = False                                          
                    except:
                            print("Student could not be added!....")
                            time.sleep(2)
                            valid = False
                            add = False
                            mrks = False
                            menu = True 
                            valid = False
                else:
                    os.system('cls')
                    print("One of your marks is out of range, 0 to 100") 
                    time.sleep(2)
        while list_stud == True:
            os.system('cls')
            for row in Students:
                print(f" First Name:{row[0]}\n Last Name:{row[1]}\n {row[2]}\n MATH------>{row[3]}%\n ENGLISH--->{row[4]}%\n HISTORY--->{row[5]}%\n GYM------->{row[6]}%\n STUDENT AVERAGE--->{row[7]}%\n----------------------------") 
            back = input("Press any key to go back to menu...")
            menu = True
            list_stud = False
        while Course_avg == True:
            os.system('cls')
            Math_avg = 0
            English_avg = 0
            History_avg = 0
            Gym_avg = 0
            try:
                print("Math----------> 1)\nEnglish-------> 2)\nHistory-------> 3)\nGym-----------> 4)\nAll Courses---> 5)\n")
                course_sel = int(input("Which course do you want to find the average for?: ")) 
                os.system('cls')               
                for row in Students:
                        Math_avg += row[3] 
                for row in Students:
                        English_avg += row[4]
                for row in Students:    
                        History_avg += row[5]
                for row in Students:   
                        Gym_avg += row[6]
                if course_sel >= 1 and course_sel <=5:
                    if course_sel == 1:                               
                        print(f"Math Average: {Math_avg // len(Students)} %")
                    elif course_sel == 2:                        
                        print(f"English Average: {English_avg // len(Students)} %")
                    elif course_sel == 3:                        
                        print(f"History Average: {History_avg // len(Students)} %")
                    elif course_sel == 4:                        
                        print(f"Gym Average: {Gym_avg // len(Students)} %")
                    elif course_sel == 5:
                        print(f"Math Average: {Math_avg // len(Students)} %")
                        print(f"English Average: {English_avg // len(Students)} %")
                        print(f"History Average: {History_avg // len(Students)} %")
                        print(f"Gym Average: {Gym_avg // len(Students)} %")
                    time.sleep(2)
                    moveon = input("Press any key to continue: ")
                    Course_avg = False
                    list_stud = True
                else:
                    print("Not in range of options....")
                    time.sleep(2)                       
            except:
                print("not a valid selection")            
except:
    print("PROGRAM ENDED")           
    