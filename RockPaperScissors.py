import random
choices = ["Rock", "Paper", "Scissors"]

player = False
player_scr = 0
comp_scr = 0
while True:
    player = input("Rock, Paper or Scissors:\n").capitalize()
    comp = random.choice(choices)
    print(comp)
    if player == comp:
        print("Tied!!")
    elif player == "Rock":
        if comp == "Paper":
            print("You lose :(", comp , "covers", player)
            comp_scr += 1
        else:
            print("You win !!", player, "Smashes", comp)
            player_scr += 1
    elif player == "Paper":
        if comp == "Scissors":
            print("You lose :(", comp, "Cuts", player)
            comp_scr += 1
        else:
            print("You win !!", player, "covers", comp )
            player_scr += 1
    elif player == "Scissors":
        if comp == "Rock":
            print("You lose :(",comp, "smashes", player)
            comp_scr += 1
        else:
            print("You win !!", player , "Cuts", comp)
            player_scr += 1
    elif player == "End":
        print("Final Scores:\n")
        print("Player:", player_scr)
        print("CPU:",comp_scr)
        break
if player_scr > comp_scr:
    print("Yay!! You won.")
elif comp_scr > player_scr:
    print("Duh... Better luck next time.")
else:
    print("Scores Level")

