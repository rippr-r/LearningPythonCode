def addition(num1, num2):
    answer = num1 + num2
    print(f"Your answer for {num1} + {num2} is {answer}")

def subtraction(num1, num2):
    if num1 < num2:
        answer = num2 - num1
        print(f"Your answer for {num2} - {num1} is {answer}")
    else:
        answer = num1 - num2
        print(f"Your answer for {num1} - {num2} is {answer}")

def multiplication(num1, num2):
    answer = num1 * num2
    print(f"Your answer for {num1} * {num2} is {answer}")

def division(num1, num2):
    if num2 == 0:
        print("Can't divide by 0")
    else:
        if num1 < num2:
            answer = num2 / num1
            print(f"Your answer for {num2} / {num1} is {answer}")
        else:
            answer = num1 / num2
            print(f"Your answer for {num1} / {num2} is {answer}")

def intro():
    print("Welcome to the Basic Calculator")
    print("Please select what math you wnat to do!")
    select = int(input("1. Addition 2. Subtraction 3. Multiplication 4. Division: "))
    if 1 <= select <= 4:
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        second(select, num1, num2)
    else:
        print("Invalid choice, reselect your choice")
        intro()

def second(selected, num1, num2):
    match selected:
        case 1:
            addition(num1, num2)
        case 2:
            subtraction(num1, num2)
        case 3:
            multiplication(num1, num2)
        case 4:
            division(num1, num2)

def main():
    intro()

main()
