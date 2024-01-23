import random

options = ['rock', 'paper', 'scissors']

while True:
    computer = random.choice(options)
    player = None

    while player not in options:
        player = input("Rock, Paper, or Scissors: ").lower()


    def winner(computer, player):
        print("Computer: ", computer)
        print("Player: ",  player)
        if player == computer:
            print("Its a Tie!!")
        
        elif player == "rock":
            if computer == "paper":
                print("You Lose")
            else:
                print("You Win")

        elif player == "paper":
            if computer == "scissors":
                print("You Lose")
            else:
                print("You Win")

        elif player == "scissors":
            if computer == "rock":
                print("You Lose")
            else:
                print("You Win")
            
    winner(computer, player)

    play_again = input("Want to play again? Yes/No: ").lower()

    if play_again != "yes":
        break