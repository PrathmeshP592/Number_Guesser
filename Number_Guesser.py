import random

def guessing_game():
    while True:
        
        random_number = random.randint(1, 100)
        print("Welcome to the Number Guessing Game! You have 5 chances to guess the correct number between 1 and 100.")

        
        for attempts in range(5):
            
            guess = int(input("Enter your guess: "))
            
            
            if guess == random_number:
                print("Congratulations! You guessed the correct number:", random_number)
                break
            
            
            if guess < random_number:
                print("Try again! The number is greater than your guess.")
            else:
                print("Try again! The number is less than your guess.")

        
        else:
            print("Sorry, you've used all your chances.")
            hint_choice = input("Do you want a hint? (yes/no): ").lower()
            if hint_choice == "yes":
                if random_number % 2 == 0:
                    print("Hint: The number is even.")
                else:
                    print("Hint: The number is odd.")
                final_guess = int(input("This is your last chance. Enter your guess: "))
                if final_guess == random_number:
                    print("Congratulations! You guessed the correct number:", random_number)
                else:
                    print("Sorry, your last chance was wrong. The correct number was:", random_number)
            else:
                print("The correct number was:", random_number)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break


guessing_game()
