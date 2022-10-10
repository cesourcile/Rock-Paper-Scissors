import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0


# Define parameters.
player_name = input("What is your name ?\n")

player = Player(player_name)
ia = Player("Computer")

choices = ["Rock", "Paper", "Scissors"]
choices_ascii = [
    """
             _______
        ---'   ____)
              (_____)
              (_____)
              (____)
         ---.__(___)
        """,
    """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """,
    """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """]

number_of_games = input("How many games do you want to play ?\n")

# Limiting number of games at 20.
if int(number_of_games) > 20:
    print("This is too much. Please choose a number of parties inferior at 20.")
    number_of_games = input("How many games do you want to play ?\n")

print(f"Okay ! To win, you must have a score equals to {number_of_games}.\n")

# Loop to play.
while player.score < int(number_of_games) and ia.score < int(number_of_games):

    # Time to choose.
    ia_choice = random.randint(0, 2)
    print("Choose between Rock, Paper and Scissors.\n")
    player_choice = input(f"{player_name} > ").capitalize()
    while player_choice not in choices:
        print("This is not Rock, Paper or Scissors. Please choose between those three.")
        print("Choose between Rock, Paper and Scissors.\n")
        player_choice = input(f"{player_name} > ").capitalize()

    print(f"{player_name} > You chose {player_choice}")

    # Determine a winner.
    for index, choice in enumerate(choices):

        if choice == player_choice:
            print(f"{choices_ascii[index]}")
            print(f"Computer > Computer chose {choices[ia_choice]}")
            print(f"{choices_ascii[ia_choice]}")

            if index == ia_choice:
                print("Equality !")

            elif index == 2 or ia_choice == 2:
                if ia_choice == 0 or index == 1:
                    print(f"{choices[ia_choice]} beats {player_choice}")
                    ia.score += 1

                else:
                    print(f"{player_choice} beats {choices[ia_choice]}")
                    player.score += 1

            elif index > ia_choice:
                print(f"{player_choice} beats {choices[ia_choice]}")
                player.score += 1

            elif index < ia_choice:
                print(f"{choices[ia_choice]} beats {player_choice}")
                ia.score += 1

    print(f"--------- {player_name} - {player.score} VS Computer - {ia.score} ---------")

if player.score == int(number_of_games):
    print("YOU WIN ! Congratulations !")
else:
    print("YOU LOSE ! Good luck for the next time.")

