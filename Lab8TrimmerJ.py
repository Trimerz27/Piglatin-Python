####################################################################################
#        This is a menu driven program that translates a phrase from English       #
#                 to piglatin or piglatin to Engish                                #
#                                                                                  #
#                                                                                  #
#                           Author: Joel Trimmer                                   # 
#                           Date:   11/15/2024                                     #
#                           Version: 1.0.0                                         #
#                                                                                  #
####################################################################################
VOWELS = 'aeiou'
VOWEL_SUFFIX = 'yay'
CONSONANT_SUFFIX = 'ay'

def main():

    welcome = 'Welcome to the Eglish-Piglatin translator.\n'
    print(welcome)

    # display the menu
    displayMenu()
    # priming reed
    option = input('\nSelect the option from the menu. P, E, or X\t')

    while option.upper() != 'X':

        # decision structure for menu option
        if option.upper() == 'P':
            english_to_piglatin()
        elif option.upper() == 'E':
            piglatin_to_english()
        else:
            print('\nYou selected an invalid option.\n')

        displayMenu()
        # modifying statement
        option = input('\nSelect the option from the menu. P, E, or X\t')

    goodbye = '\nThank you for using the English-Piglatin translator.'
    print(goodbye)

def english_to_piglatin():
    print('You selected the option to translate English to Piglatin.')
    phrase = getPhrase()
    # create the list of words in the phrase
    words = phrase.split()
    for word in words:
        # determin if the word starts with a vowel
        firstLetter = word[0]
        if firstLetter.lower() in VOWELS:
            #print(f'The word, {word}, starts with a vowel.')
            word = word + VOWEL_SUFFIX
            print(word)
        else:
            #print(f'the word, {word}, starts with a consonant')
            word = word[1:] + word[0] + CONSONANT_SUFFIX
            print(word)


def piglatin_to_english():
    print('You selected the option to translate piglatin to English.')
    phrase = getPhrase()
    #create the list of words in the phrase
    words = phrase.split()
    # create an empty list and append the translated words to the list
    translated = []
    for word in words:
        suffix = word[-3:]
        # does the word end with a VOWEL_SUFFIX, 'YAY'
        if suffix == VOWEL_SUFFIX:
            # ENGLISH WORDS START WITH A VOWEL
            word = word.rstrip(VOWEL_SUFFIX)
            translated.append(word.lower())
        else:
        # does the word end with the Consonant suffix, 'ay'    
            word = word.rstrip(CONSONANT_SUFFIX)
            word = word[-1] + word[:-1]
            translated.append(word.lower())
    # Join the list of words back into a string (Phrase)
    transPhrase = ' '.join(translated)
    print(f'The Phrase, {phrase}, translated into English is: \n\t{transPhrase}\n')





def getPhrase():
    phrase = input('Enter the phrase you wish to translate')

    return phrase

def displayMenu():
    print('Select P to translate English to piglatin.')
    print('Select E to translate piglatin to English.')
    print('select X to exit the program.')


if __name__ == '__main__':
    main()


            
