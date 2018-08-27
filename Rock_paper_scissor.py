import random
game_score=[0,0] 
# 0th index belongs to user and 1st index belongs to computer
l=[1,2,3]
# 1 for Scissors, 2 for Paper , 3 for Rock
def print_status_of_computer(comp):
    if comp==1:
        print("Computer had selected 'Scissors'")
    elif comp==2:
        print("Computer had selected 'Paper'")
    else:
        print("Computer had selected 'Rock'")
        
def play_game(user,comp):
    computer_score=0
    user_score=0
    if(user==1 and comp==3 or user==2 and comp==1 or user==3 and comp==2):
        computer_score+=1
    elif(user==1 and comp==2 or user==2 and comp==3 or user==3 and comp==1 ):
        user_score+=1
    else:
        pass
    return [user_score, computer_score]

Flag=True
while(Flag):
    user=int(input("Enter 1 for scissors\nEnter 2 for paper\nEnter 3 for Rock\n"))
    comp=random.choice(l)
    if(user<4):
        print_status_of_computer(comp)
        x=play_game(user,comp)
        print(x)
        game_score[0]+=x[0]
        game_score[1]+=x[1]
        choice=input("Do you want to play again,\n then press 'Y or y' for yes or 'N or n'for no\n")
        if choice.lower()=='y':
            continue
        else:
            if(game_score[0]>game_score[1]):
                print("User won :) ")
                
            elif(game_score[0]<game_score[1]):
                print("Computer Won :) , user lost :( , try again ")
            else:
                print(" Draw Match")
            print(game_score)
            Flag=False
    else:
        print("The input which you have give is out of range, pls give input only in numbers \n(1-Scissors,2-Paper,3-Rock)") 
          
