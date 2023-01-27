#  File: TestCipher.py

#  Description: This program ciphers using 2 methods: substitution ciphers 
#         and transposition ciphers. The substitution ciphers replace 
#         individual characters in a string. Transposition ciphers on 
#         the other hand scramble the characters in the string.

#  Student's Name: Julian Canales

#  Student's UT EID: jac22779   
 
#  Partner's Name: Simaak Siddiqi

#  Partner's UT EID: srs5826

#  Course Name: CS 313E 

#  Unique Number: 52038

#  Date Created: 1/24/23

#  Date Last Modified: 1/27/23

import sys

def createMatrix(string, key):
    matrix = []
    # adds rows 
    for i in range(key):
        matrix.append([])
        # adds columns 
        for j in range(len(string)):
            matrix[i].append('')
    return matrix

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode ( strng, key ):
    matrix = createMatrix(strng, key)
    smat = [i for i in strng] 
    sup = key - 1
    i = 0
    for j in range(len(strng)):
        matrix[abs(i)][j] = smat[0]
        if i == sup:
            i *= -1
        i += 1
        smat = smat[1:]
    text = ''
    for i in matrix:
        for j in range(len(strng)):
            if i[j] != '':
                text += i[j]
    return 	text

#  Input: coded string and key
#  Output: list of coordinates 
def findCoord(strng, key):
    sup = key -1
    i = 0
    listOfCoord = []
    for j in range(len(strng)):
        coord = (abs(i),j)
        listOfCoord.append(coord)
        if i == sup:
            i *= -1 
        i += 1
    return listOfCoord

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode ( strng, key ):
    # create an empty matrix
    matrix = createMatrix(strng, key)
    # mark the respective list of coords
    listOfCoords = findCoord(strng, key)
    # make a new list which is the list of coords sorted
    listOfCoords.sort()

    # length to the length of the string bc we are going to change strng
    length = len(strng)

    # put the marked characters in the matrix
    for (a,b) in listOfCoords:
        matrix[a][b] = strng[0]
        strng = strng[1:]
    
    # initialize our return value
    text = ""
    # the max value of i
    sup = key - 1
    # initialize i and j
    i = 0
    j=0
    # add the characters to text
    while j < length:
        text += (matrix[abs(i)][j]) 
        if i == sup:
            i *= -1
        i += 1
        j=j+1
        
    return 	text

#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string ( strng ):
    temp = [i for i in strng if (ord(i) <= 122 and ord(i) >= 97)]
    return "".join(temp)

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def encode_character (p, s):
    return chr(((ord(p)+ord(s) - 97*2) % 26) + 97)


#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character decoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def decode_character (p, s):
    return chr(((ord(s)-ord(p))%26) + 97)

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode ( strng, phrase ):
    strng = filter_string(strng)
    phrase = filter_string(phrase)
    word = ''
    for i in range(len(strng)):
        word += encode_character(phrase[(i%len(phrase) - len(phrase))], strng[i])
    return word

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode ( strng, phrase ):
    strng = filter_string(strng)
    phrase = filter_string(phrase)
    word = ''
    for i in range(len(strng)):
        word += decode_character(phrase[(i%len(phrase) - len(phrase))], strng[i])
    return word

def main():
    # read the plain text from stdin
    plain_text = sys.stdin.readline().strip()
  
    # read the key from stdin
    key = sys.stdin.readline().strip()

    # encrypt and print the encoded text using rail fence cipher
    print()
    print("Rail Fence Cipher")
    print()
    print("Plain Text: " + plain_text)
    print("Key: " + key)
    print("Encoded Text: " + rail_fence_encode(plain_text, int(key)))

    # read encoded text from stdin
    encoded_text = sys.stdin.readline().strip() 

    # read the key from stdin
    key = sys.stdin.readline().strip()

    # decrypt and print the plain text using rail fence cipher
    print()
    print("Encoded Text: " + encoded_text)
    print("Enter Key: " + key)
    print("Decoded Text: " + rail_fence_decode(encoded_text, int(key)))

    # read the plain text from stdin
    plain_text = sys.stdin.readline().strip()

    # read the pass phrase from stdin
    pass_phrase = sys.stdin.readline().strip()

    # encrypt and print the encoded text using Vigenere cipher
    print()
    print("Vigenere Cipher")
    print()
    print("Plain Text: " + plain_text)
    print("Pass Phrase: " + pass_phrase)
    print("Encoded Text: " + vigenere_encode(plain_text, pass_phrase))

    # read the encoded text from stdin
    encoded_text = sys.stdin.readline().strip()

    # read the pass phrase from stdin
    pass_phrase = sys.stdin.readline().strip()

    # decrypt and print the plain text using Vigenere cipher
    print()
    print("Encoded Text: " + encoded_text)
    print("Pass Phrase: " + pass_phrase)
    print("Decoded Text: " + vigenere_decode(encoded_text, pass_phrase))
  
# The line above main is for grading purposes only.
# # DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()  