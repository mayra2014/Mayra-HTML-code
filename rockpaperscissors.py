import random
def play():
    user=input("Enter your choice (rock, paper, scissors): ")
    computer=random.choice(['rock','paper','scissors'])
    print (f"user choice is: {user}") 
    print (f"computer choice is: {computer}")
    if user==computer:
        print("Its a tie!")
    elif (user=='rock' and computer=='scissors') or (user=='paper' and computer=='rock') or (user=='scissors' and computer=='paper'):
        print("you win!")
    else:
        print("computer wins!")
play()
    