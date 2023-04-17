#Made by Zayed
#Date: Jan 12 2023
#Purpose: Databasing



import os, time, sys, sqlite3
Student_Data = False
Options = False
score = False
menu = True
listing = False
addition = False
student_grades = {}


Student_Data = ["Andrea", "Dylan", "Coltina", "Dawson", "Carter", "Zayed", "Hayden", "Owen", "Erik", "Gabe", "Christian", "Noah", "Theerth", "Sujen", "Thirn" ]

def create_connection(db_file):
    #create a database connection to the SQLite database
    #return: Connection object or None
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    return conn


def create_table(conn,table, columns):
    col = ",".join(columns)
    sql = f'''CREATE TABLE IF NOT EXISTS {table}( id INTEGER PRIMARY KEY, {col});'''
    conn.execute(sql)


def insert_db(conn,table, columns,data):
    sql=f'''INSERT INTO {table} {tuple(columns)} VALUES {tuple(data)};'''
    conn.execute(sql)
    conn.commit()


def select_db(conn,table,columns_and_data=None):
    if not columns_and_data==None:
        col = " AND ".join(columns_and_data)
        sql=f'''SELECT * FROM {table} WHERE {col}'''
        return conn.execute(sql)
    else:
        sql =f"SELECT * from {table}"
        return conn.execute(sql)
   
def delete_db(conn,table,column,what_to_remove):
    sql=f'''DELETE FROM {table} WHERE {column} = {what_to_remove}'''
    conn.execute(sql)
    conn.commit()  


def update_db(conn,table,columns_and_data,where_to_update):
    col = ",".join(columns_and_data)
    sql = f"UPDATE {table} set {col} where {where_to_update}"
    conn.execute(sql)
    conn.commit()


connection = create_connection("db_file.db")
create_table(connection,"studentbook",["first TEXT","last TEXT","result TEXT","PHYSICS REAL","CHEMISTRY REAL","FRENCH REAL","MATH REAL","AVERAGE REAL"])
results=select_db(connection,"studentbook").fetchall()
Students = list(map(list, results))

'''
insert_db(connection,"studentbook",["first","last","Result", "PHYSICS", "CHEMISTRY", "FRENCH", "MATH", "AVERAGE"],["Yeast", "Dune", "Passed", 80.0, 79.0, 83.0, 72.0, 78.5])
insert_db(connection,"studentbook",["first","last","Result", "PHYSICS", "CHEMISTRY", "FRENCH", "MATH", "AVERAGE"],["Noel", "Noa", "Passed", 83.0, 95.0, 92.0, 94.0, 91])
insert_db(connection,"studentbook",["first","last","Result", "PHYSICS", "CHEMISTRY", "FRENCH", "MATH", "AVERAGE"],["Cris", "Ron", "Failed", 37.0, 23.0, 51.0, 46.0, 39.3])
insert_db(connection,"studentbook",["first","last","Result", "PHYSICS", "CHEMISTRY", "FRENCH", "MATH", "AVERAGE"],["Leo", "Mane", "Passed", 19.0, 77.0, 80.0, 83.0, 64.8])
insert_db(connection,"studentbook",["first","last","Result", "PHYSICS", "CHEMISTRY", "FRENCH", "MATH", "AVERAGE"],["Tyrone", "Ream", "Failed", 5.0, 15.0, 13.0, 7.0, 10.0])
'''

