import time
import random
list=['r','p','s']
#let this game be between you and the computer
"""Rule of rock-paper-scissor is rock beats scissors, 
                                 scissor cuts paper,
                                 paper beats rock  
"""

#the computer will use a random.choice[] to choose from the list


def play():
   #this for-loop is used as a Count to begin the game, it announces "Rock paper scissors GO" 
    for i in range(3):
        time.sleep(1)
        print (list[i], end=" ", flush=True)
    time.sleep(0.5)
    print ("GO!")
    # below is the logic
    player=input(f" 'r' for Rock , 'p' for Paperor  's' for Scissors ")
    comp=random.choice(list)

    if is_win(player,comp):
        print ("You have done it")
        return 
    print( "You lost")
       
def is_win(player,comp):
    if(player=='r' and comp=='s' or player=='s' and comp=='p' or player=='p' and comp=='r'):
        return True
    return False

play()