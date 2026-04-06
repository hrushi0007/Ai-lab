word = "hello"
guessed = ["_"] * len(word)
attempts = 6
guessed_letters = []

while attempts > 0:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("Already guessed!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong!")

    if "_" not in guessed:
        print("\nYou Win! Word:", word)
        break
else:
    print("\nYou Lose! Word was:", word)
