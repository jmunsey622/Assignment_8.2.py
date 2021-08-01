# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: James Munsey
# Creation Date: <date>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
    cave = ''
            #while cave != '1' and cave != '2':
	        #print('Which cave will you go into? (1 or 2)')
	        #cave = input()
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()
    #Improper indentation
    #return caves
    return cave
    #Improper naming of return value

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    #time.sleep(3)
    time.sleep(2)
    #Sleep counter did not match notes
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
         print('Gives you his treasure!')
    else:
         #print 'Gobbles you down in one bite!'
    		print ('Gobbles you down in one bite!')
    		#Missing parenthesis 

playAgain = 'yes'
#while playAgain = 'yes' or playAgain = 'y':
while playAgain == 'yes' or playAgain == 'y':
#Missing correct equality operators

    displayIntro()
    #caveNumber = choosecave()
    caveNumber = chooseCave()
    #Improper spelling of variable name
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
    #if playAgain == "no":
    if playAgain ==("no"):
    #Missing parenthesis 
      #print("Thanks for planing")  
      print("Thanks for playing")
      #Spelling error
