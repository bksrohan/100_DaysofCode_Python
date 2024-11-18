import random
from hangman_art import stages, logo, pokemon_logo
from pokemon import pokemon

print(pokemon_logo + logo)
print("NOTE: MR. Mine, and Farfetch'd")
print ("Dont have the period or excalmation and is one word")
print("NOTE: Since there is 2 versions of Nidoran, I only put one to avoid confusion")


lives = 6

chosen_word = random.choice(pokemon)
print(chosen_word)

place_holder = ""

for letter in chosen_word:
    place_holder += "_"
print(place_holder)

game_over = False
correct_letters = []

while not game_over:
    print(f"You have {lives} lives left")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -=1
        print(f"You guessed {guess} that's not in the word")
        print(f"You have {lives} lives left")
        if lives == 0:
            game_over = True
            print("You Lose!")
            print(f"The word was: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("You win.")

    print(stages[lives])