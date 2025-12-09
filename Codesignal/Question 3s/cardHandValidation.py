'''
Card Hand Validation
You are provided with a set of cards characterized by suits (+, -, =), 
values (A, B, C), and counts of these values ranging from 1 to 3. Your goal is 
to identify a valid hand from the given cards. A valid hand consists of 3 cards where:

All the suits are either the same or all different,
All the values are either the same or all different,
All the counts are either the same or all different.
Example 1:

Input cards:

{ +AA, -AA, +AA, -C, -B, +AA, -AAA, -A, =AA }
Valid hands could be:

{ +AA, +AA, +AA }
Suit: Same [+ + +]
Value: Same [A A A]
Count: Same [2 2 2]

{ -A, -AA, -AAA }
Suit: Same [- - -]
Value: Same [A A A]
Count: Different [1 2 3]

{ -C, -B, -A }
Suit: Same [- - -]
Value: Different [C B A]
Count: Same [1 1 1]

{ +AA, -AA, =AA }
Suit: Different [+, -, =]
Value: Same [A A A]
Count: Same [2 2 2]
Example 2:

A valid hand can also be:

{ -A, +BB, =CCC }
Suit: Different [+, -, =]
Value: Different [A B C]
Count: Different [1 2 3]
Task:
Write a program to find and return the first valid hand from the provided list of cards. Input will be read from stdin.

For example, given the input:

+AA, -AA, +AA, -C, -B, +AA, -AAA, -A, =AA
Output any valid hand from this set.
'''
# lets assume we are given the list of cards as a string cards
def cardHandValidation(cards): 
    # convert cards string to a list of strings (easy to parse)
    cardsArr = [c.strip() for c in cards.split(',')] # -> ['+AA', '-AA', ..]
    
    n = len(cardsArr)

    # check card combos of 3
    for i in range(n): 
        for j in range(i+1, n): 
            for k in range(j+1, n): 
                c1, c2, c3 = cardsArr[i], cardsArr[j], cardsArr[k]
                suitSet = set()
                valueSet= set()
                countSet = set()
                # add suit, value, and count to a set and check len of set
                suits = [c1[0], c2[0], c3[0]]
                value = [c1[1], c2[1], c3[1]]
                count = [len(c1)-1, len(c2)-1, len(c3)-1]

                for val in range(3): 
                    suitSet.add(suits[val])
                    valueSet.add(value[val])
                    countSet.add(count[val])
                
                if (len(suitSet) in (1,3)) and (len(valueSet) in (1,3)) and (len(countSet) in (1,3)): 
                    return [c1, c2, c3]
    return []


                



