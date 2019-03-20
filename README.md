# Cryptography
playing with cryptography

# Caesar cipher 
It has only a few possibilities.
can be cracked by Brute force or Frequency analysis. Hence it is very vulnerable and easy to get cracked
 
Frequency analysis seek to information leaking
  
  
Cracking the cipher based on frequencies of alphabet letters (Be aware that the most frequency may be "white space")
  
  
  The frequecny_analysis.py presents that the second most frequent letter is N which refers to shifting the second most frequent alphabet letter 'E' to the right by 9 will be the key. (key = 9)
  
  {' ': 1, 'A': 6, 'B': 0, 'C': 5, 'D': 4, 'E': 40, 'F': 22, 'G': 1, 'H': 7, 'I': 9, 'J': 0, 'K': 6, 'L': 8, 'M': 15, 'N': 33, 'O': 0, 'P': 0, 'Q': 17, 'R': 7, 'S': 23, 'T': 14, 'U': 6, 'V': 0, 'W': 14, 'X': 8, 'Y': 15, 'Z': 28}
  
  And if i use this key value (9) in caesar_crack, the decrypted message appears
