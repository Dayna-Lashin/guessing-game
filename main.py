import random


def play():
    start = input("\nWelcome to the guessing game! \nWho is guessing? Type 1 to guess and 2 for the computer to guess: ").lower()

    def user_guess():
        correct_guess = False
        random_number = random.randrange(1, 100)

        while not correct_guess:
            user_input = input("\nGuess a number between 0 and 100: ")

            try:
                number = int(user_input)
                if number == random_number:
                    correct_guess = True
                elif number > random_number:
                    print("Too high")
                elif number < random_number:
                    print("Too low")
            except:
                print("Invalid input")

        print("You guessed the right number!\n")

    def computer_guess():
        low = 1
        high = 100
        feedback = ""
        input("\nThink of a number 1-100 and hit enter when you're ready...\n")

        while feedback != "c":
            guess = random.randint(low, high)
            feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
            if feedback == "h":
                high = guess - 1
            elif feedback == "l":
                low = guess + 1

        print(f"\nThe Computer guessed your secret number: {guess}!\n")

    if start == "1":
        user_guess()
    else:
        computer_guess()

    play_again = input("Do you want to play again? Type Y for yes and N for no: ").lower()
    if play_again == "y":
        play()
    else:
        print("\nThanks for playing!")


play()
