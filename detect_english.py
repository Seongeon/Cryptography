ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#need a list to store the english words
ENGLISH_WORDS = []

def get_data():
    dictionary = open("/Users/Kevin-S-Hong/desktop/cryptography/cryptography2/english_words.txt", "r")
    #intialize the english words list with the words present in the file
    #every word is in a distinct line
    for word in dictionary.read().split('\n'):
        ENGLISH_WORDS.append(word)

    dictionary.close()

#english words counter
def count_words(text):
    text = text.upper()
    words = text.split(' ')
    matches = 0

    for word in words:
        if word in ENGLISH_WORDS:
            matches +=  1
    return matches

def is_text_english(text):
    matches = count_words(text)

    if (float(matches) / len(text.split('\n'))) * 100 >= 80:
        return True #it is an english text if more than 80% of words in the text are english words

    return False #not an english text

def caesar_crack(cipher_text): #brute force
    for key in range(len(ALPHABET)): #try all the possible key values so the size of the ALPHABET
        plain_text = ''

        for c in cipher_text:
            index = ALPHABET.find(c)
            index = (index-key)%len(ALPHABET)
            plain_text = plain_text + ALPHABET[index]

        if is_text_english(plain_text):
            print("We have managed to crack Caesar cipher, the key is: %s, the message is %s" % (key, plain_text))

if __name__=="__main__":
    get_data()

    encrypted='PNX PIERUQNUVIO RNM RLQIQNPNUIEZAIZIPN VZWIYQRUXAXYQN IZWMIZWIRVYX BZWBIORPC NIXOIPN VZWIRMNZURAVHIQNIZLQRNDNMIERMNI NLXPWRBRXWIRWIQRAIMZGIZWMHEQRUNIY RVZ RUGIRWOUCNWBRZUIERBQRWIBQNILXWBRWNWBZUIB ZMRBRXWIXOIYQRUXAXYQGHQZAIKNLXVNIRWL NZARWPUGIRWOUCNWBRZUIRWIBQNIZWZUGBRLIB ZMRBRXWIZAIENUUHI'
    caesar_crack(encrypted)