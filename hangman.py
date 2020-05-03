import random
import os

def print_word_update(guesses, word):
    update = []
    for val in word:
        if val in guesses:
            update.append(val)
        else:
            update.append('*')

    return str(update)

def checker(what, to_check):
    if what == "attempts":
        if not to_check.isdecimal():
            print("please enter a number for the amount of attempts.")
            return False
        else:
            if int(to_check) < 1 or int(to_check) > 10:
                print("number of attempts must be between 1 and 10.")
                return False
        return True
    else:
        if not to_check.isdecimal():
            print("please enter a number for the minimum lenght of word.")
            return False
        else:
            if int(to_check) < 4 or int(to_check) > 25:
                print("Word lengths must be between 4 and 25")
                return False
        return True
def main():

    # clear = lambda: os.system('cls')
    # clear()
    num_attempts = ""
    words = set()
    while True:
        num_attempts = input("How many guesses would you like to get [1-10]? ")
        if checker("attempts", num_attempts) == True:
            num_attempts = int(num_attempts)
            break
    word_length = ""
    while True:
        word_length = input("What is the minimum word length you would like to be given [4-25]? ")
        if checker("wl", word_length) == True:
            word_length = int(word_length)
            break
    word_list = open('wordlist.txt', 'r')
    prev_guesses = []
    for line in word_list.readlines():
        words.add(line.strip())

    word_choice = ""
    while len(word_choice) != word_length:
        word_choice = random.sample(words,1)[0]
    tmp = word_choice
    won = False
    while True:
        if won == True:
            print("Congratulations You Won!!!")
            break
        if num_attempts == 0:
            print("You lose! :(")
            print("The word was {}".format(word_choice))
            break
        print("Word: {}".format(print_word_update(prev_guesses, word_choice)))
        print("Number of guesses remaining: {}".format(num_attempts))
        print("Previous guesses: {}".format(prev_guesses))
        guess = ""
        choice = ""
        while True:
            # print(tmp)
            choice = input("Would you like to guess the letter or the word? [l/w] ")
            if choice == "l":
                while len(guess) != 1:
                    guess = input("Your guess: ")
                    if len(guess) != 1:
                        print("Enter a letter please")
                if guess in tmp:
                    print("Correct!")
                    prev_guesses.append(guess)
                    tmp = tmp.replace(guess.strip(), "")
                    num_attempts -= 1
                else:
                    print("unlucky :(")
                    prev_guesses.append(guess)
                    num_attempts -= 1
                break
            elif choice == "w":
                guess = input("Your guess: ")
                if guess == word_choice:
                    print("Correct!")
                    won = True
                    num_attempts -= 1
                else:
                    print("unlucky :(")
                    num_attempts -= 1
                break
            else:
                print("Enter w or l.")

        if won == True:
            continue
        elif tmp == "":
            won = True


if __name__ == "__main__":
    main()
