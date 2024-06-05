import random
user_choice = int(input("Enter your choice: Type 0 for rock, 1 for paper, 2 for scissors "))
if  user_choice>=3 or user_choice <0:
    print("Invalid choice, you loose")
else:
    computer_choice = random.randint(0,2)
print("Computer Chose:")
print(computer_choice)
if computer_choice == user_choice:
    print("It's a draw.")
elif computer_choice > user_choice:#2>0
    print("You Lose.")
elif user_choice > computer_choice:
    print("You Win.")
elif computer_choice == 0 and user_choice ==2:
    print("You Lose.")
elif user_choice ==0 and computer_choice == 2:
    print("You win.")


