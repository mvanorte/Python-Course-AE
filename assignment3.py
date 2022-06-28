#importing the random module
from random import randint


#ndice=5
#this function will roll the dice and works fine
def roll(hand):
    
    #hand=[]
    ndice=5-len(hand)
    #print('Nr dice',ndice, hand)
    for nhand in range(ndice):
        hand.append(randint(1,6))
    
        
    hand.sort()
#print(hand)
    return hand




#this function will calculate the score and works fine
def calc_score(hand):
    straight1=[1,2,3,4,5]
    straight2=[2,3,4,5,6]
    unique=sorted(list(set(hand)))
#print(unique)
    i=0
    j=0
    k=0
    l=0
    pair1=0
    pair2=0
    pair3=0
    score=0
    values=unique
    if len(unique)==1:
        score=1 #five of kind
    elif len(unique)==2:
        for a in range(5):
            if hand[a]==unique[0]: #see how many times first value of hand repeats
                i+=1            #i is first counter
        if i==4:
            score=4 #four of a kind
        elif i==3:
            for a in range(5):
                if hand[a]==unique[1]: #see how many times second value of hand repeats
                    j+=1        #j is second counter
            if j==2:
                score=3 #full house
            #else:
                #score=5 #three of a kind
        elif i==2:
            for a in range(5):
                if hand[a]==unique[1]:
                    j+=1
            if j==3:
                score=3 #full house
        elif i==1:
            score=4 #four of a kind
        

        
    elif unique==straight1 or unique==straight2:
        score=4     #straight
    elif len(unique)==3:
        for a in range(5):
            if hand[a]==unique[0]:
                i+=1
        if i==2:
            pair1+=1
        elif i==3:
            score=5 #three of a kind
        for a in range(5):    
            if hand[a]==unique[1]:
                j+=1
        if j==2:
            pair2+=1
        elif j==3:
            score=5 #three of a kind
        for a in range(5):
         if hand[a]==unique[2]:            
            k+=1
        if k==2:
            pair3+=1
        elif k==3:
            score=5 #three of a kind
        if pair1==1 and pair2==1 and pair3==0:
            score=6         #two pairs
        elif pair1==1 and pair2==0 and pair3==0:
            score=7         #one pair
        elif pair1==0 and pair2==1 and pair3==0:
            score=7         #one pair
        elif pair1==1 and pair3==1 and pair2==0:
            score=6         #two pairs
        elif pair2==1 and pair3==1 and pair1==0:
            score=6         #two pairs
    elif len(unique)==4:
        for a in range(5):
            if hand[a]==unique[0]:
                i+=1
        if i==2:
            pair1+=1
        for a in range(5):
            if hand[a]==unique[1]:
                j+=1
        if j==2:
            pair1+=1
        for a in range(5):
         if hand[a]==unique[2]:
            k+=1
        if k==2:
            pair1+=1
        for a in range(5):
         if hand[a]==unique[3]:
            l+=1
        if l==2:
            pair1+=1
        if pair1==1:
            score=7  #one pair
        
    else:
        score=8             #bust
    return score,values, i, j, k, l,pair1, pair2, pair3

