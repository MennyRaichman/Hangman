#Hangman
def print_hangman_ascii_photo(HANGMAN_ASCII_ART, MAX_TRIES):
    print(HANGMAN_ASCII_ART, MAX_TRIES)
#
#
def print_hangman(HANGMAN_PHOTOS, num_of_tries):
    return HANGMAN_PHOTOS[num_of_tries]
#    
# Vrsion 3
def check_win(secret_word, old_letters_guessed):
    space = "_"  
    return space not in show_hidden_word(secret_word, old_letters_guessed)
#
#
def show_hidden_word(secret_word, old_letters_guessed):
    tab = '_ '
    guessed_letters = ''
    for letter in secret_word:
        if letter in old_letters_guessed:
            guessed_letters += letter + ' '
        else:
            guessed_letters += tab
    return guessed_letters
#
# Version 2
def is_valid_input(guess_letter):
    return (len(guess_letter) < 2) and (guess_letter.isalpha())
#
# Vrsion 2
def check_valid_input(guess_letter, old_letter_guesed):
    return is_valid_input(guess_letter) and guess_letter.lower() not in old_letter_guesed
#
#
def try_update_letter_guessed(guess_letter, old_letters_guessed, secret_word):
    guess_letter = guess_letter.lower()
    if check_valid_input(guess_letter, old_letters_guessed):
        if guess_letter in secret_word:
            old_letters_guessed.extend(guess_letter)
            print(show_hidden_word(secret_word, old_letters_guessed))
    else:
        old_letters_guessed.sort()
        print('X')
        print(' -> '.join(old_letters_guessed))
#
# Vrsion 2
def choose_word(list_of_words, WORD_INDEX):
    # index start with 0
    WORD_INDEX = WORD_INDEX - 1
    # if index bigger than the list, start over
    if WORD_INDEX > len(list_of_words):
        WORD_INDEX = WORD_INDEX % len(list_of_words)
    return list_of_words[WORD_INDEX]
    
#
def main():
    # Const definition
    FILE_PATH = ""
    WORD_INDEX = ""
    MAX_TRIES = 6
    GAME_ON = "Let’s start!"
    list_of_words = ['hangman', 'song', 'most', 'broadly', 'song', 'hangman', 'work', 'music', 'work', 'broadly', 'typically']
    HANGMAN_ASCII_ART = """  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/ \n"""
    HANGMAN_PHOTOS = {0:
"""    x-------x""",

1:
"""    x-------x
    |
    |
    |
    |
    |""",

2:
"""    x-------x
    |       |
    |       0
    |
    |
    |""",

3:
"""    x-------x
    |       |
    |       0
    |       | 
    |
    |""",

4:
"""    x-------x
    |       |
    |       0
    |      /|\ 
    |
    |""",

5:
"""    x-------x
    |       |
    |       0
    |      /|\ 
    |      / 
    |""",

6:
"""    x-------x
    |       | 
    |       0 
    |      /|\ 
    |      / \ 
    |"""}
    #Variable defnition
    guess_letter = ""
    secret_word = ""
    space = "_"
    num_of_tries = 0
    old_letters_guessed = []
    
    # Print the Welcome Screen
    print_hangman_ascii_photo(HANGMAN_ASCII_ART, MAX_TRIES)
    # Get index for a word in the list
    WORD_INDEX = int(input("Enter index: "))
    # Calling the choose_word function
    secret_word = choose_word(list_of_words, WORD_INDEX)
    
    # Game ON
    print(GAME_ON)
    # Print the first photo from dict
    print(print_hangman(HANGMAN_PHOTOS, num_of_tries))
    # Print the underline of the secret_word
    print(show_hidden_word(secret_word, old_letters_guessed))
    while num_of_tries < MAX_TRIES:
        # Get the letter
        guess_letter = input("Guess a letter: ").lower()
        # Incorrect input
        if not is_valid_input(guess_letter):
            print('X')
            continue
        # Try update letter guessed 
        try_update_letter_guessed(guess_letter, old_letters_guessed, secret_word)
        #
        if check_win(secret_word, old_letters_guessed):
            print('WIN')
            break            
        # Unlucky guess
        if guess_letter not in secret_word and guess_letter.lower() not in old_letters_guessed:
            old_letters_guessed.extend(guess_letter)
            num_of_tries += 1
            print(':(')
            print(print_hangman(HANGMAN_PHOTOS, num_of_tries))
            print(show_hidden_word(secret_word, old_letters_guessed))
            # Lose
            if num_of_tries == MAX_TRIES:
                print("LOSE")
if __name__ == "__main__":
    main()				