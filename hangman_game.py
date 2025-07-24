import random

def play_hangman():
    word_list = [
        "apple", "house", "plane", "snake", "river",
         "cat", "dog", "book", "pen", "tree",
    "sun", "cup", "fish", "milk", "ball"

    ]

    secret_word = random.choice(word_list)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6
    display_word = ["_" for _ in secret_word]

    print("\n🎀 Welcome to Hangman 🎀")
    print("Guess the word, one letter at a time.")
    print("You have 6 chances to guess wrong.\n")

    while wrong_guesses < max_wrong_guesses and "_" in display_word:
        print("Word:", " ".join(display_word))
        print("Guessed letters:", " ".join(guessed_letters))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("✔️ Correct!\n")
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    display_word[i] = guess
        else:
            wrong_guesses += 1
            print(f"❌ Wrong! {max_wrong_guesses - wrong_guesses} guesses left.\n")

    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", secret_word)
    else:
        print("💀 Game over! The word was:", secret_word)

while True:
    play_hangman()
    replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if replay != "yes":
        print("Thanks for playing Hangman! 👋")
        break
