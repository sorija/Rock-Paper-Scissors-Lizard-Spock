# Rock-paper-scissors-lizard-Spock game
import random

# helper functions

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Error: Invalid name."


def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    

# main 
def rpsls(player_choice): 
         
    print ("")
    print "Player chooses" + " " + player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses" + " " + comp_choice
    diff = (comp_number - player_number) % 5

    # determines and announces the winner
    if diff == 1:
        print "Computer wins!"
    elif diff == 2:
        print "Computer wins!"
    elif diff == 3:
        print "Player wins!"
    elif diff == 4:
        print "Player wins!"
    else:
        print "Player and computer tie!"
    

#Interface
print "Welcome to the Rock-paper-scissors-lizard-Spock game! Rules are as follows:"
print " scissors cut paper\n paper covers rock\n lizard poisons Spock\n Spock smashes scissors\n scissors decapitates lizard\n lizard eats paper\n paper disproves Spock\n Spock vaporizes rock\n Rock crushes scissors"
print ("")
print "If you wish to stop the game, enter <<done>>."
print ("")
while True:
    player_choice = raw_input("Enter your choice: ")
    if player_choice == "done":
        print "Goodbye!"
        quit()
    else:
        rpsls(player_choice)




