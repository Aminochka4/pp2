import random
def game():
    cnt = 1
    x = random.randrange(1,20)
    a = input("Hello! What is your name?\n")
    print ("Well, "+a+", I am thinking of a number between 1 and 20.")
    b = 0
    while(True):
        b = int(input("Take a guess.\n"))
        if(b==x):
            break
        if (b<x):
            print("Your guess is too low.")
    
        else:
            print("Your guess is too high.")
        cnt+=1
    print ("Good job, "+a+"! You guessed my number in ",cnt," guesses!")
# game()