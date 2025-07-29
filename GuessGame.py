import random

new = random.randint(1,10)
# print("Random number :",new)


trial =0

while True:
    n = int(input("Enter Guess Number b/w (1-10) : "))
    
    if n == new :
        print(f"Incredible, You Guess Right Number in {trial}-trial")
        break
    
    elif n > new and n<11 :
        print("Hint--Go Little bit lower")
        trial+=1
        
    elif n<new and n>0 :
        print("Hint--Go Little bit Higher")
        trial+=1
        
    else :
        print("You are Wrong! Fucker, Be in your Limit")
        trial+=1

print("Thank You..............")
    
    