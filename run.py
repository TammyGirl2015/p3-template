from random import randint

# Options for player to input
t = ["rock", "paper", "scissors"]

# Function to display game instructions
def game_instructions():
    print("\nWelcome to Rock-Paper-Scissors.")
    print("Type in rock, paper or scissors in lowercase. The Computer will randomly pick one of the three choices.\n")
    print("Rock crushes Scissors")
    print("Scissors cuts Paper")
    print("Paper covers Rock\n")
    print("The game is the best out of three and you can choose whether to continue playing or not. Good Luck!\n")

# Display game instructions
game_instructions()

# Computer chooses random option
computer = t[randint(0,2)]

player = False

while player == False:
    # While loop: sets the parameters for winning, losing, and tying for the player and the computer.
    # The code checks that the correct words, case sensitive, are input.
    # Returns error message if input is anything other than Rock, Paper, or Scissors.
    player = input("rock, paper, scissors? ").lower() 
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
        print("That's not a valid play. Choose rock, paper or scissors.")
    player = False 
    computer = t[randint(0,2)] 
