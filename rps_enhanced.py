import random
import color

print(
    f"""
 |||||||| ||     || ||||||||     |||     ||||||   |||||||| ||    || ||||||||  |||||||  |||||||| 
    ||    ||     || ||          || ||   ||    ||  ||       |||   ||    ||    ||     || ||    || 
    ||    ||     || ||         ||   ||  ||        ||       ||||  ||    ||           ||     ||   
    ||    ||||||||| ||||||    ||     || ||   |||| ||||||   || || ||    ||     |||||||     ||    
    ||    ||     || ||        ||||||||| ||    ||  ||       ||  ||||    ||           ||   ||     
    ||    ||     || ||        ||     || ||    ||  ||       ||   |||    ||    ||     ||   ||     
    ||    ||     || ||||||||  ||     ||  ||||||   |||||||| ||    ||    ||     |||||||    ||   

    
Welcome to my rock paper scissors game!

{"*"*60} 
Rules:
-You can type only "Rock", "Paper", "Scissors" for inputs
-You can play how many times you want
-Have fun!
{"*"*60} 
 """
)

# ! Only change TIE, LOSE or WIN. Don't mess with R_P_S or game won't work
R_P_S = ["Rock", "Paper", "Scissors"]
TIE = "It is tie"
LOSE = "I win"
WIN = "You win"


def Main():
    result = 0
    computer = random.choice(R_P_S)
    player = input("Your choice: ")
    TEXT = f"I choose {computer}, you choose, {player}."
    return Game(computer, player, TEXT)


def Game(computer, player, TEXT):
    if player == "Scissors":
        if computer == "Paper":
            print(f"{TEXT} {WIN}")
            return Try_again(1)
        if computer == "Rock":
            print(f"{TEXT} {LOSE}")
            return Try_again(0)
        if computer == "Scissors":
            print(f"{TEXT} {TIE}")
            return Try_again(2)

    elif player == "Rock":
        if computer == "Scissors":
            print(f"{TEXT} {WIN}")
            return Try_again(1)
        if computer == "Paper":
            print(f"{TEXT} {LOSE}")
            return Try_again(0)
        if computer == "Rock":
            print(f"{TEXT} {TIE}")
            return Try_again(2)

    elif player == "Paper":
        if computer == "Rock":
            print(f"{TEXT} {WIN}")
            return Try_again(1)
        if computer == "Scissors":
            print(f"{TEXT} {LOSE}")
            return Try_again(0)
        if computer == "Paper":
            print(f"{TEXT} {TIE}")
            return Try_again(2)

    else:
        print(f"{color.RED}\nInvalid input\n{color.END}")
        return Main()


def Try_again(result):
    if result == 1:
        print("\n\nCongratulations. You won!")
    elif result == 0:
        pass  # You can add something for losing the game here # ! Remove "pass".
    elif result == 2:
        pass  # You can add something for tie up the game here # ! Remove "pass".

    play_again = input("Do you want to try again, yes or no? : ")

    if play_again == "yes":
        Main()
    elif play_again == "no":
        print("Okay good byee")
    else:
        print(f"{color.RED}\nInvalid input\n{color.END}")


Main()
