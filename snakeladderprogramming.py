#program for snake and ladder
import random #we are importing a random function
count=0 #intially player position is zero where we start a game
while(count<=100):#we are using while condition that count must be less than are equal to 100
    a=input("enter 'r' to roll a dice")#we are taking input from the user as r
    if(a=='r'):#a is just a variable that we use we are comparing the random variable if this statement is true then the next condition comes
        r=random.randint(1,6)#here r is a random integer from 1 to 6
        count=count+r#we are incrementing the count value
    print("Your dice value")#printing a dice value
    print(r)
    print("Your count value")#printing a count value
    print(count)
    if(count==8):#using if statement we are initiasing a count value
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
        count=70
        print("no snake has bitten you")
    elif(count==93):
        count=64
        print("no snake has bitten you")
    else:
        if count==100:#if count is equal to 100 you have won the game
           print("You have won the game:")
        
        
