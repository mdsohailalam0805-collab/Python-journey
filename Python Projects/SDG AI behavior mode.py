
print("SMART DICE GAME")

import random

#behavior tracking
player1_greedy=0
player2_greedy=0

player1_rounds=0
player2_rounds=0

player1_score=0
player2_score=0

score=0
rounds=0

max_rounds=4 #limit

#Randome limit
player1_limit=random.randint(2,4)
player2_limit=random.randint(2,4)

while player1_rounds < max_rounds or player2_rounds < max_rounds:

    #player1 turn
    if player1_rounds < max_rounds:
        input("player_1 click enter to roll dice:")
        choice= input("Roll dice? (yes/no):").lower()
                
        if choice =="yes":
            player1_greedy+=1
            dice1=random.randint(1,6)
            dice2=random.randint(1,6)
        
            print("player1 got:", dice1,dice2)
            
        #reset rule
        
            if dice1==1 and dice2==1:
                print("OH NO! you rolled a 1")
                print("score reset to 0")
                player1_score=0
            else:
                total1=dice1+dice2
                player1_score+=total1
                player1_rounds+=1
                print("player1 total:",total1)
                print("player1 score", player1_score)
                print("player1 rounds:",player1_rounds)
        
            
        #Bonus Rule
        
            if dice1==dice2:
                print("BONUS ! same number rolled +5")
                player1_score+=5
                print("player1 score:",player1_score)
    
    #Greedy limit penalty
    
    if player1_greedy==player1_limit:
            print("greedy penalty -5")
            player1_score-=5
            player1_greedy=0  #greedy reset
            player1_limit=random.randint(2,4)

    else:
            print("turn skipped safe play")
            player1_greedy=0
            
            
       
    print("___////___////___")
     
    #player2 turn
    if player2_rounds < max_rounds:
        input("player_2 click enter to roll dice:")
        choice=input("Roll dice (yes/no):").lower()
        if choice =="yes":
                player2_greedy+=1
                
                dice1=random.randint(1,6)
                dice2=random.randint(1,6)
    
                print("player2 got:", dice1,dice2)
        
        #Reset rule
        
        if dice1==1 and dice2==1:
            print("OH NO! you rolled a 1")
            print("score reset to 0")
        else:
            total2=dice1+dice2
            player2_score+=total2
            player2_rounds+=1
    
            print("player2 total:",total2)
            print("player2 rounds:",player2_rounds)
            
     #Bonus Rule
            
        if dice1==dice2:
            print("BONUS ! same number rolled +5")
            player2_score+=5
            print("player2 score:",player2_score)
            
        #Greedy penalty
        
        if player2_greedy==player2_limit:
            print("greedy penalty -5")
            player2_score-=5
            player2_greedy=0  #greedy reset
            player2_limit=random.randint(2,4)

        else:
         print("turn skipped")
         player2_greedy=0
         
                #GAME OVER
                
print("player1_final score:",player1_score)
print("player2_final score:",player2_score)
print("GAME OVER")
            
            #WINNNER
            
if player1_score > player2_score:
        print("player1 is the winner")
elif player2_score > player1_score:
        print("player2 is the winner")
else:
        print("Game Tie")
        
print(" THANK YOU FOR PLAYING")
        
   