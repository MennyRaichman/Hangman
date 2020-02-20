# B"H
# Hangman
def print_hangman_ascii_photo(HANGMAN_ASCII_ART, MAX_TRIES):
    """this function print the welcome screen
    :param HANGMAN_ASCII_ART: HANGMAN_ASCII_ART value
    :param MAX_TRIES: MAX_TRIES value
    :type HANGMAN_ASCII_ART: int
    :type MAX_TRIES: String
    :return: print
    """
    print(HANGMAN_ASCII_ART, MAX_TRIES)
   
# Vrsion 3
# בודק אם נשארו מרווחים במילה הסודית
def check_win(secret_word, old_letters_guessed):
    """this function checks if the player win
    :param secret_word: secret_word value
    :param old_letters_guessed: old_letters_guessed value
    :param space: space value
    :type secret_word: String
    :type old_letters_guessed: list
    :type spase: String
    :return: True or False if space not in the list
    :rtype: bool
    """
    space = "_"  
    return space not in show_hidden_word(secret_word, old_letters_guessed)

# מראה את המילה הסודית והניחושים הנכונים עד כה במקומם
def show_hidden_word(secret_word, old_letters_guessed):
    """this function shows the secret_word with underline
    :param secret_word: secret_word value
    :param old_letters_guessed: old_letters_guessed value
    :type secret_word: String
    :type old_letters_guessed: list
    :return: True or False if space not in the list
    :rtype: bool
    """
    space = '_ '
    guessed_letters = ''
    for letter in secret_word:
        if letter in old_letters_guessed:
            guessed_letters += letter + ' '
        else:
            guessed_letters += space
    return guessed_letters

# Version 2
# בודק האם התו זה אות באנגלית ולא יותר מתו אחד
def is_valid_input(guess_letter):
    """this function if valid input
    :param guess_letter: guess_letter value
    :type guess_letter: String
    :return: True if is letter and only one charor or False if not
    :rtype: bool
    """
    return (len(guess_letter) < 2) and (guess_letter.isalpha())

# Vrsion 2
# מממש את הפונקציה הקודמת ובודק גם אם כבר נוחש בעבר
def check_valid_input(guess_letter, old_letters_guessed):
    """this function checks if alerady guessed letter
    :param guess_letter: guess_letter value
    :param old_letters_guessed: old_letters_guessed value
    :type guess_letter: String
    :type old_letters_guessed: list
    :return: True if ont yet guessed or False if alerady guessed
    :rtype: bool
    """
    return is_valid_input(guess_letter) and guess_letter not in old_letters_guessed       

# מחזיר אמר אם הניחוש נכון ומוסיף לרשימת הניחושים
# תו לא תקין או שכבר נוחש מדפיס איקס ואת רשימת התווים שנוחשו
def try_update_letter_guessed(guess_letter, old_letters_guessed):
    """this function checks if alerady guessed letter 
    if not add to the old_letters_guessed list
    :param guess_letter: guess_letter value
    :param old_letters_guessed: old_letters_guessed value
    :type guess_letter: String
    :type old_letters_guessed: list
    :return: True if ont yet guessed or print the guessed list if alerady guessed
    :rtype: bool
    """

    #guess_letter = guess_letter.lower()
    if check_valid_input(guess_letter, old_letters_guessed):
        old_letters_guessed.extend(guess_letter)
        return True
    else:
       old_letters_guessed.sort()
       print('X')
       print(' -> '.join(old_letters_guessed))

# Vrsion 2
# בוחר מילה מתוך הקובץ
def choose_word(file_path, index):
    """this function choose a word from words in a file
    :param file_path: file_path value
    :param index: index value
    :type file_path: String
    :type index: int
    :return: the word in the index location
    :rtype: String
    """
    # open the file
    file = open(file_path)
    words = file.read()
    # split by \n to a list of line
    word = words.split(" ")
    # convert list to dict
    dict_of_words = {}
    list_of_words = []
    for value in word:
        if value not in dict_of_words:
            dict_of_words[value] = 1
        else:
            dict_of_words[value] +=1
    list_of_words = list(dict_of_words.keys())
    # index start with 0
    index = index - 1
    # if index bigger than the list, start over
    if index > len(word):
        index = index % len(word)
    file.close()
    return word[index]
# Hangman game - Enjoy
def main():
    # Const definition
    FILE_PATH = ""
    WORD_INDEX = ""
    MAX_TRIES = 6
    GAME_ON = "Let’s start!"
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
    num_of_tries = 0
    #attempts 
    old_letters_guessed = []
    
    # Print the Welcome Screen
    print_hangman_ascii_photo(HANGMAN_ASCII_ART, MAX_TRIES)
    # Get the file path from the user
    FILE_PATH = input("Enter file path: ")
    # Get index for a word in the file
    WORD_INDEX = int(input("Enter index: "))
    # Calling the choose_word function
    secret_word = choose_word(r"C:\\Users\\OSUser\\Desktop\\PythonFiles\\words.txt", WORD_INDEX)
    
    # Game ON
    print(GAME_ON)
    # Print the first photo from dict
    print(HANGMAN_PHOTOS[num_of_tries])
    # Print the underline of the secret_word
    print(show_hidden_word(secret_word, old_letters_guessed))
    while num_of_tries < MAX_TRIES:
        # Get the letter
        guess_letter = input("Guess a letter: ").lower()
        # If incorrect input going back to guess letter
        if not is_valid_input(guess_letter):
            print('X - invalid input')
            continue
        # If correct input
        # If alerady guessed will print 'X' and old_letters_guessed
        if try_update_letter_guessed(guess_letter, old_letters_guessed):
            # If correct guess else wrong guess
            if guess_letter in secret_word:
                print(show_hidden_word(secret_word, old_letters_guessed))
                # If win
                if check_win(secret_word, old_letters_guessed):
                    print('WIN')
                    break 
            #elif guess_letter not in secret_word:
            else:
                num_of_tries += 1
                # print(':(\n' + HANGMAN_PHOTOS[num_of_tries] + '\n' + show_hidden_word(secret_word, old_letters_guessed))
                print(':(')
                print(HANGMAN_PHOTOS[num_of_tries])
                print(show_hidden_word(secret_word, old_letters_guessed))
                # If lose
                if num_of_tries == MAX_TRIES:
                    print("LOSE")

if __name__ == "__main__":

    main()