from art import logo, vs
from dataset import data
import random


def extract_properties(choice):
    name = choice['name']
    followers = choice['follower_count']
    description = choice['description']
    country = choice['country']
    print(f"{name}, a {description}, from {country}")
    return followers


print(logo)
run_game = True
score = 0
choice_a = random.choice(data)
choice_b = choice_a
while run_game:
    if score > 0:
        print(f"You guessed correct. Current Score: {score}")
    while choice_a['name'] == choice_b['name']:
        choice_b = random.choice(data)
    print("Compare A: ", end='')
    follower_a = extract_properties(choice_a)
    print(vs)
    print("Against B: ", end='')
    follower_b = extract_properties(choice_b)
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    if answer == 'A':
        if follower_a > follower_b:
            score += 1
        else:
            print(f"\nYou Guessed Wrong, Game Over! Final Score: {score}")
            run_game = False
    elif answer == 'B':
        if follower_b > follower_a:
            score += 1
        else:
            print(f"\nYou Guessed Wrong, Game Over! Final Score: {score}")
            run_game = False
    else:
        print(f"\nWrong Input, Game Over! Final Score: {score}")
        run_game = False

    choice_a = choice_b
    if run_game:
        print("\n" * 100)
