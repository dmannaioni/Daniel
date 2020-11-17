from random import randint
t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)]
player = False

while player == False:
     player = input("Choose Rock, Paper or Scissors: ")
     if player == computer:
         print("Tie, Re-do")
         print(" ")
     elif player == "Rock":
         if computer == "Paper":
                print("Defeat!", computer, "covers", player)
                print(" ")
         else:
            print("Victory!", player, "crushes", computer)
            print(" ")
     elif player == "Paper":
        if computer == "Scissors":
            print("Defeat!", computer, "cut", player)
            print(" ")
        else:
            print("Victory!", player, "covers", computer)
            print(" ")
     elif player == "Scissors":
        if computer == "Rock":
            print("Defeat!", computer, "crushes", player)
            print(" ")
        else:
            print("Victory!", player, "cut", computer)
            print(" ")
     else:
        print("Misspell,try again!")
        print(" ")
     player = False
     computer = t[randint(0,2)]
