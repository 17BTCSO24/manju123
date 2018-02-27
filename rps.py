import random
rps=["rock","paper","scissor"]
computer=random.choice(rps)
print("rock","paper","scissor")
user=input("type your choice")
print("computer")
if(computer==user):
    print("it is a tie")
elif(computer=="rock" and user=="scissor"):
        print("computer won")
elif(computer=="rock" and user=="paper"):
        print("user won")
elif(computer=="scissor" and user=="rock"):
        print("user won")
elif(computer=="scissor" and user=="paper"):
        print("computer won")
elif(computer=="paper" and user=="scissor"):
        print("user won")
elif(computer=="paper" and user=="rock"):
        print("computer won")
        
    
    
        
    