def select(hand):
    
    score, value, i, j, k,l, pair1, pair2, pair3=calc_score(hand)
    unique=sorted(list(set(hand)))
    #print(unique)
    #print(len(unique))
    #kept=0
    if len(unique)==5:
        
        newhand=unique 
        #kept+=4
    elif len(unique)==1:
        newhand=unique #go for five of a kind, no better combination possible
        #kept+=5
    elif len(unique)==2:
        if score==3:
            newhand=hand    #full house done (3+2) (aim for five or four of a kind later)
            #kept+=5
        elif score==4:
            if i==4:
                newhand=[unique[0],unique[0],unique[0],unique[0]]      #keep 4 of a kind, aim for five of a kind later
                #kept+=4
            elif j==4:
                newhand=[unique[1],unique[1],unique[1],unique[1]]      #keep 4 of a kind, aim for five of a kind later
                #kept+=4
    elif len(unique)==3:
        if score==5:
            if i==3:
                newhand=[unique[0],unique[0],unique[0]]     #keep 3 of a kind, aim for 4 or five of a kind later
                #kept+=3
            elif j==3:
                newhand=[unique[1],unique[1],unique[1]]     #keep 3 of a kind, aim for 4 or five of a kind later
                #kept+=3
            elif k==3:
                newhand=[unique[2],unique[2],unique[2]]    #keep 3 of a kind, aim for 4 or five of a kind later
                #kept+=3
        
        elif score==6:
            if pair1==1 and pair2==1:
                newhand=[unique[0],unique[0],unique[1],unique[1]] #keep 2 pairs
                #kept+=4
            elif pair1==1 and pair3==1:
                newhand=[unique[0],unique[0],unique[2],unique[2]] #keep 2 pairs
                #kept+=4
            elif pair2==1 and pair3==1:
                newhand=[unique[1],unique[1],unique[2],unique[2]] #keep 2 pairs
                #kept+=4
        elif score==7:
            if pair1==1:
                newhand=[unique[0],unique[0]] #keep 1 pair
                #kept+=2
            elif pair2==1:
                newhand=[unique[1],unique[1]] #keep 1 pair
                #kept+=2
            elif pair3==1:
                newhand=[unique[2],unique[2]] #keep 1 pair
                #kept+=2
    elif len(unique)==4:
            #if score==7:
                    if i==2:
                        newhand=[unique[0],unique[0]] #keep 1 pair
                        #kept+=2
                    elif j==2:
                        newhand=[unique[1],unique[1]] #keep 1 pair
                        #kept+=2
                    elif k==2:
                        newhand=[unique[2],unique[2]] #keep 1 pair
                        #kept+=2
                        #print('high')
                    elif l==2:
                        newhand=[unique[3], unique[3]] #keep 1 pair
                        #kept+=2
    else:
        newhand=[]
        #kept+=0
        #kept=len(newhand)
    return newhand


#gameplay
print('Welcome to Dice Poker! Beat the computer by getting the highest score!')
#finalhandai=[]
#finalhandplayer=[]
keptplayer=[]
#kept=0
previous_hand=[]
for rounds in range(1,4):
    print('Round', rounds,':')
    #print(previous_hand)
    computerhand=roll(previous_hand)
    #hand=[1,2,3,3,5]
    #computerhand=[1,1,2,4,5]  #to delete
    score=calc_score(computerhand)
    
    previous_hand=select(computerhand)
    print('The computer rolled: ', computerhand)
    print('and kept:',select(computerhand))
    playerhand=roll(keptplayer)
    #finalhandai.append(select(hand))
    #playerhand=[1,1,3,4,5] #to delete
    print('You rolled:', playerhand)
    ans=list(input('Which dice do you want to keep? (choose from 1,2,3,4,5)'))
    #print(ans)
    keptplayer=[]
    for dice in ans:
        keptplayer.append(playerhand[int(dice)-1])


print("The computer's final hand is: ", computerhand)
print("Your final hand is: ", playerhand)
playerscore=calc_score(playerhand)[0]
computerscore=calc_score(computerhand)[0]
#print(playerscore)
#print(computerscore)
if playerscore<computerscore:
    print("Congratulations, you won! :) ")
elif playerscore>computerscore:
    print("Oh no, you lost :( ")
else:
    print("It's a tie! Let's see who wins.")
    for a in range(5):
        if calc_score(playerhand)[1][a]>calc_score(computerhand)[1][a]:
            print("Congratulations, you won! :) ")
            break
        elif calc_score(playerhand)[1][a]<calc_score(computerhand)[1][a]:
            print("Oh no, you lost :( ")
            break
        
            
        
        
        

    
        
    





            


