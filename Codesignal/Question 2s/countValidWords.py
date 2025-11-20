'''
Count Valid Words from String
Given a string and a list of valid letters, count how many words in the 
string can be formed using the letters in the valid letters list. 
For the input string, words are split using spaces. Punctuation and numbers 
are always considered valid letters. Both uppercase and lowercase are invalid 
for letters not present in the input list.

Example:

Input:
String: "Hello, I am h2ere!"
Letters: "heloiar"
Output: 3
Explanation:
Valid words: "Hello,", "I", "h2ere!".
Invalid word: "am" (as 'm' is not present in the list of valid letters).
'''
import string
def countValidWords(s, letters): 
    # create set to keep in track of valid letters 
    validLetters = set(letters.lower())
    count = 0
    # split string into words
    words = s.split()
    # go through string and check each word 
    for i in words:
        valid = True
        for char in i: 
            if char.isdigit() or char in string.punctuation:
                continue
            if char.lower() not in validLetters: 
                valid = False
                break
        if valid: 
            count += 1
    return count

print(countValidWords("Hello, I am h2ere!", "heloiar"))
print(countValidWords("wow!!! this... is?? cool", "wothoisc"))
