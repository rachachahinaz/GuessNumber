import random

class Game:
    def play(self):
       
        number = random.randint(50, 100)
        tries = 5

        print("Welcome to the Number Guessing Game!")
        print("You have 5 tries to guess the number between 50 and 100.")


        while tries > 0:
            try:

                guess = int(input("Enter your guess please !: "))
                if guess < 50 or guess > 100:
                    print("Please enter a number between 50 and 100.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue


            if guess < number:
                print("Guess higher!")
            elif guess > number:
                print("Guess lower!")
            else:
                print(f"Congratulations! woow You guessed the number: {number}")
                break

            tries -= 1
            if tries == 0:
                print(f"Sorry, you lost! The correct number was {number}.")
            else:
                print(f"You have {tries} tries left.")


if __name__ == "__main__":
    game = Game()
    game.play()
