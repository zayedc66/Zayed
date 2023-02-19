#Made by Zayed
#2/8/2023
#Battleship
#spot=["o"]*25
import os, random, time
spot=[]
def start_game():
    #this method allows me to set all the spots on the board as the wave emoji
    spot=[]
    i=1 
    while i<=25:
        spot.append("🌊")
        spot.append("🌊")
        spot.append("🌊")
        spot.append("🌊")
        spot.append("🌊")
        i+=1
    return spot


def place_ships():
    ships=["💨"]*25
    ship_1=random.randint(1,11)
    ship_2=random.randint(1,11)
    while ship_1 ==ship_2:
        ship_2=random.randint(1,11)
    if ship_1 ==1 or ship_2==1:
        ships[0]="💥"
        ships[1]="💥"
    if ship_1 ==2 or ship_2==2:
        ships[5]="💥"
        ships[10]="💥"
    if ship_1 ==3 or ship_2==3:
        ships[6]="💥"
        ships[11]="💥"    
    if ship_1 ==4 or ship_2==4:
        ships[23]="💥"
        ships[24]="💥"
    if ship_1 ==5 or ship_2==5:
        ships[21]="💥"
        ships[11]="💥"
    if ship_1 ==6 or ship_2==6:
        ships[16]="💥"
        ships[13]="💥"
    if ship_1 ==7 or ship_2==7:
        ships[23]="💥"
        ships[19]="💥"
    if ship_1 ==8 or ship_2==8:
        ships[3]="💥"
        ships[12]="💥"
    if ship_1 ==9 or ship_2==9:
        ships[2]="💥"
        ships[5]="💥"
    if ship_1 ==10 or ship_2==10:
        ships[7]="💥"
        ships[18]="💥"
    if ship_1 ==11 or ship_2==11:
        ships[13]="💥"
        ships[17]="💥"
    return ships 
            
def display_board():
    i=0
    row=1
    print("|      A      B      C      D      E  |")
    print("|-------------------------------------|")
    while i<25:
        print(f"|{row} |   {spot[i]}  |  {spot[i+1]}  |  {spot[i+2]}  |  {spot[i+3]}  |  {spot[i+4]}|")
        i+=5
        row+=1
    print("|-------------------------------------|")
    print("Welcome to battleship! Enter a key, press N for new game, or press Q to quit")
          
        
def garbage_input():
    print("Bad Input")
    time.sleep(2)


try:
    spot=start_game()
    ships=place_ships()
    ship_1 = 2
    ship_2 = 2
    run=True
    while run:
        display_board()
        guess=input("Enter a coordinate(letter, number): ").upper()
        if len(guess)<1:
            garbage_input()
        elif guess=="N":
            spot=start_game()
            ships=place_ships()
        elif guess=="Q":
            run=False
            print("Thank you for playing!!")
            time.sleep(2)
        elif not guess[1].isnumeric():
            garbage_input()
        elif int(guess[1])>5:
            garbage_input()  
        else:
            letter = guess[0]
            number = guess[1]   
            if int(number) <=5:
                if letter == "a":
                    start = 0
                if letter == "b":
                    start = 1
                if letter == "c":
                    start = 2
                if letter == "d":
                    start = 3
                if letter == "e":
                    start = 4
                if ord(guess[0])>=65 and ord(guess[0])<=69:
                    start=ord(guess[0])-65
                    spot[start+(int(guess[1])-1)*5]=ships[start+(int(guess[1])-1)*5]
                    if spot[start+(int(guess[1])-1)*5]=="💥":
                        print("HIT!!")
                        time.sleep(1)
                    if spot[start+(int(guess[1])-1)*5]=="💨":
                        print("Miss")        
                        time.sleep(1)
            print(guess)     
        os.system("cls")
except:
    print("Please Enter A VAlid Guess!")
    os.system("cls")