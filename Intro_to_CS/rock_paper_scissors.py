import random

welcome = """
************************************************************
*                                                          *
*        Welcome to the Rock, Paper, Scissors Game!        *
*                                                          *
************************************************************
"""
print(welcome)

options = ['rock', 'paper', 'scissors']

def game_play():
    print("Select number of players")
    print()
    number_of_players = int(input("1 player OR 2 players (1/2): "))
    print()
    

    if number_of_players == 1:        
        while True:
            print("You will now play against computer")
            print()
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

    elif number_of_players == 2:
        while True:
            player_1 = None
            player_2 = None
            print()
            while player_1 not in options:
                print("Player_1's Turn")
                player_1 = input("Rock, Paper, or Scissors: ").lower()
            print()
            while player_2 not in options:
                print("Player_2's Turn")
                player_2 = input("Rock, Paper, or Scissors: ").lower()
            print()
            def winner (player_1, player_2):
                print("Player_1: ", player_1)
                print("Player_2: ",  player_2)
                if player_1 == player_2:
                    print("Its a Tie!!")
                
                elif player_1 == "rock":
                    if player_2 == "paper":
                        print("Player_2 Wins")
                    else:
                        print("Player_1 Wins")

                elif player_1 == "paper":
                    if player_2 == "scissors":
                        print("Player_2 Wins")
                    else:
                        print("Player_1 Wins")

                elif player_1 == "scissors":
                    if player_2 == "rock":
                        print("Player_2 Wins")
                    else:
                        print("Player_1 Wins")
                    
            winner(player_1, player_2)

            play_again = input("Want to play again? Yes/No: ").lower()

            if play_again != "yes":
                break

game_play()