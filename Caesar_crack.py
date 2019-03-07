alphabet = ' ABCDEFGHIZKLMNOPQRSTUVWXYZ'

#cracking the caesar encryption with brute-force
def caesar_crack(cipher_text):
    #going to try all the possible key values as the size of the alphabet
    for key in range(len(alphabet)):
        plain_text = ''
        # a loop in the loop
        for c in cipher_text:
            index = alphabet.find(c)
            # try decrypting the text with a key from 0 to 25
            index = (index-key) % len(alphabet)
            plain_text = plain_text + alphabet[index]
        print('With key %s, the result is : %s'%(key, plain_text))

if __name__ == "__main__":
    encrypted = "YMNXENXEFEQFRZEZBFRUQZ"
    caesar_crack(encrypted)

'''The results as follows
With key 0, the result is : YMNXENXEFEQFRZEZBFRUQZ
With key 1, the result is : XLMWDMWDEDPEQIDIAEQTPI
With key 2, the result is : WKLVCLVCDCODPHCH DPSOH
With key 3, the result is : VZKUBKUBCBNCOGBGZCORNG
With key 4, the result is : UIZTAZTABAMBNFAFYBNQMF
With key 5, the result is : THIS IS A LAME EXAMPLE
With key 6, the result is : SGHRZHRZ ZK LDZDW LOKD
With key 7, the result is : RFGQYGQYZYZZKCYCVZKNZC
With key 8, the result is : QEFPXFPXYXIYZBXBUYZMIB
With key 9, the result is : PDEOWEOWXWHXIAWATXILHA
With key 10, the result is : OCDNVDNVWVGWH V SWHKG 
With key 11, the result is : NBCMUCMUVUFVGZUZRVGZFZ
With key 12, the result is : MABLTBLTUTEUFYTYQUFIEY
With key 13, the result is : L AKSAKSTSDTEXSXPTEHDX
With key 14, the result is : KZ ZR ZRSRCSDWRWOSDGCW
With key 15, the result is : ZYZIQZIQRQBRCVQVNRCFBV
With key 16, the result is : IXYHPYHPQPAQBUPUMQBEAU
With key 17, the result is : HWXGOXGOPO PATOTLPAD T
With key 18, the result is : GVWFNWFNONZO SNSKO CZS
With key 19, the result is : FUVEMVEMNMYNZRMRZNZBYR
With key 20, the result is : ETUDLUDLMLXMYQLQIMYAXQ
With key 21, the result is : DSTCKTCKLKWLXPKPHLX WP
With key 22, the result is : CRSBZSBZKZVKWOZOGKWZVO
With key 23, the result is : BQRAIRAIZIUZVNINFZVYUN
With key 24, the result is : APQ HQ HIHTIUMHMEIUXTM
With key 25, the result is :  OPZGPZGHGSHTLGLDHTWSL
With key 26, the result is : ZNOYFOYFGFRGSKFKCGSVRK'''