import random

def main():
    randomnum = random.randint(1,10)
    tries=5
    while(tries>0):
        guess = int(input (" Guess a number between 1-10:"))
        if (guess == randomnum):
            print("you win nothing...")
            break
        else:
            print("try again")
            tries = tries - 1
            print("You have " + str(tries) + " tries left")
    if(tries==0):
        input("You lose pay $198 to get 5 more tries.")
        
    
if __name__ == "__main__":
    main() 