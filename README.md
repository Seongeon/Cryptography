# Cryptography
playing with cryptography

# Caesar cipher 
It has only a few possibilities.
can be cracked by Brute force or Frequency analysis. Hence it is very vulnerable and easy to get cracked
 
Frequency analysis seek to information leaking
  
  
Cracking the cipher based on frequencies of alphabet letters (Be aware that the most frequency may be "white space")
  
  
  The frequecny_analysis.py presents that the second most frequent letter is N which refers to shifting the second most frequent alphabet letter 'E' to the right by 9 will be the key. (key = 9)
  
  And if i use this key value (9) in caesar_crack, the decrypted message appears
