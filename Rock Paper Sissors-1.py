
import random 

def rock_paper_sissors():
    anwser = int(input("Welcome to Rock, Paper, Sissors. Enter r for Rock, p for Paper, or s for Sissors:"))
    
    Randomchoice = random.choice("Rock","Paper","Sissors")
    #Ties
    if (anwser == r and Randomchoice == Rock):
        print("Tie, Rock, ties with Rock")
    elif (anwser == p and Randomchoice == Paper):
        print("Tie, paper, ties with paper")
    elif (anwser == s and Randomchoice == Sissors):
        print("Tie, Sissors, ties with Sissors")  
    #Anwser = rock
    elif (anwser == r and Randomchoice == Paper):
        print("You lose, paper covers rock") 
    elif (anwser == r and Randomchoice == Sissors):
        print("You win, Rock crushes sissors") 
    #Anwser = Paper
    elif (anwser == p and Randomchoice == Rock):
        print("You win, paper covers rock") 
    elif (anwser == p and Randomchoice == Sissors):
        print("You lose, sissors cut paper")     
    #Anwser = sissors
    elif (anwser == s and Randomchoice == Rock):
        print("You lose, Rock crushes sissors")  
    elif (anwser == s and Randomchoice == Paper):
        print("You win, sissors cuts paper")     
    
  
    
            
    
    
    
rock_paper_sissors()