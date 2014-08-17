'''
Created on Aug 17, 2014

@author: Elizabeth
'''

# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions



def number_to_name(comp_number):    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if comp_number == 0:
        comp_name = 'rock'
    elif comp_number == 1:
        comp_name = 'Spock'
    elif comp_number == 2:
        comp_name = 'paper'
    elif comp_number == 3:
        comp_name = 'lizard'
    elif comp_number == 4:
        comp_name = 'scissors'
    else:
        print "Incorrect number given"
        comp_name = None
    return comp_name

    
def name_to_number(player_name):
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if player_name == 'rock':
        player_number = 0
    elif player_name == 'Spock':
        player_number = 1
    elif player_name == 'paper':
        player_number = 2
    elif player_name == 'lizard':
        player_number = 3
    elif player_name == 'scissors':
        player_number = 4
    else:
        player_number = None
        print "Please enter rock, paper, scissors, lizard, or Spock."
    return player_number


def rpsls(player_name):
    player_win = False
    comp_win = False
    tie = False
    
    # convert name to player_number using name_to_number
    player_number = name_to_number(player_name)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randint(0,4)
    
    # compute difference of player_number and comp_number modulo five
    difference = (player_number - comp_number) % 5
    
    # use if/elif/else to determine winner
    if difference == 1 or difference == 2:
        player_win = True
    elif difference == 3 or difference == 4:
        comp_win = True
    else :
        tie = True
        
    # convert comp_number to name using number_to_name
    comp_name = number_to_name(comp_number)
    
    # print results
    if player_win == True:
        print "Player chooses " + player_name
        print "Computer chooses " + comp_name
        print "Player wins!" + "\n"
    elif comp_win == True:
        print "Player chooses " + player_name
        print "Computer chooses " + comp_name
        print "Computer wins!" + "\n"
    else :
        print "Player chooses " + player_name
        print "Computer chooses " + comp_name
        print "Player and Computer tie!" + "\n"

    
# test your code

def main():
    rpsls("rock")
    rpsls("Spock")
    rpsls("paper")
    rpsls("lizard")
    rpsls("scissors")

# always remember to check your completed program against the grading rubric

if __name__ == '__main__':
    main()

