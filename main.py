import random

def computer_guess(x):
    low = 0
    high = x
    feedback = ''
    trials=0
    
    while feedback != 'c':
        if low != high:
            guessed = random.randint(low, high)
        else:
            guessed = low  # only one possibility left
        try:
            feedback = input(f"Is {guessed} correct? Type 'c' for correct, 'l' if too low, 'h' if too high: ").lower()
            if feedback not in ['c', 'l', 'h']:
                raise ValueError("Invalid feedback input.")
        except ValueError as e:
            print(" Invalid input. Please enter 'c', 'l', or 'h' only.")
            continue
        trials+=1
        if feedback == 'h':
            high = guessed - 1
        elif feedback == 'l':
            low = guessed + 1

    print(f" Congratulations! The computer guessed your number: {guessed} in {trials} trials")


computer_guess(2000)