import random
score = 0
while(1):
    
    user = int(input("enter 0 for snake , 1 for water , 2 for gun : "))
    comp = random.randint(0,2)
    print("comp choice: ",comp)
    if(user == 0 and comp == 1 or user == 1 and comp == 2 or user == 2 and comp == 0):
        print("you won")
        score += 1
    elif(user == comp):
        continue
    else:
        print("better luck next time")
        print("YOUR SCORE:",score)
        break
     