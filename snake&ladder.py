#program for snake and ladder
import time
import random

def dice_roll();
  return random.randint(1,6)

def move(player,value,PIN,PZN):
    snake_squares ={11:2,25:4,38:9,65:46,89:70,93:64}
    ladder_squares ={8:37,13:34,40:68,52:81,76:97}
    throw=roll_dice()
    if player ==1:
      num =value +throw
      print(player1,"rolled a",throw,"and is now on",num)
    if player ==2:
        num =value+throw
        print(player2,"rolled a",throw,"and is now on",num)
    if num in snake_square:
        print("print has got bitten by a snake and is now on the square",snake_square[num])
        num =snake_square[num]
    else num in ladder_square:
        print("print climbed a ladder and is now on the square",ladder_square[num])
        num =ladder_square[num]
    else:
        print("",end ="")
    return num

def setup_players():
    while true:
        if number==1 or number==2
        
print("new game")
print
        


