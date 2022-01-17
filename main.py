import random

print(("-" * 30) + "\nRock, Paper, Scissors\n" + ("-" * 30))

user_score, computer_score = 0, 0

while True:
    print("1 Rock , \n2 Paper , \n3 Scissors")
    user_choice = input("Your choice: ")
    computer_choice = random.choice(["1", "2", "3"])

    if user_choice == "1":
        if computer_choice == "1":
            print("Computer's choice: Rock , Scoreless!")

        elif computer_choice == "2":
            print("Computer's choice: Paper , You lose!")
            computer_score += 100

        elif computer_choice == "3":
            print("Computer's choice: Scissors , You win!")
            user_score += 100

    elif user_choice == "2":
        if computer_choice == "1":
            print("Computer's Choice : Rock , You Win!")
            user_score += 100
        elif computer_choice == "2":
            print("Computer's Choice : Paper , Scoreless!")
        elif computer_choice == "3":
            print("Computer's Choice : Scissors , You Lost!")
            computer_score += 100

    elif user_choice == "3":
        if computer_choice == "1":
            print("Computer's Choice : Rock , You Lost!")
            computer_score += 100
        elif computer_choice == "2":
            print("Computer's Choice : Paper , You Win!")
            user_score += 100
        elif computer_choice == "3":
            print("Computer's Choice : Scissors , Scoreless!")
    else:
        break

    print("User's Score : {} \nComputer's Score : {}".format(user_score, computer_score))

