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

def repeatedDigits(lst): 
    count = 0
    for i in lst: 
        if len(str(i)) > len(set(str(i))): 
            count += 1 
    return count

def shareDigit(num1, num2): 
    num1set = set(str(num1))
    num2set = set(str(num2))
    return bool(num1set & num2set)


'''
3. Sets for Fast Membership Checks

Using set() to dedupe or check overlaps.
Example:

Return true if two words share any common letter.
Count how many integers in a list share at least one digit with a target number.
'''

def common_letter(w1, w2): 
    w1set = set(w1)
    w2set = set(w2)
    return bool(w1set & w2set)

def share_digit(lst,target): 
    count = 0
    targetSet = set(str(target))
    
    for num in lst: 
        numSet = set(str(num))
        if len(targetSet & numSet) >= 1: 
            count += 1 
    return count

''' 
4. Sliding Window / Single-Pass Scan

Exactly like the coin-collection problem — linear left-to-right pass, checking conditions without skipping.
Example:

Count how many times the pattern 'A?C' appears (A then ANY char then C).
Count 'TxxC' occurrences in a string.
'''

def pattern_count(s): 
    count = 0
    for i in range(len(s)-2): 
        if s[i] == 'A' and s[i+2] == 'C': 
            count += 1
    return count

def pattern_coun2(s): 
    count = 0
    for i in range(len(s)-3): 
        if s[i] == 'T' and s[i+1] == 'x' and s[i+2] == 'x' and s[i+3] == 'C': 
            count += 1 
    return count


'''
5. Pattern Matching in Strings

Checking for substrings at positions i, i+1, i+2, etc.
Example:

Count how many substrings match 'abc'.
Count occurrences of a pattern with wildcards.

'''

def strings_match(s): 
    count = 0
    for i in range(len(s)-2): 
        subStr = s[i:i+3]
        if subStr == 'abc': 
            count += 1 
    return count 

ans = strings_match('abcabcabbabc')
print(ans)

'''
6. Greedy Decisions

Choosing the earliest or best option in one pass.

Example:

Given seats '10010', place a student in the closest open seat.

Seats: '10010' → Place student at the first 0 → index 1 is taken, index 2 is empty → place at index 2.

Count non-overlapping occurrences of 'T..C'.

Pattern: 'TABCTXXTC' → Count non-overlapping 'T..C' → matches: 'TABC' and 'TXTC' → total 2.
'''

def early_placement(s): 
    for i in range(len(s)): 
        if s[i] == '0': 
            return i 

def count_nonoverlap(s): 
    count = 0
    skip = 0
    for i in range(len(s)-3): 
        if skip > 0:
            skip -= 1 
            continue
        if s[i] == 'T' and s[i+3] == 'C': 
            count += 1
            skip = 3
    return count

def count_nonoverlap(s):
    count = 0
    i = 0
    while i <= len(s) - 4:  # pattern length = 4
        if s[i] == 'T' and s[i+3] == 'C':
            count += 1
            i += 4  # skip past this match for non-overlapping
        else:
            i += 1
    return count

'''
7. Index Boundary Safety

Avoiding out-of-range errors (like your s[i+3]).
This is heavily tested.

Example:

Scan for a pattern of length 4 without errors.

String: 'ABCDTABC' → Scan for patterns of length 4 → safe checks:

Index 0-3 → 'ABCD'
Index 1-4 → 'BCDT'
Index 2-5 → 'CDTA'
Index 3-6 → 'DTAB'
Index 4-7 → 'TABC'
Stop at index 5 → would go out of bounds if checked

Only check i+3 if i+3 < len(s).
'''

'''
8. Loop Control (break / continue / advancing i smartly)

Knowing when to move i by 1, when to skip, when NOT to skip.

Example:

Count overlapping vs. non-overlapping occurrences of '11'.

String: '1111'

Overlapping '11' → '11' at 0-1, 1-2, 2-3 → 3 matches
Non-overlapping '11' → '11' at 0-1, skip next, then 2-3 → 2 matches

Skip outdated characters while scanning.

String: 'XOXOXOX' → skip characters after an 'O' → patterns handled without double counting
'''
        


            
           
