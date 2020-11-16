from random import randint
t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)]
player = False

while player == False:
     player = input("Rock, Paper, Scissors?")
     if player == computer:
         print("Tie, Re-do")
     elif player == "Rock":
         if computer == "Paper":
                print("Defeat!", computer, "covers", player)
         else:
            print("Victory!", player, "crushes", computer)
     elif player == "Paper":
        if computer == "Scissors":
            print("Defeat!", computer, "cut", player)
        else:
            print("Victory!", player, "covers", computer)
     elif player == "Scissors":
        if computer == "Rock":
            print("Defeat!", computer, "crushes", player)
        else:
            print("Victory!", player, "cut", computer)
     else:
        print("Misspell,try again!")
     player = False
     computer = t[randint(0,2)]
        
