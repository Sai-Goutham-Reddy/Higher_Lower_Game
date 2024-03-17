import random
from game_data import data
from art import logo, vs
from clear import clear

def random_number():
    return random.randint(0, 49)
    
def details(guess):
    return [guess['name'], 
            guess['follower_count'], 
            guess['description'], 
            guess['country']]

play_game = True

while play_game:
    print(logo)
    guess_a = data[random_number()]
    guess_b = data[random_number()]
    score = 0
    list_a = details(guess_a)
    list_b = details(guess_b)
    def description():
        print(f"Comapre A: {list_a[0]}, a {list_a[2]}, from {list_a[3]}")
        print(vs)
        print(f"Against B: {list_b[0]}, a {list_b[2]}, from {list_b[3]}")
    description()
    correct_guess = True
    while correct_guess:
        user_choice = input("Who as more Instagram followers? Type 'A' or 'B': ").upper()
        
        def compare(list_a, list_b, user_choice):
            if list_a[1] > list_b[1] and user_choice == 'A' or \
            list_b[1] > list_a[1] and user_choice == 'B' or \
            list_a[1] == list_b[1]:
                return True
        
        
        if compare(list_a, list_b, user_choice):
            score += 1
            clear()
            print(logo)
            print(f"You're right! current score {score}.")
            list_a = list_b
            list_b = details(data[random_number()])
            description()
            
        else:
            clear()
            print(f"Sorry that is a wrong answer. Final score: {score}")
            correct_guess = False
            if input("Want play game again: Type 'y' or 'n': ").lower() == 'y':
                clear()
                play_game = True
            else:
                play_game = False
        