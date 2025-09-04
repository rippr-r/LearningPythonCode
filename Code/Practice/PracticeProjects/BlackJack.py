## My have bugs, wanting to go back at a leter date and debug and change up logic.

import random

money = 1000
playerHand = []
dealerHand = []

def dealCard():
    card = random.randint(1, 10) #Aces are counted as 1
    return card

def cases(num):
    match num:
        case 1:
            deposit()
        case 2:
            gamble()
        case 3:
            print("Exiting....")
            exit()

def deposit():
    global money
    depo = int(input("How much would you like to deposit?: "))
    money += depo
    intro()

def gamble():
    global money
    global playerHand
    global dealerHand

    playerHand.clear()
    dealerHand.clear()

    user = 0
    deal = 0

    bet = int(input("How much do you want to bet?: "))
    print(" ")

    p = 0
    while p < 2:
        playerHand.append(dealCard())
        p += 1

    d = 0
    while d < 2:
        dealerHand.append(dealCard())
        d += 1

    while True:
        user = sum(playerHand)
        deal = sum(dealerHand)
        if user > 21:
            print(f"You have {user}, You lose. \n")
            money -= bet
            break
        print(f"You have {user}, the dealer has {deal} ")
        choice = int(input("What would you like to do? \n1. Hit\n2. Stand\n"))
        if choice == 1:
            playerHand.append(dealCard())
            user = sum(playerHand)
            if user > 21:
                print(f"You have {user}, You lose. \n")
                money -= bet
                break
            elif user == 21:
                print("Blackjack! You win!")
                money += bet * 2
                break
        elif choice == 2 and user <= 21:
            stand(bet)
            break
        else:
            print("Invalid choice, try again.")

    intro()

def stand(bet):
    global money
    user = sum(playerHand)
    dealer = sum(dealerHand)

    while dealer < 17:
        print("Dealer hits.")
        dealerHand.append(dealCard())
        dealer = sum(dealerHand)
        print(f"Dealer now has {dealer}")

    if dealer > 21:
        print("Dealer busts! You win!")
        money += bet * 2
    elif dealer == user:
        print(f"Push! Both have {user}.")
    elif dealer > user:
        print(f"Dealer wins with {dealer} over your {user}.")
        money -= bet
    else:
        print(f"You win with {user} over dealer's {dealer}!")
        money += bet * 2
    intro()

def intro():
    print("Welcome to blackjack!")
    print(f"You have {money} in your account. \nWhat would you like to do?\n ")
    print("1. Deposit\n2. Gamble\n3. Exit")
    choice = int(input(" "))
    if 1 <= choice <= 3:
        cases(choice)
    else:
        print("Enter a valid choice.\n")
        intro()

intro()
