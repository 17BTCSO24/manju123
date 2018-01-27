#program for snake and ladder
import random
count=0
while(count<=100):
    a=input("enter 'r' to roll a dice")
    if(a=='r'):
        r=random.randint(1,6)
        count=count+r
    print("Your dice value")
    print(r)
    print("Your count value")
    print(count)
    if(count==8):
        count=37
        print("wow you have climbed a ladder")
    elif(count==11):
        count=2
        print("no snake has bitten you")
    elif(count==13):
        count=34
        print("wow you have climbed a ladder")
    elif(count==25):
        count=4
        print("no snake has bitten you")
    elif(count==38):
        count=9
        print("no snake has bitten you")
    elif(count==40):
        count=68
        print("wow you have climbed a ladder")
    elif(count==52):
        count=81
        print("wow you have climbed a ladder")
    elif(count==65):
        count=46
        print("no snake has bitten you")
    elif(count==76):
        count=97
        print("wow you have climbed a ladder")
    elif(count==89):
        count=90
        print("no snake has bitten you")
    elif(count==93):
        count=64
        print("no snake has bitten you")
    else:
        if count==100:
           print("You have won the game:")
        
        
