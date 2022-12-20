#import random
#gussing number
#it so high 
#it low high

import random

n=random.randint(0,10)
choice=3

while choice != 0:

    
    n1=int(input("guess the number:"))
    if n1==n:
        print("your guess the number is correct ! !")
        break
    
    
    elif n1>=n:
        print("your guess the number is high ! !")
        choice -=1
        print("!!! You guess the number is wrong !!!")
        print(f"your choice is {choice} times only")

    
    
    
    elif n1<=n:
        print("you guess the number is low ! !")
        choice -=1
        print("!!! You guess the number is wrong !!!")
        print(f"your choice is {choice} times only")

    
    else:
        print("! Sorry it have only 1-10number gussing not 1above number you guess !!") 


print("!! Thank you play game !!")        