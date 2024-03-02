with open("words.txt", encoding="utf-8") as file:
    words = [line.rstrip() for line in file]

wrongs = ""
possible_letters = ["", "", "", "", ""]
rights = ["", "", "", "", ""]


print("\n- Wordle Solver -\n")
print("Usage: 0:grey, 1:orange, 2:green")  # alterar a forma de uso

for i in range(5):
    temp_suggestion = []

    guess = input("Your guess: ").lower()
    results = input("Results: ")

    if len(results) != 5:
        exit("Bad input")

    for i in range(len(results)):
        if results[i] == "0":
            wrongs = wrongs + guess[i]
        elif results[i] == "1":
            possible_letters[i] = guess[i]
        elif results[i] == "2":
            rights[i] = guess[i]
        else:
            exit("Bad input")

    for word in words:
        valid_suggestion = True
        for wrong in wrongs:
            if wrong in word:
                valid_suggestion = False
                break

        for possible in possible_letters:
            if possible not in word:
                valid_suggestion = False
                break

        for n in range(5):
            if word[n] != rights[n] and rights[n] != "":
                valid_suggestion = False
                break

        if valid_suggestion == True:
            temp_suggestion.append(word)
    print(temp_suggestion)
