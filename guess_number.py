import random
def guess(x):
    random_num=random.randint(1,x)
    guess=0
    while guess !=random_num:
        guess=int(input(f"Guess a no between 1 and {x} :"))
        if guess < random_num:
            print("Sorry, guess again, low")
        elif guess > random_num:
            print("Sorry, guess again, high")
        else:
            print(f"congrats,You guess right number, {random_num} correct!!")
            
guess(10)       