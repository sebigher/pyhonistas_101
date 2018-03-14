
import random
game_choices = ["rock", "paper", "scissors"]

# computer = random.choice(game_choices);
#
# myTurn = input("your turn: ")
# print("your turn: ", myTurn )


user_choice = input("give your choice: ")
print("your choice is: ", user_choice)

# if user_choice == "rock":
#     print("ok:", user_choice)
# else:
#     print("nok", "please, try again")

# not enough for many choices
# if user_choice == "rock":
#     print("ok:", user_choice)
# elif user_choice == "paper":
#     print("ok:", user_choice)
# elif user_choice == "scissors":
#     print("ok:", user_choice)
# else:
#     print("nok", "please try again")

# we will use random range
# index_random = random.randint(0, 2)
# cpu_choose = game_choices[index_random]
# print("cpu choose: ", cpu_choose)

user_choice = ''
while user_choice != "rock" and \
        user_choice != "paper" and \
        user_choice != "scissors":
    user_choice = input('rock, paper or scissors?')

# more directly
computer_choice = random.choice(game_choices)


print("computer shows: ", computer_choice)
print("user shows: ", user_choice)

if computer_choice == user_choice:
    winner = "tie"
    print("we have a tie")
elif computer_choice == "rock" and user_choice == "scissors":
    winner = "computer"
    print("1 computer won")
elif computer_choice == "scissors" and user_choice == "paper":
    winner = "computer"
    print("2 computer won")
elif computer_choice == "paper" and user_choice == "rock":
    winner = "computer"
    print("3 computer won")
else:
    winner = "user"
    print("user won")

print("results... winner is: ", winner)
