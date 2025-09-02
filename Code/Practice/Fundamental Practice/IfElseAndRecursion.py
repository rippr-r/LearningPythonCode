import random

def boolRightNum(guess, number):
    if guess == number:
        return True
    elif guess > number:
        print("Number is less than your guess")
        return False
    elif guess < number:
        print("Number is greater than your guess")
        return False
    
def guessing(number):
    guess = int(input("Enter your guess: "))
    
    if boolRightNum(guess, number):
        print("You win!")
    else:
        guessing(number)

def main():
    print("Welcome to the guessing game!")
    number = random.randint(1,10)
    guessing(number)

main()
