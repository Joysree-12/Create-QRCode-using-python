import random
def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c':
        guess=random.randint(low,high)
        feedback=input(f"Is {guess} too high ,too low or correct?")
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
        
    print(f'yes, computer guess correct, {guess}, number')
computer_guess(7)
        