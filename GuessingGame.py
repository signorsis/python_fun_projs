
import random as r
import time 

def guess(x):
    #takes a number x, which will be a range for the set of the 
    #numbers to guess for 1 upto x
    # user will guess for up to 5 chances and upto it gets it right
    # step1. generate the random number 
    #     2. let the player input a certain guessed number
    #     3. check the number with the random num
    #     4. if not guessed right repeat until he gets it right upto 5 guesses
    #     5. print feed back and results for each trial

    rand_num=r.randint(1,x)
    guess=0 #intialized guess which does not make the guess right
    counter_of_guesses=1 
    while counter_of_guesses<=3 and guess != rand_num:
        
        if (counter_of_guesses==3):
            print(f"you have one last try, GOOD LUCK")  
        if(counter_of_guesses==1):
            guess=int(input (f"guess a number between 1 and {x} : "))
        else:
            guess=int(input (f"try-again: "))
        if(guess<rand_num):
            print (f"Sorry {guess} is low\n")
        elif(guess>rand_num):
             print (f"Sorry {guess} is high\n")
            
        counter_of_guesses +=1
    if(guess==rand_num):
            print(f"Congrats: you have guessed it correctly \ after {counter_of_guesses-1} trial")
    else:
         print("guessing not succesfull")
def computer_guess(x):
     #Computer guesses the number we give it
     #logic
     #we give z computer a number in a certain range
     #and it generates a random int in that range

     print (f"Okay, got it. The number is {x}:  how many guesses will it take it to guess it right")

     counter_of_guesses=0
     guess=0
     while guess!=x:
          guess=r.randint(1,10)
          counter_of_guesses+=1
     
     print (f" It took it {counter_of_guesses} trial to get it right")

def smart_computer_guess(x):
     #now we will let a smart computer play the guessing game
     #we will give it a feedback, like you guessed low or you guessed high
     print (f"Okay, got it. The number is {x}::: how many guesses will it take it to get it right")
     counter_of_guesses=0
     guess=0
     low=1
     high=10

     while guess!=x:
          time.sleep(3)
          if(guess<x):
               if guess !=0:
                    print (f"comuputer your guess: {guess} is, Low")
               low=guess+1
               guess=r.randint(low,high)
          elif(guess>x):
               print (f"comuputer your guess: {guess} is, High")
               high=guess-1
               guess=r.randint(low,high)  
          counter_of_guesses +=1    
     time.sleep(2)
     print (f"comuputer your guess: {x} is Correct\
,it took you {counter_of_guesses} trial to get it right")

smart_computer_guess(int(input("Enter the number for the computer to guess: ")))
# guess(10)