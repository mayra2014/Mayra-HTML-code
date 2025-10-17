import random
def guess_number():
    computer=random.randint(1,1000)
    attempts=0
    guess=None
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 1000.")
    while guess != computer:
        try:
            guess=int(input("Please enter your guess, lets see if its correct!:"))
            attempts+=1
            if guess < computer:
                print("Too low! Please Try again.")
            elif guess > computer:
                print("Too high! Please try again.")
            else:
                print(f"Congratulations! You've guessed the number {computer} in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 100")
guess_number()
            