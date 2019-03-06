alphabet = ' ABCDEFGHIZKLMNOPQRSTUVWXYZ'
key = 5   #i use it for shifting
def caesar_encrypt(plain_text):
    #the encrypted message
    cipher_text = ''
    #make all alphabets in the text to Capital
    plain_text = plain_text.upper()

    for c in plain_text:
        index = alphabet.find(c) #to find the numerical representation
        index = (index+key) % len(alphabet) #to shift the alphabets
        cipher_text = cipher_text + alphabet[index]

    return cipher_text


def caesar_decrypt(cipher_text):
    plain_text = ''
    for c in cipher_text:
        index = alphabet.find(c)
        index = (index - key) % len(alphabet)
        plain_text = plain_text + alphabet[index] #append decrypted alphabets in the plain_text

    return plain_text

if __name__ == "__main__":
    encrypted = caesar_encrypt("This is a lame example")
    print(encrypted)
    decrypted = caesar_decrypt(encrypted)
    print(decrypted)