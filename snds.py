#Made by Zayed
#3 / 29 / 2023
#Search and Sort

import os, time, sys
Names = ["Andrea", "Dylan", "Coltina", "Dawson", "Carter", "Zayed", "Hayden", "Owen", "Erik", "Gabe", "Christian", "Noah", "Theerth", "Sujen", "Thirn" ]

# Selection sort in Python
# time complexity O(n*n)
#sorting by finding min_index
def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return


def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1
   
#find = input("Enter The Name You Would Like To Search")


def add_name():
    global if_on_list

    ent_name = str(input("Enter a name you would like to add to the list: "))        
    if_on_list = int(binary_search(Names,0,len(Names)-1,ent_name))
        
    if if_on_list == -1:
        Names.append(ent_name)
    elif not if_on_list == -1:
        print(ent_name,"is already on the list")


def sort():
    bubbleSort(Names)

    
def quit():
    print("Application Shutting Down...")
    time.sleep(2)
    os.system('cls')    
    print("Shut down")

def search():
    global look
    find = input("Enter the name to search: ")
    look = (binary_search(Names,0,len(Names)-1,find))
    if look == -1:
        print("Not in list")
    else:
        print(find,"Is already in the array")     
     
dic = {1:add_name,2:sort,3:search,4:quit,}
 

def menu():
    print (f"List Of Names: {Names}")
    correctInput = False
    #print intro statement
    while correctInput == False:
        print("-----------------------------------\n1) Add A Name To The List \n2) Sort The List (case sensitive) \n3) Search A Name On The List \n4) EXIT\n-----------------------------------")
        user_input = input("Please Choose One Of The Four Avaliable Options(Numbers: 1-4): ")
        if user_input.isnumeric():
            if int(user_input) in range(1,5):
                correctInput = True
                user_input=int(user_input)
            else:
                print("Please type given options within range(Numbers: 1-4): ")
        else:
            print("Invalid Input. Please Try Again")
    dic[user_input]()

while True:      
    menu()
    print("Loading...")
    time.sleep(3)
    os.system('cls')