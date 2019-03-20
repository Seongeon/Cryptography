LETTERS = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#white space may be the most frequent letter in english

def frequency_analysis(plain_text):
    plain_text = plain_text.upper() #to make an intetested plain text into Capital letters
    letter_frequency = {}
    for letter in LETTERS:
        letter_frequency[letter] = 0 #intialize the dictionary

    for letter in plain_text:
        if letter in LETTERS:
            letter_frequency[letter] +=1 #keep incrementing the occurence of the given letter

        return letter_frequency
#plot the histogram of the letter_frequency pairs
def plot_distribution(letter_frequency):
    centers = range(len(LETTERS))
    plt.bar(centers, letter_frequency.values(), align='center', tick_label=letter_frequency.keys())
    plt.xlim([0, len(LETTERS)-1])
    plt.show()

if __name__=="__main__":
    #plain_text = 'my name is Noe. I'm from south korea. I'm interested in philosophy, economics and computer science.
    plain_text = "Shannon defined the quantity of information produced by a source--for example, the quantity in a message--by a formula similar to the equation that defines thermodynamic entropy in physics. In its most basic terms, Shannon's informational entropy is the number of binary digits required to encode a message."

    frequencies = frequency_analysis(plain_text)
    plot_distribution(frequencies)