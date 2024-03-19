from random import randint

"""
Options for player to input
"""

t = ["rock", "paper", "scissors"]

"""
Computer chooses random option
"""

computer = t[randint(0,2)]

player = False

while player == False:
    """
    While loop: sets the parameters for winning, losing and tying for the player and the computer. 
    The code checks that the correct words, case sensitive, are input. 
    Returns error message if input is anything other than Rock, Paper or Scissors.
    """
    player = input("rock, paper, scissors?")
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    player = False
    computer = t[randint(0,2)]
    

