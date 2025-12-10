'''
Largest Shared Digit Count

Prompt:
You are given a list of two-digit integers. A digit is considered shared if it appears in at least one place in multiple numbers. 
Your task is to return the maximum count of any digit across all given integers.

Example:
Input: [55, 15, 57, 18]

Digit 5 appears in: 55, 15, 57 → total 3 numbers
Output: 3
'''

def largest_shared_digit(nums):
    hmap = {} 
    for i in nums: 
        for j in set(str(i)): 
            hmap[j] = hmap.get(j,0) + 1 
    return max(hmap.values())

answer = largest_shared_digit([55,15,57,18])

'''
Collecting Coins with Moving Tokens

You are given a string s consisting of characters:

"." = empty space

"T" = a token

"C" = a coin

Each token can move exactly 3 positions to the right (not less, not more).
A token collects a coin if it lands exactly on a 'C'.

A token can only be used once, and each coin can be collected at most once.

Return the maximum number of distinct coins that can be collected.

Example:
Input: "T..C.TC.C"
Output depends on which tokens can jump exactly 3 steps onto a coin.
'''

def collect_coins(s): 
    maxCount = 0
    s = list(s)
    for i in range(len(s)):
        if s[i] == 'T' and i + 3 < len(s) and s[i+3] == 'C': 
            maxCount += 1
            s[i+3] == '.'
    return maxCount

ans = collect_coins("T..C.TC.C")
print(ans)

'''
1. Frequency Counting / Hash Maps

Learn to count digits, chars, or items efficiently.
Example:

Given a list of strings, return the character that appears in the most strings.
Given an integer list, find the digit that appears most frequently overall.
'''

def freq_count(lst): 
    charCount = {}
    for i in lst: 
        for j in i: 
            charCount[j] = charCount.get(j,0) + 1
    # this gets the key of the max value
    maxValue = max(charCount, key=charCount.get)

def freq_int_count(lst): 
    hmap = {}
    for i in lst: 
        for dig in str(i):
            hmap[dig] = hmap.get(dig,0) + 1 
    maxValue = max(hmap, key=hmap.get)
    return maxValue

'''
2. Digit & String Manipulation

Converting numbers → strings → sets, scanning characters.
Example:

Given a list of integers, return how many have repeated digits.
Check if two numbers share a digit.
'''





'''
3. Sets for Fast Membership Checks

Using set() to dedupe or check overlaps.
Example:

Return true if two words share any common letter.
Count how many integers in a list share at least one digit with a target number.
'''

'''
4. Sliding Window / Single-Pass Scan

Exactly like the coin-collection problem — linear left-to-right pass, checking conditions without skipping.
Example:

Count how many times the pattern 'A?C' appears (A then ANY char then C).
Count 'TxxC' occurrences in a string.
'''

'''
5. Pattern Matching in Strings

Checking for substrings at positions i, i+1, i+2, etc.
Example:

Count how many substrings match 'abc'.
Count occurrences of a pattern with wildcards.
'''
        


            
           
