def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        nonlocal guesses
        guesses.append(letter)
        display = "".join([ch if ch in guesses else "_" for ch in secret_word])
        print(display)
        return set(secret_word).issubset(guesses)

    return hangman_closure

# Main
if __name__ == "__main__":
    secret = input("Enter the secret word: ").lower()
    guess_fn = make_hangman(secret)

    while True:
        letter = input("Guess a letter: ").lower()
        if guess_fn(letter):
            print("You guessed the word!")
            break
