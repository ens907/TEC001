import random

while True:
    x = random.randint(1, 10)
    
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == x:
        print("You guessed it right!")
        break 