def add_student():
   os.system('cls')
   Student_Data = list(map(list,results))
   print("\nAdding student \n")
   f_name = input("Student First Name: ")
   l_name = input("Student Last Name: ")
   os.system('cls')  
   valid=False
   marks = True
   while marks == True:  
               os.system('cls')
               print("Enter the marks for tests 1-4")
               try:      
                   PHYSICS = float(input("PHYSICS mark %: "))
                   CHEMISTRY = float(input("CHEMISTRY mark %: "))
                   FRENCH = float(input("FRENCH mark %: "))
                   MATH = float(input("MATH mark %: "))
                   valid=True
               except:
                   os.system('cls')
                   valid=False
                   print("please enter marks in numerical format, ##.# or ##")
                   time.sleep(2)
               if valid == True and PHYSICS in range(0,101) and CHEMISTRY in range(0,101) and FRENCH in range(0,101) and MATH in range(0,101):
                   os.system('cls')
                   student_avg = (PHYSICS + CHEMISTRY + FRENCH + MATH)/4
                   if student_avg >= 50:
                       passed = "Passed"
                   elif student_avg < 50:
                       passed = "Failed"            
                   print(f"{f_name} {l_name} {passed} with an overall mark of: {student_avg} %" )
                   insert_db(connection,"studentbook", ["first","last","result","PHYSICS","CHEMISTRY","FRENCH","MATH","AVERAGE"],[f_name,l_name,passed,PHYSICS,CHEMISTRY,FRENCH,MATH,student_avg])
                   confirm = input("Enter 'E' to add student to database OR Enter 'N' to cancel (will return you to menu!): ").upper()
                   if confirm == "E":
                       os.system('cls')
                       #Student_Data.append([f_name,l_name,passed,PHYSICS,CHEMISTRY,FRENCH,CHEMISTRY,student_avg])
                       main()
                       os.system('cls')
                   else:
                       print("Student was not added to list..... Returning to main menu.....")
                       os.system('cls')
                       main()

'''
def list_student():
   os.system('cls')
   Student_Data = list(map(list,results))
   for row in Student_Data:
       print(row)
       print(f""" First Name:{row[0]}\n Last Name:{row[1]}\n {row[2]}\n
       PHYSICS------>{row[3]}%\n
       CHEMISTRY--->{row[4]}%\n
       FRENCH--->{row[5]}%\n
       MATH------->{row[6]}%\n
       STUDENT AVERAGE--->{row[7]}%\n----------------------------""")
   back = input("Press the enter key to go back to menu...")
   os.system('cls')
   main()
'''

def list_student():
    print('\x1bc')
    results=select_db(connection,"Students_table").fetchall()
    Students = list(map(list, results))
    for row in Students:
        print(f" First Name:{row[1]}\n Last Name:{row[2]}\n {row[3]}\n MATH------>{row[4]}%\n ENGLISH--->{row[5]}%\n HISTORY--->{row[6]}%\n GYM------->{row[7]}%\n STUDENT AVERAGE--->{row[8]}%\n----------------------------") 
    goback = input("Press the enter key to go back to menu...")
    menu()

def Student_Average():
    correctInput = False
    choice = False
    counter = 0
    Student_Data = list(map(list,results))
    for x in Student_Data:
        print(str(counter) + ": " + x[0])
        counter += 1
    while correctInput == False:
        choice = input("Enter number that corresponds to the student: ")
        if choice.isnumeric() and int(choice) in range(0, counter, 1):
            choice = int(choice)
            correctInput = True
        else:
            print("Invalid Input. Try again")
    print(str(Student_Data[choice][5]))  


def course_average():
   courses = ["Physics", "Chemistry", "French", "Math"]
   Student_Data = list(map(list,results))
   for i in courses:
           x = 0
           for student in Student_Data:
               x += student[courses.index(i) + 4]    
           print (f"{i} avg: {x / len(Student_Data)}")
           #len(studentData)
   back = input("Press any key to go back to menu...")
   main()


def quit():
   os.system('cls')  
   print("Application Shutting Down...")
   time.sleep(2)
   os.system('cls')  
   sys.exit()
   
dic = {1:add_student,2:list_student,3:course_average,4:quit,5:Student_Average}


def main():
    global Student_Data
    correctInput = False
   # intro print statement
    Student_Data = list(map(list,results))
    while correctInput == False:
        print("\nWelcome to Student Grades Program \n\n-----------------------------------\n1) Add Student to list (Calculates Student Average) \n2) List Students + Student Average \n3) Course Average\n4) Exit Program\n-----------------------------------")
        user_input = input("Choose one of the four avaliable options: ")
        if user_input.isnumeric():
            if int(user_input) in range(1,5):
                correctInput = True
                user_input=int(user_input)
        else:
            print("Invalid Input. Try again")
    dic[user_input]()


while True:
    main()
    add_student()
    Student_Average()  
    course_average()
    list_student()