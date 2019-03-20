import matplotlib.pylab as plt
LETTERS = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#white space may be the most frequent letter in english

def frequency_analysis(cipher_text):
    cipher_text = cipher_text.upper() #to make an intetested plain text into Capital letters
    letter_frequency = {}
    for letter in LETTERS:
        letter_frequency[letter] = 0 #intialize the dictionary

    for letter in cipher_text:
        if letter in LETTERS:
            letter_frequency[letter] +=1 #keep incrementing the occurence of the given letter

    return letter_frequency
#plot the histogram of the letter_frequency pairs
def plot_distribution(letter_frequency):
    centers = range(len(LETTERS))
    plt.bar(centers, letter_frequency.values(), align='center', tick_label=letter_frequency.keys())
    plt.xlim([0, len(LETTERS)-1])
    plt.show()

def caesar_crack(cipher_text):
    letter_frequency = frequency_analysis(cipher_text)
    print(letter_frequency)
    plot_distribution(letter_frequency)
if __name__=="__main__":
    cipher_text = 'LZTWLEANQMZQREKWNZIWNHMEMZLZQEAFXEFELZWRFSEUMNQTXTUMZWEFSIEFSENRUTWYFSYEKNLZWZETKELZWRFSENIZFQNXRDEMZEFHMNZ ZIEANIZEWZHTLSNYNTSENSEMNXEIFCEFSIDAMNQZEUWNRFWNQCENSKQZZSYNFQEANYMNSEYMZEHTSYNSZSYFQEYWFINYNTSETKEUMNQTXTUMCDMFXEGZHTRZENSHWZFXNSLQCENSKQZZSYNFQENSEYMZEFSFQCYNHEYWFINYNTSEFXEAZQQDE'
    caesar_crack(cipher_text)