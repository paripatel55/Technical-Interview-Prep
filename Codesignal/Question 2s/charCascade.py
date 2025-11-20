'''
Character Cascade from String Array
You are given an array of strings arr. 
Your task is to construct a string from the words in arr, 
starting with the 0th character from each word 
(in the order they appear in arr), followed by the 1st character, 
then the 2nd character, etc. If one of the words doesn't have an 
ith character, skip that word. Return the resulting string.

Example: For arr = ["Daisy", "Rose", "Hyacinth", "Poppy"], 
the output should be solution(arr) = "DRHPaoyoisapsecpyiynth".

'''

def charCascade(arr):
    resStr = "" 
    # find max length word 
    maxLen = max(len(word) for word in arr)
    # loop through from 0 to max length word
    for i in range(maxLen): 
        for word in range(len(arr)): 
            if i < len(arr[word]): 
                resStr += arr[word][i]
    return resStr
                

arr = ["Daisy", "Rose", "Hyacinth", "Poppy"]
print(charCascade(arr))
# Expected: "DRHPaoyoisapsecpyiynth"

arr = ["Hi", "Hello", "Bye"]
print(charCascade(arr))
# Expected: "HBBiYeHlyo" 
# Explanation:
# i=0: H H B → "HHB"
# i=1: i e y → "iey"
# i=2:  l → "l" (only Hello has index 2)
# i=3: l → "l" (only Hello)
# i=4: o → "o" (only Hello)
# Combine: "HHBieyllo"

arr = ["Python"]
print(charCascade(arr))
# Expected: "Python"
