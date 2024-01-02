import os

def clear():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Unix/Linux/MacOS
    else:
        _ = os.system('clear')

from data import data
import random

print("Welcome to the Instagram Higher Or Lower game! \n")


score = 0

continueGame = True
while continueGame:
    person1 = random.choice(data)
    person2 = random.choice(data)

    print(f"Compare A: {person1["name"]}, a {person1["description"]}, from {person1["country"]}. \n")
    print("______________________________________________________________________")
    print("______________________________________________________________________")
    print("______________________________________________________________________")
    print(f"Against B: {person2["name"]}, a {person2["description"]}, from {person2["country"]}. \n")
    userChoice = input("Who has more followers on Instagram? (type 'A' or 'B')").lower()
    clear()

    if person1["follower_count"] > person2["follower_count"]:
        moreFollowers = 'a'
    elif person1["follower_count"] == person2["follower_count"]:
        moreFollowers = userChoice 
    else:
        moreFollowers = 'b'

    if moreFollowers == userChoice:
        score += 1
        print(f"Your right! Current score: {score}")
    else:
        continueGame = False
        print(f"Your wrong! Final score: {score}")





